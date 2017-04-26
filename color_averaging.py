from emoji_json_parsing import rgb_tuple

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

def _calc_avg_pixel_val(intermediate, row, col, sq_length):
    if(row % sq_length != 0):
        print("row not properly aligned")
        return []
    elif(row + sq_length >= len(intermediate)):
        num_edge_pixels = 0
        avg_r_vert = 0
        avg_g_vert = 0
        avg_b_vert = 0
        for i in range(row, len(intermediate)):
            intermediate_pix = intermediate[i][col]
            avg_r_vert += intermediate_pix.r
            avg_g_vert += intermediate_pix.g
            avg_b_vert += intermediate_pix.b
            num_edge_pixels += 1
        return rgb_tuple(r = avg_r_vert // num_edge_pixels, g = avg_g_vert // num_edge_pixels, b = avg_b_vert // num_edge_pixels)
    else:
        avg_r_vert = 0
        avg_g_vert = 0
        avg_b_vert = 0
        for i in range(row, row + sq_length):
            intermediate_pix = intermediate[i][col]
            avg_r_vert += intermediate_pix.r
            avg_g_vert += intermediate_pix.g
            avg_b_vert += intermediate_pix.b
        return rgb_tuple(r=avg_r_vert // sq_length, g=avg_g_vert // sq_length, b=avg_b_vert // sq_length)


def calc_avg_img_values(rgb_image, sq_length):
    if(sq_length > len(rgb_image[0]) or sq_length > len(rgb_image)):
        print("compressed image greater resolution than given image, too high sq length size")
        return rgb_image

    intermediate = []
    for line in rgb_image:
        intermediate.append(_calc_avg_pixel_line_values(line, sq_length))

    avg_img = []
    for row in range(0, len(intermediate), sq_length):
        vert_compressed_pixels = []
        for col in range(len(intermediate[0])):
            vert_compressed_pixels.append(_calc_avg_pixel_val(intermediate, row, col, sq_length))
        avg_img.append(vert_compressed_pixels)
            

    return avg_img



