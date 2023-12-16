import dwt
import lsb
import evaluate
import cv2
from skimage.metrics import peak_signal_noise_ratio
import xlwt

class SteganographyMenu:
    def __init__(self):
        self.original_image_path = 'Original_image/lena.jpg'
        self.message_to_embed = ''
        self.lsb_encoded_image_path = 'Encoded_image/lena_lsb_encoded.jpg'
        self.dwt_encoded_image_path = 'Encoded_image/lena_dwt_encoded.jpg'
        self.img_original = None

    def get_image_path(self):
        return input("Enter the path of the image: ")

    def get_message_to_embed(self):
        return input("Enter the message to embed: ")

    def encode_lsb(self):
        self.message_to_embed = self.get_message_to_embed()
        image_path = self.get_image_path()
        self.lsb_encoded_image_path = 'Encoded_image/lena_lsb_encoded.jpg'
        lsb.Lsb(2).insert(image_path, self.message_to_embed, self.lsb_encoded_image_path)
        print("Message has been embedded using LSB. Encoded image saved at:", self.lsb_encoded_image_path)

    def encode_dwt(self):
        self.message_to_embed = self.get_message_to_embed()
        image_path = self.get_image_path()
        self.dwt_encoded_image_path = 'Encoded_image/lena_dwt_encoded.jpg'
        dwt.DWT()._dwt_encode(image_path, self.message_to_embed, self.dwt_encoded_image_path)
        print("Message has been embedded using DWT. Encoded image saved at:", self.dwt_encoded_image_path)


    def decode_lsb(self):
        image_path = self.get_image_path()
        lsb_message = lsb.Lsb(2).decode_message(image_path)
        print("The message extracted after LSB steganography: ", lsb_message)

    def decode_dwt(self):
        image_path = self.get_image_path()
        dwt_message = dwt.DWT()._dwt_decode(image_path)
        print("The message extracted after DWT steganography: ", dwt_message)

    def evaluate(self):
        self.original_image_path = self.get_image_path()
        self.img_original = cv2.imread(self.original_image_path)
        self.img_original = cv2.cvtColor(self.img_original, cv2.COLOR_BGR2RGB)

        self.dwt_encoded_image_path = self.get_image_path()
        img_dwt_encoded = cv2.imread(self.dwt_encoded_image_path)
        img_dwt_encoded = cv2.cvtColor(img_dwt_encoded, cv2.COLOR_BGR2RGB)

        self.lsb_encoded_image_path = self.get_image_path()
        img_lsb_encoded = cv2.imread(self.lsb_encoded_image_path)
        img_lsb_encoded = cv2.cvtColor(img_lsb_encoded, cv2.COLOR_BGR2RGB)

        book = xlwt.Workbook()
        sheet1 = book.add_sheet("Sheet 1")
        style_string = "font: bold on , color red; borders: bottom dashed"
        style = xlwt.easyxf(style_string)
        sheet1.write(0, 0, "Original vs Encoded", style=style)
        sheet1.write(1, 1, "MSE", style=style)
        sheet1.write(1, 2, "PSNR", style=style)

        sheet1.write(2, 0, "DWT", style=style)
        sheet1.write(2, 1, evaluate.Compare().meanSquareError(self.img_original, img_dwt_encoded))
        sheet1.write(2, 2, peak_signal_noise_ratio(self.img_original, img_dwt_encoded))

        sheet1.write(3, 0, "LSB", style=style)
        sheet1.write(3, 1, evaluate.Compare().meanSquareError(self.img_original, img_lsb_encoded))
        sheet1.write(3, 2, peak_signal_noise_ratio(self.img_original, img_lsb_encoded))

        book.save("Comparison_result/Comparison_results.xls")
        print("Comparison Results were saved as xls file!")

    def plots(self):

        img_orig = cv2.imread(self.original_image_path)
        img_orig = cv2.cvtColor(img_orig, cv2.COLOR_BGR2RGB)
        img_dwt = cv2.imread(self.dwt_encoded_image_path)
        img_dwt = cv2.cvtColor(img_dwt, cv2.COLOR_BGR2RGB)
        img_lsb = cv2.imread(self.lsb_encoded_image_path)
        img_lsb = cv2.cvtColor(img_lsb, cv2.COLOR_BGR2RGB)
        evaluate.Figs.plot_histogram(img_orig, 'Original Image')
        evaluate.Figs.plot_histogram(img_dwt, 'DWT Encoded Image')
        evaluate.Figs.plot_histogram(img_lsb, 'LSB Encoded Image')

        evaluate.Figs().plot_difference(self.original_image_path, self.dwt_encoded_image_path, 'DWT')
        evaluate.Figs().plot_difference(self.original_image_path, self.lsb_encoded_image_path, 'LSB')

        evaluate.Figs().plot_color_histograms(self.original_image_path, self.dwt_encoded_image_path, 'Color Panel Original vs DWT Encoded Image')
        evaluate.Figs().plot_color_histograms(self.original_image_path, self.lsb_encoded_image_path, 'Color Panel Original vs LSB Encoded Image')


    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Encode Message")
            print("2. Decode Message")
            print("3. Evaluate")
            print("4. Plots")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.encode_menu()
            elif choice == '2':
                self.decode_menu()
            elif choice == '3':
                self.evaluate()
            elif choice == '4':
                self.plots()
            elif choice =='5':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    def encode_menu(self):
        while True:
            print("\n")
            print("1. Encode using LSB method")
            print("2. Encode using DWT method")
            print("3. Back to Main Menu")

            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                self.encode_lsb()
            elif choice == '2':
                self.encode_dwt()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

    def decode_menu(self):
        while True:
            print("\n")
            print("1. Decode LSB encoded image")
            print("2. Decode DWT encoded image")
            print("3. Back to Main Menu")

            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                self.decode_lsb()
            elif choice == '2':
                self.decode_dwt()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    menu = SteganographyMenu()
    menu.main_menu()
