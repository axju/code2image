from code2image.cls import Code2Image

c2i = Code2Image()

# load the source code from this file
with open(__file__) as f:
    code = f.read()

# create the image with highlighted code
img = c2i.highlight(code)

# save the image
img.save('simple.png')
