import qrcode
from PIL import Image

Logo_Link = "csumb.png"  # Use a PNG image for transparency
logo = Image.open(Logo_Link).convert("RGBA") # using the RGBA mode for transparency

basewidth = 100 # earlier it was 198

wpercent = basewidth / float(logo.size[0])
hsize = int(logo.size[1] * float(wpercent))

logo = logo.resize((basewidth, hsize))

# Create the QR code
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
url = "I Love CSUMB"
QRcode.add_data(url)
QRimg = QRcode.make_image(
    fill_color='olive', back_color='white').convert('RGBA')

diff = (QRimg.size[0]-logo.size[0])//2, (QRimg.size[1]-logo.size[1])//2

# Create a new image with a transparent background
new_img = Image.new("RGBA", QRimg.size, (255, 255, 255, 255))

new_img.paste(QRimg, (0, 0))

# Paste the logo onto the new image with transparency
new_img.paste(logo, diff, logo)

new_img.save("mynewQRcode.png")
new_img.show()

