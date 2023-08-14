from load_image import ft_load
from scipy.ndimage import zoom
import matplotlib.pyplot as plt
import numpy as np


def actualzoom(image_array: np.array, zoomfactor: float):
    """
    This function zooming the image and plots it.
    """
    zoom_image = zoom(image_array, (zoomfactor, zoomfactor, 1), order=3)
    fig, ax = plt.subplots()
    ax.imshow(zoom_image)
    plt.show()


def printImage_atributes(image: any, mytext: str):
    """
    This function prints datafrom image
    """
    width, height = image.size
    channels = len(image.getbands())
    print(f"{mytext} ({height}, {width}, {channels})")


def main():
    image_loaded = ft_load("animal.jpeg")
    printImage_atributes(image_loaded, "The shape of image is:")
    print(np.array(image_loaded.getdata()))
    bw_image = image_loaded.convert('L')
    x1, y1, x2, y2 = 450, 100, 850, 500
    # Crop the desired portion
    cropped_image = bw_image.crop((x1, y1, x2, y2))
    resized_image = cropped_image.resize((400, 400))
    printImage_atributes(resized_image, "The new shape after slicing:")
    print(np.array(resized_image.getdata()))
    fig, ax = plt.subplots()
    ax.imshow(resized_image, cmap='gray')
    # Set x and y scales
    ax.set_xticks(list(range(0, 400, 50)))
    ax.set_yticks(list(range(0, 400, 50)))
    ax.set_xticklabels(list(range(0, 400, 50)))
    ax.set_yticklabels(list(range(0, 400, 50)))
    plt.show()


if __name__ == "__main__":
    main()
