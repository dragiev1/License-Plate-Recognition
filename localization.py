# Output: two images, one in grayscale and the other in binary.
from skimage.io import imread
from skimage.filters import threshold_otsu
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

car_image = imread("car.jpg", as_gray=True)
# 2 dimensional array
print(car_image.shape)
gray_car_image = car_image * 255
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(gray_car_image, cmap="gray")
threshold_value = threshold_otsu(gray_car_image)
binary_car_image = gray_car_image > threshold_value
ax2.imshow(binary_car_image, cmap="gray")
plt.show()