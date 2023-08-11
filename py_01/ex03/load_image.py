import array
import PIL
from PIL import Image
import numpy as np


def ft_load(path: str) -> array:
    """
    This function returns an array from picture.
"""
    try:
        if not path:
            raise ValueError("Path cannot be empty")
        image = Image.open(path)
        width, height = image.size
        channels = len(image.getbands())
        pixels = np.array(image.getdata())
        print(f"The shape of image is: ({height}, {width}, {channels})")
        # image.show()
        # zoom_image = image[:400, :400, :]
        # zoom_image.show()
    except (PIL.UnidentifiedImageError, FileNotFoundError) as e:
        print("File Error:", e)
        return []
    except ValueError as e:
        print("ValueError:", e)
        return []
    return pixels
