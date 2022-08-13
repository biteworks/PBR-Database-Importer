import math


class Helpers:
    # Based on https://gist.github.com/Kodagrux/5b39358d812c0fd8eaf4
    def reMap(self, inputVal):
        oldMin, oldMax = 0, 255
        newMin, newMax = 0.0, 1.0

        inputVal = oldMax if inputVal > oldMax else inputVal
        inputVal = oldMin if inputVal < oldMin else inputVal

        inputSpan = oldMax - oldMin
        outputSpan = newMax - newMin

        scaledThrust = float(inputVal - oldMin) / float(inputSpan)

        return newMin + (scaledThrust * outputSpan)

    # Based on http://www.tannerhelland.com/4435/convert-temperature-rgb-algorithm-code/
    # and https://gist.github.com/petrklus/b1f427accdf7438606a6
    def kelvinToRGB(self, kelvin):
        # range check
        if kelvin < 1000:
            kelvin = 1000
        elif kelvin > 40000:
            kelvin = 40000

        tmp_internal = kelvin / 100.0

        # red
        if tmp_internal <= 66:
            red = 255
        else:
            tmp_red = 329.698727446 * \
                math.pow(tmp_internal - 60, -0.1332047592)
            if tmp_red < 0:
                red = 0
            elif tmp_red > 255:
                red = 255
            else:
                red = tmp_red

        # green
        if tmp_internal <= 66:
            tmp_green = 99.4708025861 * math.log(tmp_internal) - 161.1195681661
            if tmp_green < 0:
                green = 0
            elif tmp_green > 255:
                green = 255
            else:
                green = tmp_green
        else:
            tmp_green = 288.1221695283 * \
                math.pow(tmp_internal - 60, -0.0755148492)
            if tmp_green < 0:
                green = 0
            elif tmp_green > 255:
                green = 255
            else:
                green = tmp_green

        # blue
        if tmp_internal >= 66:
            blue = 255
        elif tmp_internal <= 19:
            blue = 0
        else:
            tmp_blue = 138.5177312231 * \
                math.log(tmp_internal - 10) - 305.0447927307
            if tmp_blue < 0:
                blue = 0
            elif tmp_blue > 255:
                blue = 255
            else:
                blue = tmp_blue

        rgb = (self.reMap(red), self.reMap(green), self.reMap(blue))
        return rgb

    # formula from comments under https://www.youtube.com/watch?v=ipqyVWm5JmY
    def lumesToPower(self, lumens, rgb):
        return lumens / \
            (683 * (0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]))
