from code2image.cls import Code2ImageShadow

# only change the class to uses create a shadow box
c2i = Code2ImageShadow()

# load the source code from this file
with open(__file__) as f:
    code = f.read()

# create the image with highlighted code
img = c2i.highlight(code)

# save the image
img.save('shadow-box.png')
