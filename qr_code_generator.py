import qrcode

a = input('enter the URL or the text:').strip()
b = input('enter the file name:').strip()
qr=qrcode.QRCode(box_size=10,border=4)
qr.add_data(a)
image=qr.make_image(fill_color='black',back_color='white')
image.save(b)
print(f'qr code generated as {b}')