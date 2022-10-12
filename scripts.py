#  https://datagy.io/python-resize-image-pillow/
# Installing the Pillow library
pip install pillow
# conda install pillow

# Opening an Image using Pillow
from PIL import Image
with Image.open ('https://e6v4p8w2.rocketcdn.me/Users/datagy/Desktop/Original.png') as im:
    im.show()

# Getting Dimensions of an Image in Pillow
from PIL import Image
with Image.open ('https://e6v4p8w2.rocketcdn.me/Users/datagy/Desktop/Original.png') as im:
    print(im.size)

# Returns: (930, 620)

# The Python Pillow .resize() Method
Image.resize(
    size,               # Tuple representing size
    resample=None,      # Optional resampling filter
    box=None,           # Optional bounding box to resize
    reducing_gap=None   # Optional optimization
    )

# Resizing an Image using Pillow .resize()
from PIL import Image
with Image.open ('https://e6v4p8w2.rocketcdn.me/Users/datagy/Desktop/Original.png') as im:
    resized = im.resize((600,400))
    resized.show()

# Saving a Resized Image in Python Pillow
from PIL import Image
with Image.open ('https://e6v4p8w2.rocketcdn.me/Users/datagy/Desktop/Original.png') as im:
    resized = im.resize((600,400))
    resized.save('https://e6v4p8w2.rocketcdn.me/Users/datagy/Desktop/Resized.png')

# Resizing an Image by Percentage
from PIL import Image

def resize_by_percentage(image, outfile, percentage):
    with Image.open (image) as im:
        width, height = im.size
        resized_dimensions = (int(width * percentage), int(height * percentage))
        resized = im.resize(resized_dimensions)
        resized.save(outfile)

resize_by_percentage('https://e6v4p8w2.rocketcdn.me/Users/datagy/Desktop/Original.png', 'https://e6v4p8w2.rocketcdn.me/Users/datagy/Desktop/Resized.png', 0.5)

# Using .thumbnail() to Maintain Aspect Rations
from PIL import Image

with Image.open('https://e6v4p8w2.rocketcdn.me/Users/datagy/Desktop/Original.png') as im:
    print(im.size)
    im.thumbnail((300, 150))
    print(im.size)

# Returns: 
# (930, 620)
# (225, 150)

# Saving a Resized Image Using Pillow
from PIL import Image

with Image.open('/Users/datagy/Desktop/Original 2.png') as im:
    im.thumbnail((300, 150))
    im.save('https://e6v4p8w2.rocketcdn.me/Users/datagy/Desktop/thumbnail.png')

# Resize all Images in a Directory
from PIL import Image
import os

directory = '/Users/datagy/Desktop/images'
for file in os.listdir(directory):
    if file.endswith(('jpeg', 'png', 'jpg')):
        filepath = os.path.join(directory, file)
        outfile = os.path.join(directory, 'resized_'+file)
        with Image.open(directory+'/'+file) as im:
            im.thumbnail((300, 200))
            im.save(outfile)