import numpy as np
from PIL import Image

def create_image(np_array):
    """
    :param np_array: array with color values

    :return: Pillow Image Object
    """

    fin_array = np.zeros((2000, 2000, 3))

    for i in range(2000):
        for j in range(2000):
            num = hex(int(np_array[i, j]))[2:]
            if len(num) < 6:
                num = "0"*(6-len(num)) + num
            fin_array[i][j] = (int(num[0:2], 16), int(num[2:4], 16), int(num[4:6], 16))

    return Image.fromarray(np.uint8(fin_array)).convert('RGB')

