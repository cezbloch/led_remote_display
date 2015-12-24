from imaging.color import Color
from imaging.image_factory import ImageFactory
from maths.interpolation import Math
from images2gif import writeGif
from PIL import Image


class ScrollAnimation(object):
    def __init__(self, animation_size, image, background_color):
        self.__animation_size = animation_size
        self.__image = image
        self.__background_color = background_color
        self.__frames = []

    def __getitem__(self, index):
        return self.__frames[index]

    def __len__(self):
        return len(self.__frames)

    def pre_render(self, start_point, end_point, steps_amount):
        x = Math.generate_range_points(start_point[0], end_point[0], steps_amount)
        y = Math.generate_range_points(start_point[1], end_point[1], steps_amount)

        for frame_id in range(steps_amount):
            # fill frame with background color
            current_frame = ImageFactory.create_rgb_image(self.__animation_size, self.__background_color)
            bounding_box = (int(-x[frame_id]),
                            int(y[frame_id]),
                            int(-x[frame_id]) + self.__animation_size[0],
                            int(y[frame_id]) + self.__animation_size[1])
            # crop the frame even if it's outside the original image
            frame = self.__image.crop(bounding_box)
            # when cropping contains only part of the original image the rest of the frame is black
            # so get the part of the image containing the actual image
            meaningful_pixels_bounding_box = frame.getbbox()
            # if there are any pixels on the cropped area
            if meaningful_pixels_bounding_box is not None:
                # copy this part to separate image
                meaningful_pixels = frame.crop(meaningful_pixels_bounding_box)
                # and paste on the background that was created with the proper background color
                current_frame.paste(meaningful_pixels, meaningful_pixels_bounding_box)

            if current_frame.size != self.__animation_size:
                raise ArithmeticError('problem in bounding box calculation')

            self.__frames.append(current_frame)

    def save(self, filename):
        for index in range(len(self.__frames)):
            self.__frames[index] = self.__frames[index].convert('P', palette=Image.ADAPTIVE, colors=256)
        writeGif(filename, self.__frames, duration=0.2)
