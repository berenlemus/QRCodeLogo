# QRCodeLogo

## Description
This Python script generates a QR code with a custom logo embedded in the center. The QR code is generated using the `qrcode` library, and the logo is added using the `PIL` (Python Imaging Library) module. The logo is resized and positioned at the center of the QR code image with transparency.

## Features
- Generate QR codes with custom URLs or text.
- Embed a custom logo in the center of the QR code.
- Adjust the size and position of the logo for better visualization.

## Requirements
- Python 3.x
- `qrcode` library (install using `pip install qrcode`)
- `PIL` library (install using `pip install pillow`)

## Usage
1. Prepare a PNG image for the logo. Make sure the image has a transparent background for better integration.
2. Update the `Logo_Link` variable with the path to your logo image file.
3. Optionally, adjust the `basewidth` variable to resize the logo according to your preference.
4. Specify the URL or text you want to encode in the QR code by updating the `url` variable.
5. Run the Python script (`qr_code_generator.py`).
6. A new QR code image with the embedded logo will be generated and saved as `mynewQRcode.png`.
7. You can view the generated QR code image or use it as needed.

## Important Notes
- Ensure that you have a working Python environment with the required libraries installed (`qrcode` and `PIL`).
- The script assumes that the logo image file is in PNG format with a transparent background. Make sure to use PNG images for better results.
- Adjust the `basewidth` variable to resize the logo according to your preferences. Larger logos may affect the visibility of the QR code.
- The QR code is generated based on the specified URL or text. You can customize the content by updating the `url` variable.
- The generated QR code image with the embedded logo will be saved as `mynewQRcode.png` in the current directory.

## Files
- `qr_code_generator.py`: The main Python script.
- `csumb.png`: Sample PNG image used as a logo (replace with your own logo).
- `mynewQRcode.png`: Generated QR code image with the embedded logo.

