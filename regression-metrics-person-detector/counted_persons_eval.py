import os
import glob
import sys

from utils import label_map_util
from utils import visualization_utils as vis_util
import tensorflow as tf
import numpy as np
import cv2

sys.path.append("..")
print(os.getcwd())

MODEL_NAME = 'inference_graph'
VAL_PATH =  os.path.join(os.getcwd(), 'dataset_size_changed', 'validation')

CWD_PATH = os.getcwd()
TRESHOLD = 0.05
# Path to frozen detection graph .pb file, which contains the model that is used
# for object detection.
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')

# # Path to label map file
PATH_TO_LABELS = os.path.join(CWD_PATH,'training','labelmap.pbtxt')

# # Number of classes the object detector can identify
NUM_CLASSES = 1

# Load the label map.
# Label maps map indices to category names, so that when our convolution
# network predicts `5`, we know that this corresponds to `king`.
# Here we use internal utility functions, but anything that returns a
# dictionary mapping integers to appropriate string labels would be fine
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# # Load the Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)

for img in glob.glob(VAL_PATH + '/*.jpg'):
    # Input tensor is the image
    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

    # Output tensors are the detection boxes, scores, and classes
    # Each box represents a part of the image where a particular object was detected
    detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

    # # The score is shown on the result image, together with the class label.
    detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
    detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

    image = cv2.imread(img)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_expanded = np.expand_dims(image_rgb, axis=0)


    # # Perform the actual detection by running the model with the image as input
    (boxes, scores, classes) = sess.run(
        [detection_boxes, detection_scores, detection_classes],
        feed_dict={image_tensor: image_expanded})

    # scores = np.array(scores)
    print(scores[scores >= TRESHOLD].shape[0])

    # Draw the results of the detection (aka 'visulaize the results')

    vis_util.visualize_boxes_and_labels_on_image_array(
        image,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        use_normalized_coordinates=True,
        line_thickness=1,
        min_score_thresh=TRESHOLD,
        max_boxes_to_draw=None)
    
    cv2.imwrite(os.path.join(CWD_PATH, 'test_inference', os.path.basename(img)), image)
    print('Image saved in ' +os.path.join(CWD_PATH, 'test_inference', os.path.basename(img)))

