"""MissingNo"""

import hashlib
import binascii

from PIL import Image
from colormap import m255


def create_image(bin_path):
    with open(bin_path, 'rb') as f:
        data = f.read()

    bin_len = len(data)
    hex_data = binascii.hexlify(data)
    sha256_hash = hashlib.sha256(data).hexdigest()

    width = 80
    height = (bin_len // width)
    img = Image.new('RGB', (width+1, height+1))
    pixels = img.load()

    x, y = 0, 0
    for i in range(0, len(hex_data), 2):
        hex_str = hex_data[i:i+2]
        n = int(hex_str, 16)
        pixels[x, y] = tuple(m255[str(n)])
        if x == width:
            y += 1
            x = 0
        else:
            x += 1

    img.save('MissingNo.{0}.png'.format(sha256_hash), 'PNG')
