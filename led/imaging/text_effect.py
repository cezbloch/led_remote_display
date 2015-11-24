from PIL import Image, ImageDraw, ImageFont


class TextEffect(object):
    def __init__(self, display):
        self.display = display
        self.font_size, _ = display
        self.super_sample_factor = 1
        self.text_position = (0.0, 0.0)
        self.background_color = (0, 0, 0, 0)
        self.text_color = (255, 0, 0, 100)

    def draw_text(self, text):
        scale_factor = self.super_sample_factor
        image = self.draw_text_super_sampled(text, scale_factor)
        original_size = [x / scale_factor for x in image.size]
        resized_image = image.resize(original_size, Image.NEAREST)
        #resized_image.save('test.png', 'PNG')
        return image

    def draw_text_super_sampled(self, text, scale_factor):
        k_size = self.font.getsize("k")
        j_size = self.font.getsize("j")
        offset = k_size[1] - j_size[1]
        scaled_offset = offset * scale_factor
        text_size = self.font.getsize(text)
        scaled_text_size = [x * scale_factor for x in text_size]
        scaled_text_size[1] = scaled_text_size[1] + scaled_offset
        image = Image.new("RGB", scaled_text_size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        font_size = self.font.size * scale_factor
        font = ImageFont.truetype(self.font.path, font_size)
        draw.text((0, scaled_offset), text, self.text_color, font=font)
        return image

    def set_font_size(self, font_size):
        self.font_size = font_size

    def with_font(self, font):
        self.font = font
        return self


