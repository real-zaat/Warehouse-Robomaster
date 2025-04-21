import time
import robomaster
from robomaster import conn
from MyQR import myqr
from PIL import Image

# use this code to connect all robot(s) to a router

QRCODE_NAME = "qrcode.png"

if __name__ == '__main__':

    helper = conn.ConnectionHelper()
    info = helper.build_qrcode_string(ssid="INSERT NETWORK NAME HERE", password="INSERT PASSWORD HERE")
    myqr.run(words=info)
    time.sleep(1)
    img = Image.open(QRCODE_NAME)
    img.show()
    if helper.wait_for_connection():
        print("Connected!")
    else:
        print("Connect failed!")