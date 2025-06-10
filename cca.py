from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import localization

# Gets all the connected regions and groups them together.
label_image = measure.label(localization.binary_car_image)
fig, (ax1) = plt.subplots(1)
ax1.imshow(localization.gray_car_image, cmap="gray")

# regionprops creates a list of properties of all the labelled regions.
for region in regionprops(label_image):
    if region.area < 50:
        continue
    minRow, minCol, maxRow, maxCol = region.bbox
    rectBorder = patches.Rectangle((minCol, minRow), maxCol-minCol, maxRow-minRow, edgecolor="blue", linewidth=2, fill=False)
    ax1.add_patch(rectBorder)  # Draws a blue rectangle over this region.

plt.show()
