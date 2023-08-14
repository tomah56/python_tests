from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def printImage_atributes(image: np.array, mytext: str):
    """
    This function prints datafrom image
    """
    print(f"{mytext} {image.shape}")
    print(image)


def plot_image(image: np.array):
    """
    this function plots the image in a specific format
    """
    fig, ax = plt.subplots()
    ax.imshow(image, cmap='gray')
    # Set x and y scales
    ax.set_xticks(list(range(0, 400, 50)))
    ax.set_yticks(list(range(0, 400, 50)))
    ax.set_xticklabels(list(range(0, 400, 50)))
    ax.set_yticklabels(list(range(0, 400, 50)))
    plt.show()


def trim(array, x, y, width, height):
    """
    this function trims an array. giving a starting cordinate x, y a
    nd fromt hat ppoint the with and higth of the desiered now array
    """
    return array[y:y + height, x:x + width]


def transpose_image(image_array: np.array):
    """
    This fuction is swapping the row and culoms in an array
    This will result a transposed image if the array is an image
    """
    transposed_image = np.empty_like(image_array)
    # Loop through width and columns and swap the values
    for row in range(image_array.shape[0]):
        for col in range(image_array.shape[1]):
            transposed_image[col, row] = image_array[row, col]
    return transposed_image


def main():
    try:
        image_loaded = ft_load("animal.jpeg")
        image_trim = trim(image_loaded, 450, 100, 400, 400)
        # dot product is a mathematical muvelet
        # to make a scalar out of a 2 vector
        image_bandwhite = np.dot(image_trim[..., :3],
                                 [0.2989, 0.5870, 0.1140]).astype(int)
        printImage_atributes(image_bandwhite, "The shape of image is:")
        image_trans = transpose_image(image_bandwhite)
        printImage_atributes(image_trans, "New shape after Transpose:")
        plot_image(image_trans)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
