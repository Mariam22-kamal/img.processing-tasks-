import cv2

# Reading color image as grayscale
gray = cv2.imread("color-img.png",0)

# Showing grayscale image
cv2.imshow("Grayscale Image", gray)

#drawing  a fill in red square 
cv.rectangle(gray,(200,200),(300,300),(255,0,0),-1)

# waiting for key event
cv2.waitKey(0)

# destroying all windows
cv2.destroyAllWindows()
