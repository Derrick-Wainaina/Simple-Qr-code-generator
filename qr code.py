import pyqrcode
import png

link = "https://www.w3schools.com/jquery/default.asp"
qr_code = pyqrcode.create(link)
qr_code.png("w3school.png", scale=7)