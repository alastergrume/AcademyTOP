import pygame as pg
import sys
import math
import random
from config import *
from board import *

pg.init()
pg.display.set_caption('Connect 4')

width = COLUMNS * DISC_SIZE
height = (ROWS + 1) * DISC_SIZE

size = (width, height)
screen = pg.display.set_mode(size)
my_font = pg.font.SysFont("Calibri", 60)