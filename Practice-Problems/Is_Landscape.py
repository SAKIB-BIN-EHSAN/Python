# Problem-6: Write a function named "isLandscape" that takes 2 numbers(image width and height) as arguments and
# the function returns Landscape if the image width has a higher value than height. Returns Portrait otherwise


def isLandscape(image_width, image_height):
    if (image_width > image_height):
        return "Landscape"
    else:
        return "Portrait"


# print Landscape since width is higher
print(isLandscape(10, 3))

# print Portrait since height is higher
print(isLandscape(20, 30))
