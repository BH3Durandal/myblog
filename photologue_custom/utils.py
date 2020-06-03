import os
import time
from uuid import uuid4


def get_image_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    name = 'img/{}/{}.{}'.format(time.strftime('%Y/%m/%d'), uuid4().hex, ext)
    return name