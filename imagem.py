import cv2
img = cv2.imread("images.png", cv2.IMREAD_COLOR)
cv2.imshow('images', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
