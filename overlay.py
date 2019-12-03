# encoding: utf-8
"""
Program that converts any 24bit colourful photo into the colours of certain flag,
gives a tinted overlay to an image.
Flags supported at the moment:
Estonia, Russia, Lithuania, Netherlands, Hungary, Austria, Bolivia

:author: Sigrid Närep
"""
import os
import skimage
from skimage import io, data, color, img_as_float, exposure
import matplotlib.pyplot as plt


def slice_img_horizontally(original_image_copy):
    """ Divide image of any size into three equal horizontal slices.

    :param original_image:
    :return:
    """
    top = (slice(0, int(original_image_copy.shape[0]/3)))
    centre = (slice(int(original_image_copy.shape[0]/3),
                    int(original_image_copy.shape[0]/3+original_image_copy.shape[0]/3)))
    bottom = (slice(-int(original_image_copy.shape[0]/3), None))
    return top, centre, bottom


def colorize(original_image, hue, saturation=1.0):
    """ Add color of the given hue to an RGB image.

    By default, set the saturation to 1 so that the colors pop!
    """
    hsv = color.rgb2hsv(original_image)
    hsv[:, :, 1] = saturation
    hsv[:, :, 0] = hue
    return color.hsv2rgb(hsv)


def colorize_estonian_flag(image_copy, top, centre, bottom):
    """
    Method for tinting a picture in the colours of Estonian flag.

    :param image_copy: the whole picture
    :param top: the top side of the picture to be colorized
    :param centre: the centre of the picture to be colorized
    :param bottom: the bottom of the picture to be colorized
    :return:
    """
    image_copy[top] = colorize(image[top], 0.6, saturation=0.4)
    image_copy[centre] = exposure.adjust_gamma(image[centre], 3)
    image_copy[bottom] = colorize(image[bottom], 0, saturation=0)


def colorize_russian_flag(image_copy, top, centre, bottom):
    """
    Method for tinting a picture in the colours of Russian flag.

    :param image_copy: the whole picture
    :param top: the top side of the picture to be colorized
    :param centre: the centre of the picture to be colorized
    :param bottom: the bottom of the picture to be colorized
    :return:
    """
    image_copy[top] = colorize(image[top], 0, saturation=0)
    image_copy[centre] = colorize(image[centre], 0.6, saturation=0.4)
    image_copy[bottom] = colorize(image[bottom], 1, saturation=0.4)


def colorize_holland_flag(image_copy, top, centre, bottom):
    """
    Method for tinting a picture in the colours of Netherlands flag.

    :param image_copy: the whole picture
    :param top: the top side of the picture to be colorized
    :param centre: the centre of the picture to be colorized
    :param bottom: the bottom of the picture to be colorized
    :return:
    """
    image_copy[top] = colorize(image[top], 0.98, saturation=0.4)
    image_copy[centre] = colorize(image[centre], 0, saturation=0)
    image_copy[bottom] = colorize(image[bottom], 0.65, saturation=0.4)


def colorize_hungary_flag(image_copy, top, centre, bottom):
    """
    Method for tinting a picture in the colours of Hungarian flag.

    :param image_copy: the whole picture
    :param top: the top side of the picture to be colorized
    :param centre: the centre of the picture to be colorized
    :param bottom: the bottom of the picture to be colorized
    :return:
    """
    image_copy[top] = colorize(image[top], 0.98, saturation=0.4)
    image_copy[centre] = colorize(image[centre], 0, saturation=0)
    image_copy[bottom] = colorize(image[bottom], 0.4, saturation=0.4)


def colorize_lithuanian_flag(image_copy, top, centre, bottom):
    """
    Method for tinting a picture in the colours of Lithuanian flag.

    :param image_copy: the whole picture
    :param top: the top side of the picture to be colorized
    :param centre: the centre of the picture to be colorized
    :param bottom: the bottom of the picture to be colorized
    :return:
    """
    image_copy[top] = colorize(image[top], 0.12, saturation=0.4)
    image_copy[centre] = colorize(image[centre], 0.4, saturation=0.4)
    image_copy[bottom] = colorize(image[bottom], 0.98, saturation=0.4)


def colorize_austria_flag(image_copy, top, centre, bottom):
    """
    Method for tinting a picture in the colours of Austrian flag.

    :param image_copy: the whole picture
    :param top: the top side of the picture to be colorized
    :param centre: the centre of the picture to be colorized
    :param bottom: the bottom of the picture to be colorized
    :return:
    """
    image_copy[top] = colorize(image[top], 1, saturation=0.4)
    image_copy[centre] = colorize(image[centre], 0, saturation=0)
    image_copy[bottom] = colorize(image[bottom], 1, saturation=0.4)


def colorize_bolivia_flag(image_copy, top, centre, bottom):
    """
    Method for tinting a picture in the colours of Bolivian flag.

    :param image_copy: the whole picture
    :param top: the top side of the picture to be colorized
    :param centre: the centre of the picture to be colorized
    :param bottom: the bottom of the picture to be colorized
    :return:
    """
    image_copy[top] = colorize(image[top], 1, saturation=0.4)
    image_copy[centre] = colorize(image[centre], 0.17, saturation=0.4)
    image_copy[bottom] = colorize(image[bottom], 0.37, saturation=0.4)


if __name__ == "__main__":

    filename = os.path.join(skimage.data_dir, 'smile.jpg')
    smile_photo = io.imread(filename)

    image = img_as_float(smile_photo)
    top_of_img, centre_of_img, bottom_of_img = slice_img_horizontally(image)

    estonian_image = image.copy()
    lithuania_image = image.copy()
    russian_image = image.copy()
    holland_image = image.copy()
    hungary_image = image.copy()
    austria_image = image.copy()
    bolivia_image = image.copy()
    masked_image = image.copy()

    colorize_estonian_flag(estonian_image, top_of_img, centre_of_img, bottom_of_img)
    colorize_lithuanian_flag(lithuania_image, top_of_img, centre_of_img, bottom_of_img)
    colorize_russian_flag(russian_image, top_of_img, centre_of_img, bottom_of_img)
    colorize_holland_flag(holland_image, top_of_img, centre_of_img, bottom_of_img)
    colorize_hungary_flag(hungary_image, top_of_img, centre_of_img, bottom_of_img)
    colorize_austria_flag(austria_image, top_of_img, centre_of_img, bottom_of_img)
    colorize_bolivia_flag(bolivia_image, top_of_img, centre_of_img, bottom_of_img)

    fig, ax = plt.subplots(ncols=2, nrows=4, figsize=(16, 12), sharex=True, sharey=True)

    ax[0, 0].imshow(masked_image)
    ax[0, 0].set_title("Original image")
    ax[0, 1].imshow(estonian_image)
    ax[0, 1].set_title("Estonian filter image")
    ax[1, 0].imshow(lithuania_image)
    ax[1, 0].set_title("Lithuanian filter image")
    ax[1, 1].imshow(russian_image)
    ax[1, 1].set_title("Russian filter image")
    ax[2, 0].imshow(holland_image)
    ax[2, 0].set_title("Netherlands filter image")
    ax[2, 1].imshow(hungary_image)
    ax[2, 1].set_title("Hungary filter image")
    ax[3, 0].imshow(austria_image)
    ax[3, 0].set_title("Austria filter image")
    ax[3, 1].imshow(bolivia_image)
    ax[3, 1].set_title("Bolivia filter image")

    plt.show()
