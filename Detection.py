import cv2
img = cv2.imread("index.jpeg")


yuztanı=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

griton=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
yuzbul=yuztanı.detectMultiScale(griton,1.1,3)

for (x,y,w,h) in yuzbul:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),3)

cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()