import cv2
import numpy as np

# Filtering
path = r"D:\103PES__\PES_0404.JPG"
img = cv2.imread(path)
kernel1 = np.array([[-6, -6, -6], [-6, -100, -6], [-6, -6, -6]])
kernel2 = np.array([[0, 3, 6], [-3, 0, 3], [-6, 3, 0]])
out = cv2.filter2D(src=img, ddepth=-1, kernel=kernel2)  # Use 'kernel' instead of 'kernel1'
output_path = r"C:\Users\prabh\Desktop\2dconv.jpg"
cv2.imwrite(output_path, out)
