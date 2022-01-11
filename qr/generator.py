import qrcode
import csv

# Define event name
event = "Super Summit 2022"
# Read attendees file
filename = open('qrlist.csv', 'r')
file = csv.DictReader(filename)

# QRCode generator function 
def qrGenerator(data):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=15, border=1,)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#000", back_color="#fff")
    return img

# Loop through the attendees, generate the qr & save the image 
for row in file:
    data = f'''
        {event.upper()}
        {'─' * 18}
        ID: {row['ID']}
        NAME: {row['NAME'] + " " + row['SURNAME']}
        EMAIL: {row['EMAIL']}
    '''
    print(data)
    img = qrGenerator(data)
    img.save(f"{row['ID']}.png")