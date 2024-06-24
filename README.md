# Pinterest Post Maker

This Python script generates Pinterest-style post images using background images and text from a CSV file. Each generated post combines artistic backgrounds with overlaid text, suitable for social media sharing.

## Examples

### Top Row

![Post 1](output/post_1.png) ![Post 2](output/post_2.png) ![Post 3](output/post_3.png)

- **Description**: Examples showcasing three posts side by side.
- **Details**: Each post combines a different background image with overlaid text. The text color and placement vary to create visually appealing posts.

### Bottom Row

![Post 4](output/post_4.png) ![Post 5](output/post_5.png)

- **Description**: More examples demonstrating the versatility of the script.
- **Details**: These posts utilize different fonts, text alignments, and background images to showcase various design possibilities.

## Usage

To use the script and generate your own Pinterest-style posts:

1. **Clone the Repository**:
   ```
   git clone https://github.com/Nafi7393/PINTEREST-POST-MAKER.git
   cd PINTEREST-POST-MAKER
   ```

2. **Prepare Your Data**:
   - Place your background images in the `background_images` folder.
   - Create a CSV file (`pin_text.csv`) with each line containing the text for one post.

3. **Run the Script**:
   - Adjust parameters in the `if __name__ == "__main__":` block of `main.py` as needed (e.g., file paths, output folder, max limit).
   - Execute the script:
     ```
     python main.py
     ```

4. **Output**:
   - Generated images will be saved in the `output` folder.

## Requirements

- Python 3.x
- PIL (Python Imaging Library)

Ensure you have the required libraries installed. You can install them using pip:
```
pip install pillow
```

## Notes

- The script uses multithreading to speed up image generation. Adjust `max_limit` in `fire_pins` function if needed.
- Customize the font, text colors, and other parameters in `PinMaker` class as per your preferences.

## License

This project is licensed under the [MIT License](LICENSE).
