import cv2
import rpyc
from PIL import Image

def Resim(img):

    print(img)


conn=rpyc.classic.connect("localhost")



img = Image.open('index.jpeg')
img.show()
In=conn.teleport(Resim)
In(img)
cv2.waitKey(1)
cv2.destroyAllWindows()



