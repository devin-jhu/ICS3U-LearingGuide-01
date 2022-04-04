#!/usr/bin/env python3

# Created by Devin Jhu
# Created on February 2022
# The space aliens game

import stage
import ugame


def game_scene():
# image banks for CircuitPython
image bank background = stage.Bank. from bmp16("space aliens_background.bmp")

# set the background to image 0 in the image bank

# and the size (10x8 tiles of size 16x16)
background = stage.Grid(image_bank_background, 10, 8)

# create a stage for the background to show up on

#and set the frame rate to 60fps
game = stage.Stage(ugame.display, 60)
# set the Layers of all sprites,
items show up in order
game.layers = [background]
# render all sprites
# most Likely you will only render the background once per game scene
game.render_block()
if __name__ == "__main__":
    game_scene()
