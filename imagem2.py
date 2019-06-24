import cv2

img = cv2.imread("images.png", cv2.IMREAD_COLOR)

stylization = cv2.stylization(img)

cv2.imshow('images2', stylization)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("images_result.png", stylization)

 
