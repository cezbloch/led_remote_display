import PIL
from imaging.scroll_animation import ScrollAnimation
from imaging.text_effect import TextEffect
from maths.containers import Array


class TextEffectParameters(object):
    def __init__(self):
        self.text_color = None
        self.background_color = None
        self.text = None
        self.font = None
        self.display_size = None


class TextEffectFacade(object):
    def __init__(self):
        self.__animation = None
        self.__current_frame = 0
        pass

    def apply(self, parameters):
        self.restart_animation()
        effect = TextEffect(parameters.text_color, parameters.background_color)
        effect.draw_text(parameters.text, parameters.font)
        effect.crop()
        text_image = effect.get_image()
        self.__animation = ScrollAnimation(parameters.display_size, text_image, parameters.background_color)
        width, height = parameters.display_size
        start_point = Array([width, 0])
        text_image_width = text_image.size[0]
        end_point = Array([-text_image_width, 0])
        steps_amount = text_image_width + width
        self.__animation.pre_render(start_point, end_point, steps_amount)

    def get_next_frame(self):
        image = self.__animation[self.__current_frame % len(self.__animation)].transpose(PIL.Image.FLIP_TOP_BOTTOM)
        self.__current_frame += 1

        return image

    def restart_animation(self):
        self.__current_frame = 0
