import sys
import os
from PIL import Image


class JPGtoPNGconverter:
    def __init__(self):
        self.original_directory = sys.argv[1]
        self.new_directory = sys.argv[2]

    def mkdir(self):
        if os.path.exists(self.new_directory) is False:
            os.mkdir(self.new_directory)

    def convert_images(self):
        images_list = os.listdir(self.original_directory)

        for image in images_list:
            old_file_name = self.original_directory + image
            new_file_name = self.new_directory + os.path.splitext(image)[0] + '.png'

            img = Image.open(old_file_name)
            img.convert('L')
            img.save(new_file_name, 'png')


if __name__ == '__main__':
    converter = JPGtoPNGconverter()
    converter.mkdir()
    converter.convert_images()
