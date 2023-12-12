import numpy as np
import cv2
import pywt
import copy
from PIL import Image
from scipy.fft import fft2, fftshift
from skimage.metrics import peak_signal_noise_ratio
import math
import xlwt
from scipy import signal
import matplotlib.pyplot as plt
class DWT():
    def wordToBit(self,words):
        result = []
        for c in words:
            bits = bin(ord(c))[2:]
            bits = '00000000'[len(bits):] + bits
            result.extend([int(b) for b in bits])
        return result

    # fungsi merubah bit menjadi string
    def bitToWord(self,bits):
        chars = []
        for b in range(len(bits) // 8):
            byte = bits[b*8:(b+1)*8]
            chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
        flag = ''.join(chars)
        return flag

    # fungsi merubah int menjadi bit
    def intToBit(self,val):
        result = list(format(val, "b"))
        result = list(map(int, result))
        return result

    # fungsi merubah bit menjadi int
    def bitToInt(self,bit):
        val = ''.join(str(e) for e in bit)
        result = int(val, 2)
        return result

    def lsbVal(self,a, b):
        result = 0
        if a == b:
            result = 0
        elif a == 1 and b == 0:
            result = 2
        elif a == 0 and b == 1:
            result = - 2

        return result

    def normalize_coefficients(self,coefficients):
        # Normalize coefficients by subtracting 1 from odd values
        coefficients[coefficients % 2 != 0] -= 1
        # Clip the coefficients to ensure they are within the valid intensity range (0-255)
        coefficients = np.clip(coefficients, 0, 255)
        return coefficients


    def dwtEncode(self,image_path, msg, encoded_path):
        img= cv2.imread(image_path)
        blue, green, red = cv2.split(img)  # pada opencv menggunakan format b, g, r

        # Proses merubah pesan String to Bit
        bitMessage = self.wordToBit(msg)

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
                    lsbPixel = self.intToBit(int(cAr[i, j]))[-2]
                    cArResult[i, j] = cAr[i, j] + self.lsbVal(bitMessage[index], lsbPixel)
                    index += 1
                # green
                if index < bitLenght:
                    lsbPixel = self.intToBit(int(cAg[i, j]))[-2]
                    cAgResult[i, j] = cAg[i, j] + self.lsbVal(bitMessage[index], lsbPixel)
                    index += 1
                # blue
                if index < bitLenght:
                    lsbPixel = self.intToBit(int(cAb[i, j]))[-2]
                    cAbResult[i, j] = cAb[i, j] + self.lsbVal(bitMessage[index], lsbPixel)
                    index += 1

        # Normalize coefficients --- needs more actions
        #cArResult = self.normalize_coefficients(cArResult)
        #cAgResult = self.normalize_coefficients(cAgResult)
        #cAbResult = self.normalize_coefficients(cAbResult)



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


    def dwtDecode(self,image_path):
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
                if len(self.intToBit(int(cAr[i, j]))) > 2:
                    bit.append(self.intToBit(int(cAr[i, j]))[-2])
                else:
                    bit.append('0')

                if len(self.intToBit(int(cAg[i, j]))) > 2:
                    bit.append(self.intToBit(int(cAg[i, j]))[-2])
                else:
                    bit.append('0')

                if len(self.intToBit(int(cAb[i, j]))) > 2:
                    bit.append(self.intToBit(int(cAb[i, j]))[-2])
                else:
                    bit.append('0')

        return self.bitToWord(bit)

    def dwtDecode2(self,image_path):
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
                    bit.append(self.intToBit(int(cAr[i, j]))[-2])

                # Green channel
                if i < len(cAg) and j < len(cAg[i]):
                    bit.append(self.intToBit(int(cAg[i, j]))[-2])

                # Blue channel
                if i < len(cAb) and j < len(cAb[i]):
                    bit.append(self.intToBit(int(cAb[i, j]))[-2])

        return self.bitToWord(bit)


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


class Compare():
    def correlation(self, img1, img2):
        return signal.correlate2d(img1, img2)

    def meanSquareError(self, img1, img2):
        error = np.sum((img1.astype('float') - img2.astype('float')) ** 2)
        error /= float(img1.shape[0] * img1.shape[1]);
        return error


    def plot_histogram(self,image, ax, title):
        hist = cv2.calcHist([np.array(image)], [0], None, [256], [0, 256])
        ax.plot(hist, color='gray')
        ax.set_title(title)
        ax.set_xlim([0, 256])

class Figs():
    def plot_frequency(original_image_path, title):
        image = cv2.imread(original_image_path, cv2.IMREAD_GRAYSCALE)
        img = cv2.imread(original_image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Compute 2D Fourier Transform
        f_transform = fftshift(fft2(image))

        # Compute magnitude spectrum
        magnitude_spectrum = np.log(np.abs(f_transform) + 1)

        # Display the images
        plt.figure(figsize=(12, 6))

        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Image - ' + title), plt.xticks([]), plt.yticks([])

        plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
        plt.title('Frequency Spectrum - ' + title), plt.xticks([]), plt.yticks([])

        plt.show()

    def plot_histogram(image, title):
        plt.figure(figsize=(8, 5))
        plt.hist(image.flatten(), bins=256, range=[0, 256], color='gray', alpha=0.7)
        plt.title('Histogram - ' + title)
        plt.xlabel('Pixel Intensity')
        plt.ylabel('Frequency')
        plt.show()

    def plot_bitplanes(image, title):
        plt.figure(figsize=(12, 8))
        for i in range(8):
            bitplane = (image >> i) & 1
            plt.subplot(2, 4, i + 1), plt.imshow(bitplane, cmap='gray')
            plt.title(f'Bit {7 - i}')

        plt.suptitle('Bitplanes - ' + title)
        plt.show()

def main():
    original_image_path = 'Original_image/lena.jpg'
    message_to_embed = "wassuuup chabibaaa"

    # Chemins pour l'encodage
    encoded_image_path = 'Encoded_image/lena_encoded.jpg'


    # Testez la fonction d'encodage
    DWT().dwtEncode(original_image_path, message_to_embed,encoded_image_path)
    print("Message has been embedded. Encoded image saved at:", encoded_image_path)

    # Testez la fonction d'extraction
    extracted_message = DWT().dwtDecode(encoded_image_path)

    #print("Extracted Message:\n", extracted_message)
    img1= cv2.imread(original_image_path)
    img2= cv2.imread(encoded_image_path)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    book = xlwt.Workbook()
    sheet1 = book.add_sheet("Sheet 1")
    style_string = "font: bold on , color red; borders: bottom dashed"
    style = xlwt.easyxf(style_string)
    sheet1.write(0, 0, "Original vs", style=style)
    sheet1.write(0, 1, "MSE", style=style)
    sheet1.write(0, 2, "PSNR", style=style)

    sheet1.write(3, 0, "DWT")
    sheet1.write(3, 1, Compare().meanSquareError(img1, img2))
    sheet1.write(3, 2, peak_signal_noise_ratio(img1, img2))


    book.save("Comparison_result/Comparison_results.xls")
    print("Comparison Results were saved as xls file!")



    #########################################
    # Load original and encoded images


    # Plot frequency spectrum before and after encoding
    Figs.plot_frequency(original_image_path, 'Original Image')
    Figs.plot_frequency(encoded_image_path, 'Encoded Image')

    # Plot histograms
    Figs.plot_histogram(img1, 'Original Image')
    Figs.plot_histogram(img2, 'Encoded Image')

    # Plot bitplanes
    Figs.plot_bitplanes(img1, 'Original Image')
    Figs.plot_bitplanes(img2, 'Encoded Image')



if __name__ == "__main__":
    main()

