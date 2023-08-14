import PIL
from PIL import Image


def ft_load(path: str) -> Image:
    """
    This function returns an opened image.
    """
    try:
        if not path:
            raise ValueError("Path cannot be empty")
        return Image.open(path)
    except (PIL.UnidentifiedImageError, FileNotFoundError) as e:
        print("File Error:", e)
        return None
    except ValueError as e:
        print("ValueError:", e)
        return None
