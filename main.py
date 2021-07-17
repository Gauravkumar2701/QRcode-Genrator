import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=1

)
name = input("Your Name: ")
email = input("Email ID: ")
website = input("Website Link: ")

data = "Name: " + name + "\nEmail: " + email + "\nWebsite: " + website
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("YourQR")
