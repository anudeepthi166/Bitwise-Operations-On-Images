import cv2
import numpy as np
from matplotlib import pyplot as plt

# draw a rectangle
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
plt.imshow(rectangle)


# draw a circle
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
plt.imshow(circle)

#Read the images
p1=cv2.imread('square.jpg')
p2=cv2.imread('circle.jpg')

#BITWISE AND
b_and=cv2.bitwise_and(p1,p2)
plt.imshow(b_and)
cv2.imwrite("b_and.jpg",b_and)

#BITWISE OR
b_or=cv2.bitwise_or(p1,p2)
plt.imshow(b_or)
cv2.imwrite("b_or.jpg",b_or)

#BITWISE XOR
b_xor=cv2.bitwise_xor(p1,p2)
plt.imshow(b_xor)
cv2.imwrite("b_xor.jpg",b_xor)

#BITWISE NOT
b_not=cv2.bitwise_not(p1)
plt.imshow(b_not)
cv2.imwrite("b_not.jpg",b_not)
