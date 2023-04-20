# Демкин Алексей 368096
import cv2

img = cv2.imread('6.jpeg')  # загрузка изображения
cv2.imshow('image', img)
height, width = img.shape[:2]  # получение размеров изображения
resimg = cv2.resize(img, (int(width * 2), int(height * 2)))  # увеличение размера изображения в два раза
cv2.imshow('resizedimage', resimg)

cv2.waitKey(0)
cv2.destroyAllWindows()
