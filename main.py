# -*- coding: utf-8 -*-
import matrix
import character
from character import *

rows , columns = 23, 40


game_matrix = matrix.Matrix(rows, columns)
main_symbol = character.MainSymbol('$')

game_matrix.update_character_in_matrix(main_symbol.x, main_symbol.y, main_symbol.symbol)

while True:
	game_matrix.print_matrix()
	direction = raw_input("where to next (WASD")
	if direction == 'q': break
	elif direction not in (Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST):
		continue

	main_symbol.move(direction)
	game_matrix.update_character_in_matrix(main_symbol.y, main_symbol.x, main_symbol.symbol)
