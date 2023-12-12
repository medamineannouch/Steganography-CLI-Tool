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

    def plot_bitplanes(image, title):
        # Ensure the image is in the range [0, 255]
        image = (image * 255).astype(int)

        plt.figure(figsize=(12, 8))
        for i in range(8):
            bitplane = (image >> i) & 1
            plt.subplot(2, 4, i + 1)
            plt.imshow(bitplane, cmap='gray', vmin=0, vmax=1)  # Ensure proper normalization
            plt.title(f'Bit {7 - i}')

        plt.suptitle('Bitplanes - ' + title)
        plt.show()