import cv2
import numpy as np


###############################################################################################
# Create a function for Resizing Reverse Mapping: 1-Order algorithm
# First parameter: Input image that will be resized
# Second parameter: resizing factor along the horizontal axis
# Third parameter: resizing factor along the vertical axis
def reverse_mapping_1Order(image, row_factor, column_factor):
    # Seeing the shape width (row) and height (column) and channels
    # of the image using shape attribute.
    [row, column, channel] = image.shape

    # calculate the new dimensions of the resized image using `factor`.
    new_row = int(row * row_factor)
    new_column = int(column * column_factor)

    # calculate the ratio to access the pixels in old image.
    row_ratio = row / new_row
    column_ratio = column / new_column

    # Creating a new matrix of zeros with the new dimensions of the resized image.
    # We use the zeros function of NumPy to create this new matrix.
    # We also specify the data type of the matrix as unsigned 8-bit integers using the dtype argument.
    new_image = np.zeros([new_row, new_column, channel], dtype=np.uint8)

    # We iterate over each channel of the image using k
    # Then for each pixel in the image using new_x and new_y
    for k in range(channel):
        for new_x in range(new_row):
            old_x = new_x * row_ratio
            x1 = int(old_x)
            x_fraction = abs(old_x - x1)

            for new_y in range(new_column):
                old_y = new_y * column_ratio
                y1 = int(old_y)
                p1 = image[x1, y1, k]
                p2 = image[x1, y1, k]

                y_fraction = abs(old_y - y1)
                z1 = p1 * (1 - x_fraction) + p2 * x_fraction

                new_pixel = z1 * (1 - y_fraction) + z1 * y_fraction
                new_image[new_x, new_y, k] = int(new_pixel)

    # Displaying the original and resized images using the imshow function of OpenCV
    cv2.imshow('Original Image', image)
    print(image.shape)
    cv2.imshow('Resized', new_image)
    print(new_image.shape)

    # hold the screen until user close it.
    cv2.waitKey(0)

    # Deleting created GUI window from screen and memory
    cv2.destroyAllWindows()


###############################################################################################

# imread(): this method loads an image from the specified file
img = cv2.imread("/home/m7md43ban/Image Processing with Python/Codes/images/3bears.jpeg")
reverse_mapping_1Order(img, 1, 3)
