from load_image import ft_load
from scipy.ndimage import zoom
import matplotlib.pyplot as plt


def main():
    image_loaded = ft_load("animal.jpeg")
    zoom_image = image_loaded[:400, :400]
    plt.imshow(zoom_image)
    plt.title("Zoomed Image")
    plt.axis("off")  # Turn off axis labels and ticks
    plt.show()


if __name__ == "__main__":
    main()
