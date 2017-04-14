def get_border():
    """Returns the border.
    
    :return: A tuple of 4 numbers (xmin, ymin, xmax, ymax).
    :rtype: tuple
    """


def get_canvas_height():
    """Returns the canvas height.
    
    :return: The canvas height.
    :rtype: int
    """


def get_canvas_width():
    """Returns the canvas width.
    
    :return: The canvas width.
    :rtype: int
    """


def get_selected_fedge():
    """Returns the selected FEdge.
    
    :return: The selected FEdge.
    :rtype: FEdge
    """


def get_time_stamp():
    """Returns the system time stamp.
    
    :return: The system time stamp.
    :rtype: int
    """


def load_map(file_name, map_name, num_levels=4, sigma=1.0):
    """Loads an image map for further reading.
    
    :param file_name: The name of the image file.
    :type file_name: str
    :param map_name: The name that will be used to access this image.
    :type map_name: str
    :param num_levels: The number of levels in the map pyramid
                                                (default = 4).  If num_levels == 0, the complete pyramid is
                                                built.
    :type num_levels: int
    :param sigma: The sigma value of the gaussian function.
    :type sigma: float
    """


def read_complete_view_map_pixel(level, x, y):
    """Reads a pixel in the complete view map.
    
    :param level: The level of the pyramid in which we wish to read the
                                                pixel.
    :type level: int
    :param x: The x coordinate of the pixel we wish to read.  The origin
                                                is in the lower-left corner.
    :type x: int
    :param y: The y coordinate of the pixel we wish to read.  The origin
                                                is in the lower-left corner.
    :type y: int
    :return: The floating-point value stored for that pixel.
    :rtype: float
    """


def read_directional_view_map_pixel(orientation, level, x, y):
    """Reads a pixel in one of the oriented view map images.
    
    :param orientation: The number telling which orientation we want to
                                                check.
    :type orientation: int
    :param level: The level of the pyramid in which we wish to read the
                                                pixel.
    :type level: int
    :param x: The x coordinate of the pixel we wish to read.  The origin
                                                is in the lower-left corner.
    :type x: int
    :param y: The y coordinate of the pixel we wish to read.  The origin
                                                is in the lower-left corner.
    :type y: int
    :return: The floating-point value stored for that pixel.
    :rtype: float
    """


def read_map_pixel(map_name, level, x, y):
    """Reads a pixel in a user-defined map.
    
    :param map_name: The name of the map.
    :type map_name: str
    :param level: The level of the pyramid in which we wish to read the
                                                pixel.
    :type level: int
    :param x: The x coordinate of the pixel we wish to read.  The origin
                                                is in the lower-left corner.
    :type x: int
    :param y: The y coordinate of the pixel we wish to read.  The origin
                                                is in the lower-left corner.
    :type y: int
    :return: The floating-point value stored for that pixel.
    :rtype: float
    """
