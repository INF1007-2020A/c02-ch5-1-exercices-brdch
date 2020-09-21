#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	tax_rate = 0.15
	#sous total
	sum = 0
	for item in data:
		sum += item[INDEX_QUANTITY] * item[INDEX_PRICE]
	#calculer taxes
	taxes = tax_rate * sum
	total = sum + taxes
	#retourner la facture formatée
	result = name
	result += "\n" + f"SOUS_TOTAL {sum: >10.2f} $"
	result += "\n" + f"TAXES      {taxes: >10.2f} $"
	result += "\n" + f"TOTAL      {total: >10.2f} $"
	return result
#facon la plus smart
	# bill_data = [
	# 	("SOUS TOTAL", sous_total),
	# 	("TAXES     ", taxes),
	# 	("TOTAL     ", total)
	# ]
	# result = name
	# for d in bill_data:
	# 	result += "\n" + f"{d[0]} {d[1] : >10.2f} $"
	#
	# return result


def format_number(number, num_decimal_digits):
	#separer les parties decimales et entiers donne le reste de la division par 1.0 donc slmt les dec
	decimal_part = abs(number) % 1.0
	whole_part = int(abs(number))
	#formater partie decimale (f laffiche comme un reel
	decimal_str = str(int(round(decimal_part * 10**num_decimal_digits)))
	decimal_str = "." + "0" * (num_decimal_digits - len(decimal_str)) + decimal_str
	# decimal_str = f"{decimal_part:.{num_decimal_digits}f}"[1:] #approche magique

	#formater partie entiere
	whole_part_str = ""
	while whole_part >= 1000:
		digits = whole_part % 1000
		digits_str = f" {digits :0>3}"
		whole_part_str = digits_str + whole_part_str
		whole_part //= 1000
	whole_part_str = str(whole_part) + whole_part_str

	# facon cool dle faire
	#decimal_str = f'{decimal_part :.{num_decimal_digits}f}'[1:]
	# decimal_str = '.' + str(int(round(decimal_part * 10**num_decimal_digits)))
	#concaténer les deux
	return ("-" if number < 0 else "") + whole_part_str + decimal_str


def get_triangle(num_rows):
	border_char = '+'
	triangle_char = 'A'
	# num rows c le nombre de lignes du triangle soit la longueur
	#caucller largeur
	triangle_width = 1 + 2 * (num_rows - 1)

	#construire premiere et derniere ligne (bordures)
	border_row = border_char * (triangle_width + 2)

	#afficher le triangle (pr chaque ligne en part du haut, '+' + ligne de A avec espaces + '+')
	result = border_row
	#pour chaque ligne de triangle
	for i in range(num_rows):
		triangle_chars = triangle_char * (i * 2 + 1)
		result += '\n' + f'{border_char}{triangle_chars : ^{triangle_width}}{border_char}'
	result += '\n' + border_row

	return result




if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
