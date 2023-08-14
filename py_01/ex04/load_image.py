import PIL
from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """
    This function returns an opened image.
    """
    try:
        if not path:
            raise ValueError("Path cannot be empty")
        image = np.array(Image.open(path))
        # height, width, channels = image.shape
        # print(f"The shape of image is: ({height}, {width}, {channels})")
        return image
    except (PIL.UnidentifiedImageError, FileNotFoundError) as e:
        print("File Error:", e)
        return None
    except ValueError as e:
        print("ValueError:", e)
        return None
