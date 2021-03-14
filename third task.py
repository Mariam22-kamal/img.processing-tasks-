
import cv2
import numpy as np
cap= cv2.VideoCapture(1)
while True:
_, frame= cap.read()
# finds edges in the input image image and  marks them in the output map edges 
edges = cv2.Canny(frame,100,200)  
# Display edges in a frame 
cv2.imshow('Edges',edges) 
# Wait for Esc key to stop 
k = cv2.waitKey(5) & 0xFF
  if k == 27: 
      break 
