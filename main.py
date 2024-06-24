import textwrap
import os
import random
import threading
from PIL import Image, ImageDraw, ImageFont
import warnings
import csv

warnings.filterwarnings("ignore", category=DeprecationWarning)


class PinMaker:
    def __init__(self, text_lines, background_folder, output_folder="output", font_path="impact.ttf", center=True):
        self.lines = text_lines
        self.bg_folder = background_folder
        self.output_folder = output_folder
        self.font_path = font_path
        self.center = center

        self.pin_width = 1000
        self.pin_height = 1500
        self.base_font_size = 40
        self.font_increase_size = 20
        self.text_color = ["#00B6FF", "#FFE800", "#E800FF", "#00FF97", "#FF0068", '#FF5733', '#FFC300', '#33FF57', '#33E0FF', '#A033FF', '#FF33D1']

        self.img = Image.new(mode="RGB", size=(self.pin_width, self.pin_height), color="white")
        self.draw = ImageDraw.Draw(self.img)

        self.bg_file_paths = []
        self.load_backgrounds()

    def load_backgrounds(self):
        for root, directories, files in os.walk(self.bg_folder):
            for filename in files:
                file_path = os.path.join(root, filename)
                self.bg_file_paths.append(file_path)

    def get_a_background(self):
        if not self.bg_file_paths:
            raise ValueError("No background images found. Please check the folder path.")

        selected_file = random.choice(self.bg_file_paths)
        self.bg_file_paths.remove(selected_file)
        return Image.open(selected_file).resize((self.pin_width, self.pin_height))

    def set_initial_parameters(self, line):
        if len(line) <= 35:
            width = 18
            font_size = self.base_font_size + self.font_increase_size
        elif len(line) > 100:
            width = 35
            font_size = self.base_font_size
        else:
            width = 12
            font_size = self.base_font_size + self.font_increase_size * 6

        font = ImageFont.truetype(self.font_path, font_size)
        return font, width

    def make_pin(self, name, top_pad=120, stroke_color="black", stroke_width=8):
        bg_img = self.get_a_background()
        self.img.paste(bg_img, (0, 0))

        line = self.lines[0].upper()
        font, f_width = self.set_initial_parameters(line)
        para = textwrap.wrap(line, width=f_width)

        total_text_height = sum(self.draw.textsize(line, font=font)[1] for line in para)
        y_text = (self.pin_height - total_text_height) // 2 - top_pad

        overlay = Image.new('RGBA', (self.pin_width, self.pin_height), (0, 0, 0, 76))
        draw = ImageDraw.Draw(overlay)
        draw.rectangle(((0, 0), (self.pin_width, self.pin_height)), fill=(0, 0, 0, 76))
        self.img.paste(overlay, (0, 0), overlay)

        ran_para = random.randint(0, len(para) - 1)
        for k, line in enumerate(para):
            text_width, text_height = self.draw.textsize(line, font=font)

            if self.center:
                x_text = (self.pin_width - text_width) // 2
            else:
                x_text = 40

            for i in range(-stroke_width, stroke_width + 1):
                for j in range(-stroke_width, stroke_width + 1):
                    if abs(i) + abs(j) <= stroke_width:
                        self.draw.text((x_text + i, y_text + j), line, fill=stroke_color, font=font)

            if k == ran_para:
                self.draw.text((x_text, y_text), line, fill=random.choice(self.text_color), font=font, outline="black")
            else:
                self.draw.text((x_text, y_text), line, fill="white", font=font)
            y_text += text_height

        self.img.save(f"{self.output_folder}/post_{name}.png", 'PNG')


def fire_pins(csv_file_path, bg_folder="background_images", output_folder="output", max_limit=10):
    limit = 0
    all_tasks = []

    lines_list = read_lines_from_csv(csv_file_path)
    num_pins = 1
    for line in lines_list:
        limit += 1
        pin_maker = PinMaker(text_lines=[line], background_folder=bg_folder, output_folder=output_folder)
        thread = threading.Thread(target=pin_maker.make_pin, kwargs={'name': num_pins, 'top_pad': 120})
        thread.start()
        all_tasks.append(thread)
        num_pins += 1

        if limit == max_limit:
            for task in all_tasks:
                task.join()
            all_tasks = []
            limit = 0

    for task in all_tasks:
        task.join()


def read_lines_from_csv(csv_file_path):
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
        readings = csv.reader(csv_file)
        market_lines = [row[0] for row in readings]  # Assuming the lines are in the first column (A)
    return market_lines


if __name__ == "__main__":
    fire_pins(csv_file_path="pin_text.csv", bg_folder="background_images",
              output_folder="output", max_limit=10)
