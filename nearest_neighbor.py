import sys
from emoji_json_parsing import rgb_tuple

def first_nn(test_rgb_tuple, rgb_to_color_dict): #knn with k = 1
    """
    :param test_rgb_tuple: namedtuple of rgb_tuple denoting rgb
    :param rgb_to_color_dict: dictionary of keys that are rgb_tuple
    :return: a rgb_tuple of the closest color to test_rgb_tuple
    """

    lowest_euclid_dist = sys.maxsize
    nearest_tuple = rgb_tuple(-1,-1,-1)
    for key in rgb_to_color_dict:
        val = _calculate_euclidian_dist(test_rgb_tuple, key)
        if val < lowest_euclid_dist:
            lowest_euclid_dist = val
            nearest_tuple = key
    return nearest_tuple

def _calculate_euclidian_dist(test_rgb_tuple, other_rgb_tuple):
    """
    :param test_rgb_tuple: namedtuple of rgb_tuple denoting rgb
    :param other_rgb_tuple: rgb_tuple to be compared to test_rgb_tuple
    :return: euclidian dist between the 2 tuples based on rgb values
    """
    return (test_rgb_tuple.r - other_rgb_tuple.r)**2 + (test_rgb_tuple.g - other_rgb_tuple.g)**2 + (test_rgb_tuple.b - other_rgb_tuple.b)**2