import numpy as np
from ipywidgets import interact, fixed
from PIL import Image

def imshow(X, resize=None):
    image=Image.fromarray(img)
    if resize!=None:
        image = image.resize((new_width, new_height), Image.ANTIALIAS)
    image.show()
    pass
