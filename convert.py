#Place your image in the folder with the image-hodler folder, then run the script.

from progress.spinner import Spinner
from PIL import Image
import numpy as np
import os

def closest(color):
    color = np.array(color)
    distances = np.sqrt(np.sum((colors-color)**2,axis=1))
    return np.where(distances == np.amin(distances))[0][0]

def linedel(num):
    for i in range(num):
        print ('\033[1A\033[K', end='')

def choose():
    while True:
        try:
            choice = int(input("Choose Image to be Converted (by index):"))

            break
        except ValueError:
            linedel(2)
            print("Invalid input. Please enter a suitable number.\r\r")
    return choice

def listitems():
    print()
    for i, imgs in enumerate(img_list):
        print(i, imgs)
    print()

done = False
spinner = Spinner('Processing… ')

img_folder = 'image-holder'
img_list = os.listdir(img_folder)

listitems()
choice = choose()
while choice >= len(img_list) or choice < 0:
    linedel(2)
    print("\rInvalid input. Please enter number associated with an image.")
    choice = choose()

img_file = os.listdir(img_folder)[choice]
img_name = os.path.basename(img_file)
img_path = os.path.join(os.path.basename(img_folder), img_name)

img = Image.open(img_path, 'r')
img.putalpha(255)
img_val = list(img.getdata())

ref = Image.open('ref.png', 'r')
ref_val = list(ref.getdata())
colors = np.array(ref_val)
final_val = []

w, h = img.size
img_out = Image.new(mode='RGB', size=(w, h))

inc = 0
for i in img_val:
    ndx = closest(i)
    final_val.append(ndx)
    xpos = inc % w
    ypos = inc // w
    img_out.putpixel((xpos, ypos), ref_val[ndx])

    if inc % 5000 == 0:
        spinner.next()
    inc += 1
    
done = True
final = ', '.join(str(x) for x in final_val)
with open(img_name + ".txt", "w") as outfile:
    outfile.write(final)
img_out.save('output-' + img_name)
print("\rProcess Completed!")

