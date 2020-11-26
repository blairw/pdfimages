# In Ubuntu package manager: sudo apt-get install -y poppler-utils
# In Python venv: python3 -m pip install pdf2image

import glob
from pdf2image import convert_from_path
from PIL import Image

my_files = glob.glob("./01-input/*.pdf")
for this_file_path in my_files:
    this_filename = this_file_path.rsplit('/', 1)[-1]

    # use pdf2image to convert from PDF
    my_images = convert_from_path(this_file_path)
    my_rgb_images = []

    # use PIL to convert back to PDF
    counter = 0
    for this_image in my_images:
        my_rgb_images.append(my_images[counter].convert('RGB'))
        counter += 1
    
    # a little trick from https://datatofish.com/images-to-pdf-python/
    im1 = my_rgb_images[0]
    destination_name = './02-output/' + this_filename
    im1.save(destination_name, save_all=True, append_images=my_rgb_images[1:])