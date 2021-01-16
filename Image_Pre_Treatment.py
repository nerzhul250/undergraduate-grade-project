from PIL import Image
import os, sys

_NEW_WIDTH = 1040
_NEW_HEIGHT = 1040
_SOURCE_DIRECTORY = "./dataset/"
_DESTINATION_DIRECTORY = "./dataset_size_changed/"

def change_image_size(source_directory, image_name, new_width, new_height,
    destination_directory):
    image = Image.open(source_directory + image_name)
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    resized_image.save(destination_directory + image_name)


def change_all_directory_images(source_directory, new_width, new_height,
    destination_directory):
    directory = os.listdir(source_directory)
    for image_name in directory:
        if os.path.isfile(source_directory + image_name):
            change_image_size(source_directory, image_name, new_width, new_height,
            destination_directory)

if __name__ == "__main__":
    change_all_directory_images(_SOURCE_DIRECTORY, _NEW_WIDTH, _NEW_HEIGHT,
    _DESTINATION_DIRECTORY)
