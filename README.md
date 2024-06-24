# Pinterest Post Maker

This Python script generates Pinterest-style post images by overlaying text on background images. It utilizes threading for concurrent image generation and supports customization of text styling.

## Requirements

- Python 3.x
- PIL (Python Imaging Library)
- `impact.ttf` font file (or specify your own font)
- Background images in the `background_images` folder
- Input text lines in a CSV file (`pin_text.csv`)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Nafi7393/PINTEREST-POST-MAKER.git
   cd PINTEREST-POST-MAKER
   ```

2. Install dependencies:
   ```
   pip install pillow
   ```

3. Place your background images in the `background_images` folder.

## Usage

Modify `pin_text.csv` with your desired text lines. Then run the script to generate Pinterest-style images:

```
python main.py
```

Adjust parameters in `main.py` such as `max_limit` in `fire_pins` function for batch image generation.

## Example Images

|                                 |                                  |                                  |
|---------------------------------|----------------------------------|----------------------------------|
| ![Example 1](output/post_2.png) | ![Example 2](output/post_3.png)  | ![Example 2](output/post_13.png) |
| ![Example 1](output/post_9.png) | ![Example 1](output/post_10.png) | ![Example 1](output/post_8.png)  |

## Customization

- **Text Styling**: Modify `text_color`, `font_path`, `base_font_size`, and `font_increase_size` in `PinMaker` class for different text effects.
- **Backgrounds**: Add or change background images in `background_images` folder to create diverse post styles.

## Notes

- Ensure the CSV file (`pin_text.csv`) is correctly formatted with each line of text in the first column.
- The script uses threading for concurrent image processing, ensuring efficient batch image creation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
