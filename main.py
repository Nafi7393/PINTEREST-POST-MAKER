import textwrap, os, random
from PIL import Image, ImageDraw, ImageFont


class PinMaker:
    def __init__(self, text_line_path, background_path, font_path="impact.ttf", center=True):
        with open(text_line_path, 'r') as file:
            self.lines = file.readlines()

        self.pin_width = 1000
        self.pin_height = 1500
        self.center = center
        self.img = Image.new(mode="RGB", size=(self.pin_width, self.pin_height), color="white")
        self.draw = ImageDraw.Draw(self.img)

        self.text_color = ["#00B6FF", "#FFE800", "#E800FF", "#00FF97", "#FF0068", '#FF5733', '#FFC300', '#33FF57', '#33E0FF', '#A033FF', '#FF33D1']

        self.bg_file_paths = []
        self.bg_path = background_path

        self.font_path = font_path
        self.base_font_size = 40
        self.font_increase_size = 20

        for i, line in enumerate(self.lines):
            self.bg_img = self.get_a_bg()
            self.img.paste(self.bg_img, (0, 0))

            self.line = line.upper()
            self.font, self.f_width = self.set_initial(self.line)
            self.para = textwrap.wrap(self.line, width=self.f_width)
            self.make_pin(name=i, top_pad=120)

    def set_initial(self, line):
        if len(line) <= 35:
            width = 18
            font = ImageFont.truetype(self.font_path, self.base_font_size + self.font_increase_size)
        elif len(line) > 100:
            width = 35
            font = ImageFont.truetype(self.font_path, self.base_font_size)
        else:
            width = 12
            font = ImageFont.truetype(self.font_path, self.base_font_size + self.font_increase_size*6)

        return font, width

    def get_a_bg(self):
        if not self.bg_file_paths:
            for root, directories, files in os.walk(self.bg_path):
                for filename in files:
                    # Getting the absolute path of the file
                    file_path = os.path.join(root, filename)
                    self.bg_file_paths.append(file_path)

        selected_file = random.choice(self.bg_file_paths)
        self.bg_file_paths.remove(selected_file)
        return Image.open(selected_file).resize((self.pin_width, self.pin_height))

    def make_pin(self, name, top_pad, stroke_color="black", stroke_width=8):
        total_text_height = sum(self.draw.textsize(line, font=self.font)[1] for line in self.para)
        y_text = (self.pin_height - total_text_height) // 2 - top_pad  # Center the text vertically

        # Create a new image for the overlay
        overlay = Image.new('RGBA', (self.pin_width, self.pin_height), (0, 0, 0, 76))
        draw = ImageDraw.Draw(overlay)
        draw.rectangle(((0, 0), (self.pin_width, self.pin_height)), fill=(0, 0, 0, 76))

        # Paste the overlay behind the text
        self.img.paste(overlay, (0, 0), overlay)

        ran_para = random.randint(0, len(self.para)-1)
        # Draw the text on top of the overlay
        for k, line in enumerate(self.para):
            text_width, text_height = self.draw.textsize(line, font=self.font)

            if self.center:
                x_text = (self.pin_width - text_width) // 2  # Center the text horizontally
            else:
                x_text = 40

            # Draw the stroke first
            for i in range(-stroke_width, stroke_width + 1):
                for j in range(-stroke_width, stroke_width + 1):
                    if abs(i) + abs(j) <= stroke_width:
                        self.draw.text((x_text + i, y_text + j), line, fill=stroke_color, font=self.font)

            if k == ran_para:
                self.draw.text((x_text, y_text), line, fill=random.choice(self.text_color),
                               font=self.font, outline="black")
            else:
                self.draw.text((x_text, y_text), line, fill="white", font=self.font)
            y_text += text_height  # Increment y position for the next line

        # Save the image
        self.img.save(f"output/post {name + 1}.png", 'PNG')


if __name__ == "__main__":
    PinMaker("lines.txt", "bg")


