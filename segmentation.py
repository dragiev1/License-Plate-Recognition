import numpy as np
from skimage.transform import resize
from skimage import measure
from skimage.measure import regionprops
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import ccaRetouch

def is_valid_region(region_height, region_width, min_width, max_width, min_height, max_height):
    return (
        min_width < region_width < max_width and
        min_height < region_height < max_height
    )

# TODO: Fix hardcoded licenseplate here.
license_plate = np.invert(ccaRetouch.plate_like_objects[2])
# print("Unique values in license_plate: ", np.unique(license_plate))
labeled_plate = measure.label(license_plate)

fig, ax1 = plt.subplots(1)
ax1.imshow(license_plate, cmap="gray")
character_dimensions = (0.35*license_plate.shape[0], 0.6*license_plate.shape[0], 0.05*license_plate.shape[1], 0.15*license_plate.shape[1])
min_height, max_height, min_width, max_width = character_dimensions

characters = []
counter = 0
column_list = []
for regions in regionprops(labeled_plate):
    y0, x0, y1, x1 = regions.bbox
    region_height = y1 - y0
    region_width = x1 - x0

    if is_valid_region(region_height, region_width, min_width, max_width, min_height, max_height):
        print(f"Found character at: ({x0}, {y0}), width: {region_width}, height: {region_height}")

        roi = license_plate[y0:y1, x0:x1]

        # Draw red rectangle over the characters.
        rect_border = patches.Rectangle((x0,y0), x1 - x0, y1 - y0, edgecolor="red", linewidth=2, fill=False)
        ax1.add_patch(rect_border)

        resized_char = resize(roi, (20, 20))
        characters.append(resized_char)

        column_list.append(x0)

plt.show()