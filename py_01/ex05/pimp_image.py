from load_image import ft_load
import numpy as np
from PIL import Image


def printImage_atributes(image: np.array, mytext: str):
    """
    This function prints datafrom image
    """
    print(f"{mytext} {image.shape}")
    print(image)


def ft_invert(array) -> np.array:
    """
    inverts color
    """
    return 255 - array


def ft_red(array) -> np.array:
    """
    returns only red chaanal from the rgb array
    """
    temp = array.copy()
    temp[:, :, (1, 2)] = 0
    return temp


def ft_green(array) -> np.array:
    """
    returns only green chaanal from the rgb array
    """
    temp = array.copy()
    temp[:, :, (0, 2)] = 0
    return temp


def ft_blue(array) -> np.array:
    """
    returns only blue chaanal from the rgb array
    """
    temp = array.copy()
    temp[:, :, (0, 1)] = 0
    return temp


def ft_grey(array) -> np.array:
    """
    returns grayscaled image with orgiinal dimension
    """
    temp = np.mean(array, axis=-1, keepdims=True).astype(np.uint8)
    return np.repeat(temp, 3, axis=-1)


def main():
    try:
        image_loaded = ft_load("landscape.jpg")
        printImage_atributes(image_loaded, "The shape of image is:")
        im_R = ft_red(image_loaded)
        im_G = ft_green(image_loaded)
        im_B = ft_blue(image_loaded)
        im_i = ft_invert(image_loaded)
        im_h = ft_grey(image_loaded)
        row_1 = np.concatenate((image_loaded, im_i), axis=1)
        row_2 = np.concatenate((im_R, im_G), axis=1)
        row_3 = np.concatenate((im_B, im_h), axis=1)
        im_RGB = np.concatenate((row_1, row_2, row_3), axis=0)
        pil_img = Image.fromarray(im_RGB)
        pil_img.show()
        print("Inverts the color of the image received.")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
