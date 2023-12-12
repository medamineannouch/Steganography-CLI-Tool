import dwt
import lsb
import evaluate
import cv2
from skimage.metrics import peak_signal_noise_ratio
import xlwt

def main():
    original_image_path = 'Original_image/lena.jpg'
    message_to_embed = "this is a test message!"

    # Chemins pour l'encodage lsb
    lsb_encoded_image_path = 'Encoded_image/lena_lsb_encoded.jpg'
    # Chemins pour l'encodage dwt
    dwt_encoded_image_path = 'Encoded_image/lena_dwt_encoded.jpg'


    # encodage dwt
    dwt.DWT().dwtEncode(original_image_path, message_to_embed, dwt_encoded_image_path)
    print("Message has been embedded. Encoded image saved at:", dwt_encoded_image_path)

    # encodage lsb
    lsb_encoded_image_path = lsb.Lsb(2).insert(original_image_path, message_to_embed)
    print("Message has been embedded. Encoded image saved at:", lsb_encoded_image_path)



    img_dwt_original= cv2.imread(original_image_path)
    img_dwt_encoded= cv2.imread(dwt_encoded_image_path)
    img_dwt_original = cv2.cvtColor(img_dwt_original, cv2.COLOR_BGR2RGB)
    img_dwt_encoded = cv2.cvtColor(img_dwt_encoded, cv2.COLOR_BGR2RGB)

    img_lsb_original = cv2.imread(original_image_path)
    img_lsb_encoded = cv2.imread(lsb_encoded_image_path)
    img_lsb_original = cv2.cvtColor(img_lsb_original, cv2.COLOR_BGR2RGB)
    img_lsb_encoded = cv2.cvtColor(img_lsb_encoded, cv2.COLOR_BGR2RGB)

    book = xlwt.Workbook()
    sheet1 = book.add_sheet("Sheet 1")
    style_string = "font: bold on , color red; borders: bottom dashed"
    style = xlwt.easyxf(style_string)
    sheet1.write(0, 0, "Original vs Encoded", style=style)
    sheet1.write(1, 1, "MSE", style=style)
    sheet1.write(1, 2, "PSNR", style=style)

    sheet1.write(2, 0, "DWT", style=style)
    sheet1.write(2, 1, evaluate.Compare().meanSquareError(img_dwt_original, img_dwt_encoded))
    sheet1.write(2, 2, peak_signal_noise_ratio(img_dwt_original, img_dwt_encoded))

    sheet1.write(3, 0, "LSB", style=style)
    sheet1.write(3, 1, evaluate.Compare().meanSquareError(img_lsb_original, img_lsb_encoded))
    sheet1.write(3, 2, peak_signal_noise_ratio(img_lsb_original, img_lsb_encoded))

    book.save("Comparison_result/Comparison_results.xls")
    print("Comparison Results were saved as xls file!")




    # Plots


    # Plot frequency spectrum before and after  encoding
    evaluate.Figs.plot_frequency(original_image_path, 'Original Image')
    evaluate.Figs.plot_frequency(dwt_encoded_image_path, 'DWT Encoded Image')
    evaluate.Figs.plot_frequency(lsb_encoded_image_path, 'LSB Encoded Image')


    # Plot histograms
    evaluate.Figs.plot_histogram(img_dwt_original, 'Original Image')
    evaluate.Figs.plot_histogram(img_dwt_encoded, 'DWT Encoded Image')
    evaluate.Figs.plot_histogram(img_lsb_encoded, 'LSB Encoded Image')



if __name__ == "__main__":
    main()

