import cv2

filename = './Images/test_image.jpg'
W = 600
oriimg = cv2.imread(filename)
height, width, depth = oriimg.shape
imgScale = W/width
newX,newY = oriimg.shape[1]*imgScale, oriimg.shape[0]*imgScale
newimg = cv2.resize(oriimg,(int(newX),int(newY)))
cv2.imshow("Show by CV2",newimg)
cv2.waitKey(0)
cv2.imwrite('./Result/resized.jpg',newimg)