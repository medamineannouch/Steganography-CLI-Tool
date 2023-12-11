import numpy as np
import cv2
import pywt
import copy
from PIL import Image

from numpy import zeros
from numpy import diag
from scipy.linalg import svd

def wordToBit(words):
    result = []
    for c in words:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

# fungsi merubah bit menjadi string
def bitToWord(bits):
    chars = []
    for b in range(len(bits) // 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    flag = ''.join(chars)
    return flag

# fungsi merubah int menjadi bit
def intToBit(val):
    result = list(format(val, "b"))
    result = list(map(int, result))
    return result

# fungsi merubah bit menjadi int
def bitToInt(bit):
    val = ''.join(str(e) for e in bit)
    result = int(val, 2)
    return result

def lsbVal(a, b):
	result = 0
	if a == b:
		result = 0
	elif a == 1 and b == 0:
		result = 2
	elif a == 0 and b == 1:
		result = - 2

	return result

def normalize_coefficients(coefficients):
    # Normalize coefficients by subtracting 1 from odd values
    coefficients[coefficients % 2 != 0] -= 1
    # Clip the coefficients to ensure they are within the valid intensity range (0-255)
    coefficients = np.clip(coefficients, 0, 255)
    return coefficients


def dwtEncode(image_path, msg, encoded_path):
    img= cv2.imread(image_path)
    blue, green, red = cv2.split(img)  # pada opencv menggunakan format b, g, r

    # Proses merubah pesan String to Bit
    bitMessage = wordToBit(msg)

    # mendapatkan panjang pesan
    bitLenght = len(bitMessage)
    index = 0

    # Proses DWT-2D Red
    coeffsr = pywt.dwt2(red, 'haar')
    cAr, (cHr, cVr, cDr) = coeffsr
    # print (cAr)

    # Proses DWT-2D Green
    coeffsg = pywt.dwt2(green, 'haar')
    cAg, (cHg, cVg, cDg) = coeffsg

    # Proses DWT-2D Blue
    coeffsb = pywt.dwt2(blue, 'haar')
    cAb, (cHb, cVb, cDb) = coeffsb


    # inisialisasi cA baru tempat pesan akan disimpan
    cArResult = copy.deepcopy(cAr)
    cAgResult = copy.deepcopy(cAg)
    cAbResult = copy.deepcopy(cAb)

    # Proses menyisipkan pesan ke dalam gambar
    for i in range(len(cAr)):
        for j in range(len(cAr)):
            # red
            if index < bitLenght:
                lsbPixel = intToBit(int(cAr[i, j]))[-2]
                cArResult[i, j] = cAr[i, j] + lsbVal(bitMessage[index], lsbPixel)
                index += 1
            # green
            if index < bitLenght:
                lsbPixel = intToBit(int(cAg[i, j]))[-2]
                cAgResult[i, j] = cAg[i, j] + lsbVal(bitMessage[index], lsbPixel)
                index += 1
            # blue
            if index < bitLenght:
                lsbPixel = intToBit(int(cAb[i, j]))[-2]
                cAbResult[i, j] = cAb[i, j] + lsbVal(bitMessage[index], lsbPixel)
                index += 1

    # Normalize coefficients
    cArResult = normalize_coefficients(cArResult)
    cAgResult = normalize_coefficients(cAgResult)
    cAbResult = normalize_coefficients(cAbResult)
    # convert dengan IDWT Red
    # print(cArResult)
    coeffsr2 = cArResult, (cHr, cVr, cDr)
    idwr = pywt.idwt2(coeffsr2, 'haar')
    idwr = np.uint8(idwr)

    # convert dengan IDWT Green
    coeffsg2 = cAgResult, (cHg, cVg, cDg)
    idwg = pywt.idwt2(coeffsg2, 'haar')
    idwg = np.uint8(idwg)

    # convert dengan IDWT Blue
    coeffsb2 = cAbResult, (cHb, cVb, cDb)
    idwb = pywt.idwt2(coeffsb2, 'haar')
    idwb = np.uint8(idwb)

    ImageResult = cv2.merge((idwb, idwg, idwr))

    cv2.imwrite(encoded_path, ImageResult)


def dwtDecode(image_path):
    img= cv2.imread(image_path)

    # pada opencv menggunakan format b, g, r
    blue, green, red = cv2.split(img)

    # Proses DWT-2D Red
    coeffsr = pywt.dwt2(red, 'haar')
    cAr, (cHr, cVr, cDr) = coeffsr

    # Proses DWT-2D Green
    coeffsg = pywt.dwt2(green, 'haar')
    cAg, (cHg, cVg, cDg) = coeffsg

    # Proses DWT-2D Blue
    coeffsb = pywt.dwt2(blue, 'haar')
    cAb, (cHb, cVb, cDb) = coeffsb
    bit = []

    for i in range(len(cAr)):
        for j in range(len(cAr)):
            if len(intToBit(int(cAr[i, j]))) > 2:
                bit.append(intToBit(int(cAr[i, j]))[-2])
            else:
                bit.append('0')

            if len(intToBit(int(cAg[i, j]))) > 2:
                bit.append(intToBit(int(cAg[i, j]))[-2])
            else:
                bit.append('0')

            if len(intToBit(int(cAb[i, j]))) > 2:
                bit.append(intToBit(int(cAb[i, j]))[-2])
            else:
                bit.append('0')

    return bitToWord(bit)

def dwtDecode2(image_path):
    img = cv2.imread(image_path)
    blue, green, red = cv2.split(img)

    # Proses DWT-2D Red
    coeffsr = pywt.dwt2(red, 'haar')
    cAr, (cHr, cVr, cDr) = coeffsr

    # Proses DWT-2D Green
    coeffsg = pywt.dwt2(green, 'haar')
    cAg, (cHg, cVg, cDg) = coeffsg

    # Proses DWT-2D Blue
    coeffsb = pywt.dwt2(blue, 'haar')
    cAb, (cHb, cVb, cDb) = coeffsb

    bit = []

    for i in range(min(len(cAr), len(cAg), len(cAb))):  # Use the minimum length to avoid index out of bounds
        for j in range(min(len(cAr[i]), len(cAg[i]), len(cAb[i]))):
            # Red channel
            if i < len(cAr) and j < len(cAr[i]):
                bit.append(intToBit(int(cAr[i, j]))[-2])

            # Green channel
            if i < len(cAg) and j < len(cAg[i]):
                bit.append(intToBit(int(cAg[i, j]))[-2])

            # Blue channel
            if i < len(cAb) and j < len(cAb[i]):
                bit.append(intToBit(int(cAb[i, j]))[-2])

    return bitToWord(bit)


def decode_message(image_path):
    original_image = Image.open(image_path)
    pixel = list(original_image.getdata())

    binary_message = ""
    for i in range(len(pixel)):
        for offset in range(3):
            value = 0
            if pixel[i][offset] % 2 != 0:
                value = 1
            binary_message += str(value)

    output = ""
    for i in range(0, len(binary_message), 8):
        c = 0
        for j in range(8):
            c <<= 1
            c |= int(binary_message[i + j])

        output += chr(c)

    return output

def main():
    original_image_path = "Original_image/lena.jpg"
    message_to_embed = "Hello world!"

    # Chemins pour l'encodage
    encoded_image_path = "Encoded_image/encoded_image3.jpg"


    # Testez la fonction d'encodage
    dwtEncode(original_image_path, message_to_embed,encoded_image_path)
    #print("Message has been embedded. Encoded image saved at:", encoded_image_path)

    # Testez la fonction d'extraction
#    extracted_message = dwtDecode(original_image_path)
    extracted_message = dwtDecode(encoded_image_path)

    print("Extracted Message:\n", extracted_message)

if __name__ == "__main__":
    main()

