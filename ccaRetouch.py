from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import localization

def is_valid_license_plate(region_height, region_width, min_height, max_height, min_width, max_width):
    return (
        min_height <= region_height <= max_height and
        min_width <= region_width <= max_width and
        region_width > region_height
    )

label_image = measure.label(localization.binary_car_image)

# Initialize a maximum and minimum size the license plate can be in a typical image.
# Usually around 8-20% for height and 14-40% for width. 
plate_dimensions = (0.08*label_image.shape[0], 0.2*label_image.shape[0], 0.14*label_image.shape[1], 0.4*label_image.shape[1])
min_height, max_height, min_width, max_width = plate_dimensions
plate_objects_coordinates = []
plate_like_objects = []
fig, (ax1) = plt.subplots(1)
ax1.imshow(localization.gray_car_image, cmap="gray")

for region in regionprops(label_image):
    if(region.area < 50): continue
    min_row, min_col, max_row, max_col = region.bbox
    region_height = max_row - min_row
    region_width = max_col - min_col

    # Check if the current region matches the dimensions we are looking for.
    if is_valid_license_plate(region_height, region_width, min_height, max_height, min_width, max_width):
        plate_like_objects.append(localization.binary_car_image[min_row:max_row, min_col:max_col])
        rectBorder = patches.Rectangle((min_col, min_row), max_col-min_col, max_row-min_row, edgecolor="red", linewidth=2, fill=False)
        ax1.add_patch(rectBorder)  # Draw red rectangle over potential license plate.

plt.show()