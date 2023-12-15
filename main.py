import dwt
import lsb
import evaluate
import cv2
from skimage.metrics import peak_signal_noise_ratio
import xlwt

def main():
    original_image_path = 'Original_image/lena.jpg'
    message_to_embed = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Hendrerit gravida rutrum quisque non tellus orci. Potenti nullam ac tortor vitae. Consequat mauris nunc congue nisi vitae suscipit tellus mauris a. Habitant morbi tristique senectus et. Odio aenean sed adipiscing diam donec adipiscing tristique risus nec. Urna id volutpat lacus laoreet non curabitur. Cras fermentum odio eu feugiat. Interdum velit laoreet id donec. Eleifend mi in nulla posuere sollicitudin aliquam ultrices sagittis. Tellus molestie nunc non blandit massa enim nec dui. Adipiscing diam donec adipiscing tristique risus nec feugiat in. At risus viverra adipiscing at in tellus integer. Auctor elit sed vulputate mi sit amet mauris commodo quis. Feugiat pretium nibh ipsum consequat nisl vel pretium. Aliquam malesuada bibendum arcu vitae elementum curabitur vitae nunc sed. Neque viverra justo nec ultrices dui.\
Sit amet consectetur adipiscing elit duis tristique sollicitudin nibh. Consequat semper viverra nam libero justo. Consequat ac felis donec et odio pellentesque diam volutpat commodo. Posuere lorem ipsum dolor sit amet consectetur adipiscing. Duis tristique sollicitudin nibh sit. Id volutpat lacus laoreet non. At lectus urna duis convallis convallis tellus id interdum velit. Pharetra pharetra massa massa ultricies. Donec pretium vulputate sapien nec sagittis aliquam malesuada bibendum arcu. Augue ut lectus arcu bibendum at varius vel pharetra vel. Etiam sit amet nisl purus in. Consequat mauris nunc congue nisi vitae suscipit. Tempus quam pellentesque nec nam aliquam sem et tortor. Facilisis leo vel fringilla est ullamcorper eget. Convallis posuere morbi leo urna molestie at elementum. Tempus imperdiet nulla malesuada pellentesque elit eget gravida.\
Nullam vehicula ipsum a arcu cursus vitae congue mauris. Adipiscing enim eu turpis egestas pretium aenean pharetra. Facilisis gravida neque convallis a cras semper auctor neque. Sed vulputate odio ut enim. In nibh mauris cursus mattis molestie a iaculis. Cursus risus at ultrices mi tempus imperdiet nulla malesuada. Egestas tellus rutrum tellus pellentesque eu tincidunt tortor. Ipsum dolor sit amet consectetur adipiscing elit. Enim tortor at auctor urna nunc id cursus metus. Ut aliquam purus sit amet luctus venenatis lectus magna fringilla. Ac odio tempor orci dapibus ultrices in iaculis. Ut aliquam purus sit amet luctus venenatis lectus magna.\
Odio facilisis mauris sit amet massa vitae tortor condimentum lacinia. Volutpat commodo sed egestas egestas fringilla phasellus. Vulputate sapien nec sagittis aliquam. Massa tempor nec feugiat nisl. Condimentum id venenatis a condimentum vitae sapien pellentesque habitant morbi. Amet risus nullam eget felis eget nunc. Sagittis vitae et leo duis ut diam quam nulla. Amet aliquam id diam maecenas ultricies. Rutrum quisque non tellus orci ac auctor augue mauris. Est velit egestas dui id ornare arcu odio ut. Tincidunt praesent semper feugiat nibh.\
Elementum pulvinar etiam non quam lacus suspendisse faucibus interdum. Non enim praesent elementum facilisis. Viverra aliquet eget sit amet tellus. Nisl suscipit adipiscing bibendum est ultricies integer quis auctor. Gravida dictum fusce ut placerat. Libero justo laoreet sit amet cursus sit amet. Luctus accumsan tortor posuere ac ut consequat semper viverra nam. Malesuada fames ac turpis egestas sed tempus urna et. Magna eget est lorem ipsum dolor. Pharetra magna ac placerat vestibulum lectus mauris. Et odio pellentesque diam volutpat commodo. Nisl purus in mollis nunc sed. Eget mauris pharetra et ultrices. Elementum facilisis leo vel fringilla est. Mattis enim ut tellus elementum.\
Diam maecenas sed enim ut sem. Nulla aliquet porttitor lacus luctus accumsan tortor. Nam libero justo laoreet sit. Adipiscing diam donec adipiscing tristique. Tempor commodo ullamcorper a lacus. Massa sed elementum tempus egestas sed sed risus. Eget nullam non nisi est sit amet facilisis magna. Ultrices vitae auctor eu augue ut lectus arcu bibendum. Massa placerat duis ultricies lacus. Proin sed libero enim sed faucibus turpis in. Ullamcorper sit amet risus nullam eget felis eget nunc. Neque vitae tempus quam pellentesque nec nam aliquam. Malesuada fames ac turpis egestas maecenas pharetra convallis. Orci dapibus ultrices in iaculis. Aliquam sem fringilla ut morbi tincidunt augue.\
At in tellus integer feugiat scelerisque varius morbi enim nunc. Risus feugiat in ante metus. Ultrices vitae auctor eu augue. Amet est placerat in egestas erat imperdiet sed. Nibh venenatis cras sed felis eget velit aliquet. Iaculis nunc sed augue lacus viverra vitae congue eu consequat. Id semper risus in hendrerit gravida rutrum. Pulvinar sapien et ligula ullamcorper malesuada proin libero. Blandit volutpat maecenas volutpat blandit aliquam etiam erat velit. Ut pharetra sit amet aliquam id diam. In tellus integer feugiat scelerisque varius morbi enim nunc. Sit amet luctus venenatis lectus magna. Lorem ipsum dolor sit amet consectetur adipiscing elit ut. Quisque non tellus orci ac auctor augue. Urna neque viverra justo nec ultrices dui sapien eget mi.\
Eget egestas purus viverra accumsan in nisl. Interdum posuere lorem ipsum dolor sit amet. Fusce id velit ut tortor pretium viverra suspendisse potenti nullam. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit. Massa id neque aliquam vestibulum. Tempor orci dapibus ultrices in iaculis nunc sed augue lacus. Nunc non blandit massa enim nec dui. Massa tincidunt dui ut ornare lectus sit amet est. Laoreet sit amet cursus sit amet. Odio euismod lacinia at quis risus sed vulputate. Pellentesque diam volutpat commodo sed egestas. Habitant morbi tristique senectus et netus et malesuada. Ultricies mi quis hendrerit dolor magna eget. Tortor posuere ac ut consequat semper viverra nam libero. Pellentesque nec nam aliquam sem et. Tempus imperdiet nulla malesuada pellentesque.\
Proin sed libero enim sed faucibus turpis. Eu lobortis elementum nibh tellus molestie nunc non blandit massa. Nisi est sit amet facilisis magna etiam tempor orci eu. Et tortor consequat id porta. Nunc mi ipsum faucibus vitae aliquet nec ullamcorper sit amet. Cursus mattis molestie a iaculis at erat pellentesque adipiscing commodo. Interdum consectetur libero id faucibus nisl. Egestas pretium aenean pharetra magna. Adipiscing bibendum est ultricies integer. Nunc aliquet bibendum enim facilisis gravida neque convallis. Purus viverra accumsan in nisl nisi scelerisque eu ultrices. Nulla facilisi nullam vehicula ipsum a arcu cursus.\
Et malesuada fames ac turpis egestas maecenas. Urna id volutpat lacus laoreet non curabitur gravida arcu ac. Tellus molestie nunc non blandit. Duis convallis convallis tellus id interdum velit. Mi proin sed libero enim sed faucibus turpis. Placerat in egestas erat imperdiet sed euismod nisi porta lorem. Tempor commodo ullamcorper a lacus vestibulum sed arcu non odio. Sagittis purus sit amet volutpat consequat mauris nunc congue. Aliquam id diam maecenas ultricies mi eget mauris pharetra et. Amet luctus venenatis lectus magna fringilla.\
Ornare aenean euismod elementum nisi quis eleifend. At lectus urna duis convallis convallis tellus id interdum velit. Cursus in hac habitasse platea dictumst. Nam libero justo laoreet sit. Amet massa vitae tortor condimentum lacinia quis vel eros donec. Sem viverra aliquet eget sit amet tellus cras. Tortor vitae purus faucibus ornare suspendisse. Enim lobortis scelerisque fermentum dui faucibus in ornare quam. In vitae turpis massa sed elementum tempus egestas sed sed. Quis hendrerit dolor magna eget est lorem ipsum dolor sit. Non diam phasellus vestibulum lorem sed. Enim ut tellus elementum sagittis vitae et leo duis ut. Varius duis at consectetur lorem donec massa. Amet mattis vulputate enim nulla. Neque convallis a cras semper auctor neque vitae. Aliquet lectus proin nibh nisl condimentum id venenatis a condimentum. Porta nibh venenatis cras sed felis eget velit. Venenatis tellus in metus vulputate eu scelerisque felis. Commodo elit at imperdiet dui. Tortor aliquam nulla facilisi cras fermentum odio.\
Vel eros donec ac odio. Nulla malesuada pellentesque elit eget gravida cum sociis. Quam elementum pulvinar etiam non quam. A pellentesque sit amet porttitor eget dolor morbi. Aliquam id diam maecenas ultricies mi. Nibh mauris cursus mattis molestie a iaculis at. Mauris sit amet massa vitae. Integer vitae justo eget magna. Leo urna molestie at elementum eu facilisis. Vel turpis nunc eget lorem dolor. Adipiscing elit duis tristique sollicitudin nibh. A erat nam at lectus urna duis. Duis at consectetur lorem donec massa sapien faucibus et molestie. Curabitur vitae nunc sed velit dignissim sodales.\
Risus in hendrerit gravida rutrum quisque non. Dui accumsan sit amet nulla facilisi morbi tempus. Id velit ut tortor pretium viverra suspendisse potenti nullam. Quam vulputate dignissim suspendisse in est ante in. Mus mauris vitae ultricies leo integer malesuada nunc. At varius vel pharetra vel turpis nunc eget. Amet nulla facilisi morbi tempus iaculis urna. Magna fringilla urna porttitor rhoncus dolor. Sit amet cursus sit amet dictum sit amet justo donec. Est velit egestas dui id ornare arcu odio ut. A iaculis at erat pellentesque adipiscing commodo elit. Elementum nisi quis eleifend quam adipiscing vitae. Lobortis mattis aliquam faucibus purus. In fermentum et sollicitudin ac orci phasellus egestas. Dignissim suspendisse in est ante in nibh mauris cursus mattis. Ultrices gravida dictum fusce ut placerat orci nulla pellentesque dignissim.\
Tellus id interdum velit laoreet id donec ultrices tincidunt. Turpis massa sed elementum tempus egestas sed. Lacus viverra vitae congue eu consequat ac. Cursus vitae congue mauris rhoncus aenean vel elit scelerisque. Eget mi proin sed libero enim sed faucibus turpis. In dictum non consectetur a erat nam at lectus urna. Proin sagittis nisl rhoncus mattis rhoncus urna. Egestas erat imperdiet sed euismod nisi porta lorem mollis. Consectetur adipiscing elit duis tristique sollicitudin nibh sit amet. Nec ullamcorper sit amet risus nullam eget. Gravida in fermentum et sollicitudin ac orci phasellus egestas tellus. Amet commodo nulla facilisi nullam vehicula ipsum a arcu. Suspendisse sed nisi lacus sed viverra. Sollicitudin nibh sit amet commodo nulla. Auctor elit sed vulputate mi sit.\
Amet justo donec enim diam vulputate. Adipiscing elit duis tristique sollicitudin nibh sit. Massa placerat duis ultricies lacus sed turpis tincidunt id aliquet. Placerat vestibulum lectus mauris ultrices eros. Felis imperdiet proin fermentum leo. Curabitur vitae nunc sed velit dignissim sodales. Vel risus commodo viverra maecenas accumsan lacus vel facilisis. Odio euismod lacinia at quis. Non diam phasellus vestibulum lorem sed risus ultricies tristique. Faucibus vitae aliquet nec ullamcorper sit amet. Pellentesque nec nam aliquam sem et tortor consequat. Arcu felis bibendum ut tristique et. Morbi tincidunt augue interdum velit. Morbi tempus iaculis urna id volutpat. In arcu cursus euismod quis viverra nibh. Nisl pretium fusce id velit ut tortor pretium. Massa sapien faucibus et molestie ac.\
Nec nam aliquam sem et tortor consequat id porta nibh. Blandit turpis cursus in hac habitasse platea. Sed risus ultricies tristique nulla aliquet enim tortor at auctor. Aliquet sagittis id consectetur purus ut faucibus pulvinar. Aliquam etiam erat velit scelerisque in dictum non consectetur. Sit amet nisl purus in mollis nunc sed id. Morbi quis commodo odio aenean sed. Ac tortor dignissim convallis aenean. Scelerisque mauris pellentesque pulvinar pellentesque habitant morbi tristique senectus et. Tempor orci eu lobortis elementum nibh tellus.\
Sed arcu non odio euismod lacinia at quis risus. Gravida rutrum quisque non tellus orci ac auctor. Lacinia at quis risus sed vulputate odio ut enim blandit. Neque volutpat ac tincidunt vitae semper quis lectus. Eget est lorem ipsum dolor sit amet consectetur adipiscing elit. Felis donec et odio pellentesque. Nibh sed pulvinar proin gravida hendrerit. Vitae semper quis lectus nulla at. Aenean vel elit scelerisque mauris pellentesque pulvinar pellentesque. Nec tincidunt praesent semper feugiat nibh sed pulvinar. Sem fringilla ut morbi tincidunt augue interdum velit. Nibh cras pulvinar mattis nunc sed blandit libero volutpat. Quam quisque id diam vel quam elementum pulvinar etiam non. Sed arcu non odio euismod lacinia at. Suscipit adipiscing bibendum est ultricies integer. Metus vulputate eu scelerisque felis imperdiet proin fermentum leo.\
Tellus integer feugiat scelerisque varius morbi enim nunc. Neque gravida in fermentum et sollicitudin ac orci. Nunc consequat interdum varius sit amet mattis vulputate. In nisl nisi scelerisque eu. Et tortor at risus viverra adipiscing at. Nulla posuere sollicitudin aliquam ultrices. Volutpat commodo sed egestas egestas fringilla phasellus faucibus scelerisque eleifend. Malesuada bibendum arcu vitae elementum curabitur vitae nunc sed. Quisque sagittis purus sit amet volutpat consequat mauris. Tortor dignissim convallis aenean et tortor at.\
Urna nunc id cursus metus aliquam eleifend mi in. Mauris cursus mattis molestie a. Purus sit amet luctus venenatis lectus magna. Purus semper eget duis at tellus at urna condimentum mattis. Auctor augue mauris augue neque. Adipiscing bibendum est ultricies integer quis. Vestibulum morbi blandit cursus risus at ultrices mi tempus imperdiet. Orci a scelerisque purus semper eget. Eget dolor morbi non arcu risus quis varius quam. Cursus risus at ultrices mi tempus imperdiet nulla malesuada pellentesque. Id diam vel quam elementum pulvinar etiam non quam.\
Vulputate odio ut enim blandit volutpat. Gravida quis blandit turpis cursus in. Ullamcorper morbi tincidunt ornare massa eget egestas. Quis varius quam quisque id diam vel quam elementum. Turpis nunc eget lorem dolor. Pretium nibh ipsum consequat nisl vel pretium lectus quam id. Id cursus metus aliquam eleifend. Tempor orci eu lobortis elementum nibh tellus molestie. Vitae tempus quam pellentesque nec nam aliquam sem. Egestas quis ipsum suspendisse ultrices gravida dictum fusce. Tristique sollicitudin nibh sit amet commodo. Libero nunc consequat interdum varius sit amet mattis vulputate enim. Dis parturient montes nascetur ridiculus mus mauris. Nunc sed id semper risus in hendrerit gravida. Nibh tellus molestie nunc non blandit massa enim nec. Molestie ac feugiat sed lectus vestibulum mattis."

    # Chemins pour l'encodage lsb
    lsb_encoded_image_path= 'Encoded_image/lena_lsb_encoded.jpg'
    # Chemins pour l'encodage dwt
    dwt_encoded_image_path = 'Encoded_image/lena_dwt_encoded.jpg'


    # encodage dwt
    dwt.DWT()._dwt_encode(original_image_path, message_to_embed, dwt_encoded_image_path)
    print("Message has been embedded. Encoded image saved at:", dwt_encoded_image_path)

    # encodage lsb
    lsb.Lsb(2).insert(original_image_path, message_to_embed,lsb_encoded_image_path)
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

