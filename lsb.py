import sys
import math
from os import path

import cv2
import numpy as np

class LSB():
    BITS = 2

    HIGH_BITS = 256 - (1 << BITS)
    LOW_BITS = (1 << BITS) - 1
    BYTES_PER_BYTE = math.ceil(8 / BITS)
    FLAG = '%'

    def insert(self,image_path, msg, encoded_path):
        img = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)
        # Save origin shape to restore image
        ori_shape = img.shape
        print('original shape: ', ori_shape)
        max_bytes = ori_shape[0] * ori_shape[1] // self.BYTES_PER_BYTE
        # Encode message with length
        msg = '{}{}{}'.format(len(msg), self.FLAG, msg)
        assert max_bytes >= len(
            msg), "Message greater than capacity:{}".format(max_bytes)
        data = np.reshape(img, -1)
        for (idx, val) in enumerate(msg):
            self.encode(data[idx * self.BYTES_PER_BYTE: (idx + 1) * self.BYTES_PER_BYTE], val)

        img = np.reshape(data, ori_shape)

        cv2.imwrite(encoded_path, img)

    def encode(self,block, data):
        # returns the Unicode code from a given character
        data = ord(data)
        for idx in range(len(block)):
            block[idx] &= self.HIGH_BITS
            block[idx] |= (data >> (self.BITS * idx)) & self.LOW_BITS



    def extract(self,image_path):
        img = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)
        data = np.reshape(img, -1)
        total = data.shape[0]
        res = ''
        idx = 0
        # Decode message length
        while idx < total // self.BYTES_PER_BYTE:
            ch = self.decode(data[idx * self.BYTES_PER_BYTE: (idx + 1) * self.BYTES_PER_BYTE])
            idx += 1
            if ch == self.FLAG:
                break
            res += ch
        end = int(res) + idx
        assert end <= total // self.BYTES_PER_BYTE, "Input image isn't correct."

        secret = ''
        while idx < end:
            secret += self.decode(data[idx * self.BYTES_PER_BYTE: (idx + 1) * self.BYTES_PER_BYTE])
            idx += 1
        return secret

    def decode(self,block):
        val = 0
        for idx in range(len(block)):
            val |= (block[idx] & self.LOW_BITS) << (idx * self.BITS)
        return chr(val)
