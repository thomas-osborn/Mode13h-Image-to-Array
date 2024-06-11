#Place your image in the folder with the image-hodler folder, then run the script.

from PIL import Image
import os

img_folder = 'image-holder'
img_file = os.listdir(img_folder)[0]
img_path = os.path.join(os.path.basename(img_folder), os.path.basename(img_file))

img = Image.open(img_path, 'r')
img_val = list(img.getdata())

ref = Image.open('ref.png', 'r')
ref_val = list(ref.getdata())

final_val = []

for i in img_val:
    for j in ref_val:
        if i == j:
            final_val.append(ref_val.index(j))
            break

print(final_val)
