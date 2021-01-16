import os
import glob
import xml.etree.ElementTree as ET

VAL_PATH =  os.path.join(os.getcwd(), 'dataset_size_changed', 'validation')
COUNTED_PEOPLE_CSV = 'counted_persons.csv'


def count_all_persons():
    persons_counted = []
    for xml_file in glob.glob(VAL_PATH + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        print(len(root.findall('object')))
    

def main():
    count_all_persons()

main()
