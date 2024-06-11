#Place your image in the folder with the ref.png, then run the script.

from PIL import Image

im = Image.open('turdle2.png', 'r')
pix_val = list(im.getdata())

ref = Image.open('ref.png', 'r')
ref_val = list(ref.getdata())

final_img = []

for i in pix_val:
    
    for j in ref_val:
        if i == j:
            print('match')
            final_img.append(ref_val.index(j))

print(final_img)