from os.path import join, dirname
from code2image.cls import Code2ImageShadow

c2i = Code2ImageShadow()

# load the source code from this file
with open(__file__) as f:
    code = f.read()

# create the image with highlighted code
img = c2i.highlight(code)

# save the image
img.save(join(dirname(__file__), 'shadow.png'))
