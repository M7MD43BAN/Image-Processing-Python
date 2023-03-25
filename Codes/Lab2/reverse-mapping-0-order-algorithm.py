import cv2
import numpy as np


###############################################################################################
# Create a function for Resizing Reverse Mapping: 0-Order algorithm
# First parameter: Input image that will be resized
# Second parameter: resizing factor along the horizontal axis
# Third parameter: resizing factor along the vertical axis
def reverse_mapping_0Order(image, row_factor, column_factor):
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
    # Then for each pixel in the image using i and j
    for k in range(channel):
        for i in range(new_row):
            old_x = int(i * row_ratio)
            for j in range(new_column):
                old_y = int(j * column_ratio)
                new_image[i, j, k] = image[old_x, old_y, k]

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
img = cv2.imread("/home/m7md43ban/Image Processing with Python/Codes/images/Powerpuff Girls.jpeg")
reverse_mapping_0Order(img, 2, 3)
