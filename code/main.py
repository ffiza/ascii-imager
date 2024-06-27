import numpy as np
import argparse
from PIL import Image, ImageDraw, ImageFont


class Imager():
    CHARS = "Ñ@#W$9876543210?!abc;:+=-,._ "
    MAX_PIXEL_VALUE = 255
    CHAR_WIDTH = 20
    CHAR_HEIGHT = 20

    def __init__(self, img_path: str, resize_factor: int):
        self._img_path = img_path
        self._resize_factor = resize_factor
        self._input_image = None
        self._input_image_shape = None
        self._brightness = None
        self._char_mat = None
        self._font = ImageFont.truetype("fonts/RobotoMono-Regular.ttf", 15)
        self._output_image = None
        self._output_image_shape = None

    def _load_image(self) -> None:
        img = Image.open(self._img_path)
        self._input_image_shape = np.array(img).shape
        self._input_image = np.array(
            img.resize(
                (self._input_image_shape[0] // self._resize_factor,
                 self._input_image_shape[1] // self._resize_factor)))
        self._output_image_shape = self._input_image.shape

    def _get_brightness(self) -> None:
        self._brightness = np.mean(self._input_image, axis=2)

    def _make_char_mat(self) -> None:
        normalized_brightness = (self._brightness / Imager.MAX_PIXEL_VALUE
                                 * len(Imager.CHARS)).astype(np.int16)
        self._char_mat = np.array(list(Imager.CHARS[::-1]))[
            normalized_brightness]

    def _make_output_image(self) -> None:
        img_width = self._output_image_shape[0] * Imager.CHAR_WIDTH
        img_height = self._output_image_shape[1] * Imager.CHAR_HEIGHT
        img = Image.new('RGB', (img_width, img_height), color='white')
        draw = ImageDraw.Draw(img)
        for i in range(self._output_image_shape[0]):
            for j in range(self._output_image_shape[1]):
                draw.text((j * Imager.CHAR_WIDTH, i * Imager.CHAR_HEIGHT),
                          self._char_mat[i, j], 'black', self._font)
        self._output_image = img

    def _save_output_image(self) -> None:
        self._output_image.save("output.png")

    def run(self) -> None:
        self._load_image()
        self._get_brightness()
        self._make_char_mat()
        self._make_output_image()
        self._save_output_image()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--image", type=str, required=True,
        help="The name of the image.")
    parser.add_argument(
        "--resize_factor", type=int, required=True,
        help="The factor to resize the input image.")
    args = parser.parse_args()

    imager = Imager(args.image, args.resize_factor)
    imager.run()
