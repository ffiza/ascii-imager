<div align="center">
    <h1>ASCII Imager</h1>
</div>

A simple program to convert and image into an ASCII-art version of it. To use,
put the image in the `images/` folder and run

```bash
python ./code/main.py --image images/kitten.jpg --resize_factor 4
```

This code will resize the original image by a factor of `4`, will generate
the ASCII-art version and output the new file as `images/output.png`.

## Example

<p align="center">
    <img src="https://github.com/ffiza/ascii-imager/blob/main/images/kitten.jpg?raw=true" height=400>
    <img src="https://github.com/ffiza/ascii-imager/blob/main/images/output.png?raw=true" height=400>
</p>