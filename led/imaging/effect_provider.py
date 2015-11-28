class EffectProvider(object):
    def __init__(self):
        self._current_effect = None
        self._image = None
        self._apply_effect_callback = None

    def set_effect(self, effect):
        self._current_effect = effect

    def set_image(self, image):
        self._image = image

    def get_image(self):
        return self._image

    def set_apply_effect_callback(self, callback):
        self._apply_effect_callback = callback

    def apply_image(self):
        if self._apply_effect_callback is not None:
            self._apply_effect_callback()
