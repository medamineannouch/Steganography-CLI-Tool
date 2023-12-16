import numpy as np
import cv2
import pywt
import copy

class DWT():
    def __init__(self):
        pass

    def _word_to_bit(self, words):
        # Convert a string of words to a list of bits
        result = []
        for c in words:
            bits = bin(ord(c))[2:]
            bits = '00000000'[len(bits):] + bits
            result.extend([int(b) for b in bits])
        return result

    def _bit_to_word(self, bits):
        # Convert a list of bits to a string of words
        chars = []
        for b in range(len(bits) // 8):
            byte = bits[b*8:(b+1)*8]
            chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
        return ''.join(chars)

    def _int_to_bit(self, val):
        # Convert an integer to a list of bits
        result = list(format(val, "b"))
        result = list(map(int, result))
        return result

    def _bit_to_int(self, bit):
        # Convert a list of bits to an integer
        val = ''.join(str(e) for e in bit)
        result = int(val, 2)
        return result

    def _lsb_val(self, a, b):
        # Determine the least significant bit value
        result = 0
        if a == b:
            result = 0
        elif a == 1 and b == 0:
            result = 2
        elif a == 0 and b == 1:
            result = -2
        return result

    def _normalize_coefficients(self, coefficients):
        # Normalize coefficients by subtracting 1 from odd values and clipping to the valid intensity range
        coefficients[coefficients % 2 != 0] -= 1
        coefficients = np.clip(coefficients, 0, 255)
        return coefficients


    def _modify_coefficients(self, coefficients, bit_message):
        # Modify wavelet coefficients based on the message
        result = copy.deepcopy(coefficients)
        index = 0

        for i in range(len(coefficients)):
            for j in range(len(coefficients[i])):
                # Check if the index is within the bounds of the bit_message
                if index < len(bit_message):
                    # Extract the current coefficient
                    current_coefficient = int(coefficients[i, j])

                    # Convert the coefficient to bits
                    coefficient_bits = self._int_to_bit(current_coefficient)

                    # Ensure that the coefficient has at least 2 bits
                    if len(coefficient_bits) > 1:
                        # Modify the least significant bit (LSB)
                        coefficient_bits[-2] = int(bit_message[index])

                        # Convert the modified bits back to an integer
                        modified_coefficient = self._bit_to_int(coefficient_bits)

                        # Update the result
                        result[i, j] = modified_coefficient
                        index += 1

        return result

    def _dwt_encode(self, image_path, msg,encoded_path):
        # Encode a message in an image using Discrete Wavelet Transform
        img = cv2.imread(image_path)
        blue, green, red = cv2.split(img)

        bit_message = self._word_to_bit(msg)
        bit_length = len(bit_message)

        # Apply DWT to each color channel
        coefficients_r = pywt.dwt2(red, 'haar')
        coefficients_g = pywt.dwt2(green, 'haar')
        coefficients_b = pywt.dwt2(blue, 'haar')

        # Modify wavelet coefficients based on the message
        coefficients_r_result = self._modify_coefficients(coefficients_r[0], bit_message)
        coefficients_g_result = self._modify_coefficients(coefficients_g[0], bit_message)
        coefficients_b_result = self._modify_coefficients(coefficients_b[0], bit_message)

        # Normalize and reconstruct the image
        reconstructed_r = pywt.idwt2((coefficients_r_result, coefficients_r[1]), 'haar')
        reconstructed_g = pywt.idwt2((coefficients_g_result, coefficients_g[1]), 'haar')
        reconstructed_b = pywt.idwt2((coefficients_b_result, coefficients_b[1]), 'haar')

        # Merge the color channels
        image_result = cv2.merge((np.uint8(reconstructed_b), np.uint8(reconstructed_g), np.uint8(reconstructed_r)))
        cv2.imwrite(encoded_path, image_result)


    def _dwt_decode(self, image_path):
        # Decode a message from an image using Discrete Wavelet Transform
        img = cv2.imread(image_path)
        blue, green, red = cv2.split(img)

        # Apply DWT to each color channel
        coefficients_r = pywt.dwt2(red, 'haar')
        coefficients_g = pywt.dwt2(green, 'haar')
        coefficients_b = pywt.dwt2(blue, 'haar')

        bit = []

        # Extract the least significant bit from wavelet coefficients
        for coefficients in [coefficients_r[0], coefficients_g[0], coefficients_b[0]]:
            for i in range(len(coefficients)):
                for j in range(len(coefficients[i])):
                    if len(self._int_to_bit(int(coefficients[i, j]))) > 2:
                        bit.append(self._int_to_bit(int(coefficients[i, j]))[-2])
                    else:
                        bit.append('0')

        # Convert bits to a word
        return self._bit_to_word(bit)





