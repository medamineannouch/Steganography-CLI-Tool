
# Steganography CLI Tool

The Steganography CLI Tool is a command-line application designed for image encoding and decoding using two popular steganography methods: Discrete Wavelet Transform (DWT) and Least Significant Bit (LSB). 


## Features

- Image Encoding and Decoding: Encode messages into images and decode hidden messages from encoded images using either DWT or LSB methods via the command line.

- Evaluation: Evaluate the effectiveness of encoding methods by comparing original and encoded images based on Mean Squared Error (MSE) and Peak Signal-to-Noise Ratio (PSNR).

- Plots: Generate histograms and color panel plots via the command line to visually assess the impact of encoding on image properties.


## Usage

- Encode Message:

    - Provide the path of the image file for encoding.
    - Choose the steganography method (DWT or LSB).
    - Enter the message to be encoded.
    - Execute the command for encoding.
- Decode Message:

    - Provide the path of the encoded image file.
    - Choose the steganography method used for encoding.
    - Execute the command for decoding.

- Evaluate:

    - Provide paths for the original and encoded images.
    - Execute the command for evaluation to generate comparison results.
- Plot:

    - Provide paths for the original, DWT-encoded, and LSB-encoded images.
    - Execute the command for plotting to generate visual representations.


## Getting Started

Clone the repository:

```bash
  git clone https://github.com/medamineannouch/steganography-cli-tool.git
```
Install dependencies:

```bash
  pip install -r requirements.txt

```
Run the application:

```bash
  python main.py


```
    
## Acknowledgements

 - [OpenCV ](https://opencv.org/) - Open Source Computer Vision Library
 - [scikit-image ](https://scikit-image.org/) - Image processing in Python
 
