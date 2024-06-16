from configparser import ConfigParser

import pygame


def get_window_dimension(path):
    """TODO: write the docstring for this function."""
    parser = ConfigParser()
    parser.read(path)
    height = int(parser.get("window", "height"))
    width = int(parser.get("window", "width"))
    parser.clear()
    return height, width


def get_conway_params(path):
    """TODO: write the docstring for this function."""
    parser = ConfigParser()
    parser.read(path)
    nbr_rows = int(parser.get("conway", "nbr_rows"))
    nbr_cols = int(parser.get("conway", "nbr_cols"))
    parser.clear()
    return nbr_rows, nbr_cols


def get_text(path, color, key):
    parser = ConfigParser()
    parser.read(path)
    title_text = parser.get("main-menu", key)
    title_size = int(parser.get("main-menu", key + "_size"))
    font = parser.get("assets", "font")
    return pygame.font.Font(font, title_size).render(title_text, True, color)
