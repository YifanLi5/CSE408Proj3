from color_json_handling import rgb_tuple

def _calc_avg_pixel_line_values(rgb_line, sq_length):
    avg_pixel_line = []
    avg_r_horiz = 0
    avg_g_horiz = 0
    avg_b_horiz = 0
    for i, pixel in enumerate(rgb_line):
        avg_r_horiz += pixel.r
        avg_g_horiz += pixel.g
        avg_b_horiz += pixel.b
        if i % sq_length == 0 and i != 0:
            avg_pixel_line.append(rgb_tuple(r = avg_r_horiz, g = avg_b_horiz, b = avg_b_horiz))
    return avg_pixel_line

def calc_avg_img_values(rgb_image, sq_length):
    avg_image = []
    avg_r_vert = 0
    avg_g_vert = 0
    avg_b_vert = 0
    for i, line in enumerate(rgb_image):
        avg_pixel_line = _calc_avg_pixel_line_values(line, sq_length)
        avg_r_vert
        if i % sq_length == 0 and i != 0:

        avg_image.append()
    return avg_image



