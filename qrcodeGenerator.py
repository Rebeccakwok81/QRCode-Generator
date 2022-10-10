import qrcode
#Create a QRCode generator by asking the user input a url
#then converts it to a QRcode and save it as an image.

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version=1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")

url = input("Enter your URL: ")
generate_qrcode(url)
print("Your URL successfully generate! Please check your file")