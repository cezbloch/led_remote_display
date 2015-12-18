from maths.interpolation import Math
from images2gif import writeGif
from PIL import Image


class ScrollAnimation(object):
    def __init__(self, animation_size, image):
        self.__animation_size = animation_size
        self.__image = image
        self.__frames = []

    def __getitem__(self, index):
        return self.__frames[index]

    def __len__(self):
        return len(self.__frames)

    def pre_render(self, start_point, end_point, steps_amount):
        x = Math.generate_range_points(start_point[0], end_point[0], steps_amount)
        y = Math.generate_range_points(start_point[1], end_point[1], steps_amount)

        for frame_id in range(steps_amount):
            bounding_box = (int(-x[frame_id]),
                            int(y[frame_id]),
                            int(-x[frame_id]) + self.__animation_size[0],
                            int(y[frame_id]) + self.__animation_size[1])
            frame = self.__image.crop(bounding_box)

            if frame.size != self.__animation_size:
                raise ArithmeticError('problem in bounding box calculation')

            self.__frames.append(frame)

    def save(self, filename):
        image = self.__frames[0]
        self.__frames[0] = image.convert('P', palette=Image.ADAPTIVE, colors=256)
        writeGif(filename, self.__frames, duration=0.05)
