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
        if (i+1) % sq_length == 0 and i != 0:
            avg_pixel_line.append(rgb_tuple(r = avg_r_horiz // sq_length, g = avg_b_horiz // sq_length, b = avg_b_horiz //sq_length))
            avg_r_horiz = 0
            avg_g_horiz = 0
            avg_b_horiz = 0
    return avg_pixel_line

def calc_avg_img_values(rgb_image, sq_length):
    intermediate = []
    for line in rgb_image:
        intermediate.append(_calc_avg_pixel_line_values(line, sq_length))

    avg_img_value = []
    avg_r_vert = 0
    avg_g_vert = 0
    avg_b_vert = 0

    for col in range(len(intermediate[0])):
        avg_pixel_line = []
        for row in range(len(intermediate)):

            rgb_pixel_intermediate = intermediate[row][col]
            avg_r_vert += rgb_pixel_intermediate.r
            avg_g_vert += rgb_pixel_intermediate.g
            avg_b_vert += rgb_pixel_intermediate.b

            if (row+1) % sq_length == 0 and row != 0:
                avg_pixel_line.append(rgb_tuple(r = avg_r_vert // sq_length, g = avg_g_vert // sq_length, b = avg_b_vert // sq_length))
                avg_r_vert = 0
                avg_g_vert = 0
                avg_b_vert = 0
        avg_img_value.append(avg_pixel_line)

    return avg_img_value



