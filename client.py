import os
import requests
from io import BytesIO
import base64
img_data = None
path = os.path.join('./static','22.jpg')
with open(path, 'rb') as fh:
img_data = fh.read()
b64 = base64.b64encode(img_data)
jsondata = {'imagebin':b64.decode('utf-8')}

