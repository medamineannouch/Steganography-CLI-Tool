import numpy as np
from scipy.fft import fft2, fftshift
from scipy import signal
import matplotlib.pyplot as plt
import cv2


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



    def plot_difference(self, original_image_path, encoded_image_path, title):
        img_original = cv2.imread(original_image_path)
        img_encoded = cv2.imread(encoded_image_path)
        img_original = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)
        img_encoded = cv2.cvtColor(img_encoded, cv2.COLOR_BGR2RGB)

        # Display the images
        plt.figure(figsize=(12, 6))

        # Original Image Color Panel
        plt.subplot(131)
        plt.imshow(img_original)
        plt.title('Original Image ')
        plt.axis('off')

        # Encoded Image Color Panel
        plt.subplot(132)
        plt.imshow(img_encoded)
        plt.title(title +'Encoded Image ')
        plt.axis('off')


        diff_image = cv2.absdiff(img_original, img_encoded)
        plt.subplot(133)
        plt.imshow(diff_image)
        plt.title('Difference')
        plt.axis('off')

        plt.subplots_adjust(top=0.85)
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.suptitle('Difference Original vs ' + title + 'Encoded Image')
        plt.show()


    def plot_color_histograms(self, original_image_path, encoded_image_path, title):
        img_original = cv2.imread(original_image_path)
        img_encoded = cv2.imread(encoded_image_path)
        img_original = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)
        img_encoded = cv2.cvtColor(img_encoded, cv2.COLOR_BGR2RGB)
        # Display the color histograms
        plt.figure(figsize=(15, 6))

        # Original Image Color Histograms
        plt.subplot(231)
        self.plot_histogram(img_original[:, :, 0], 'Red Channel - Original',color='red')
        plt.subplot(232)
        self.plot_histogram(img_original[:, :, 1], 'Green Channel - Original',color='green')
        plt.subplot(233)
        self.plot_histogram(img_original[:, :, 2], 'Blue Channel - Original',color='blue')

        # Encoded Image Color Histograms
        plt.subplot(234)
        self.plot_histogram(img_encoded[:, :, 0], 'Red Channel - Encoded',color='red')
        plt.subplot(235)
        self.plot_histogram(img_encoded[:, :, 1], 'Green Channel - Encoded',color='green')
        plt.subplot(236)
        self.plot_histogram(img_encoded[:, :, 2], 'Blue Channel - Encoded',color='blue')

        plt.subplots_adjust(top=0.85)
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.suptitle(title)
        plt.show()

    def plot_histogram(img, title,color='grey'):

        hist = cv2.calcHist([np.array(img)], [0], None, [256], [0, 256])
        plt.plot(hist, color)
        plt.title(title)
        plt.xlim([0, 256])
        plt.show()