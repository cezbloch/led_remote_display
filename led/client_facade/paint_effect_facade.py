import PIL


class PaintEffectParameters(object):
    def __init__(self):
        self.display_size = None
        self.image = None


class PaintEffectFacade(object):
    def __init__(self):
        self.__image = None

    def apply(self, parameters):
        display_size = parameters.display_size
        image = parameters.image
        self.__image = image.resize(display_size, PIL.Image.ANTIALIAS).convert('RGB')

    def get_image(self):
        return self.__image

