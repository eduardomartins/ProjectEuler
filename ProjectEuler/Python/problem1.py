#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem1.py
#  
#  Copyright 2014 Eduardo Sant' Anna Martins <eduardomartins1993@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# ========================================================================  
#
#  Name: Multiples of 3 and 5
#  Problem: 1
#  Exercise: If we list all the natural numbers below 10 that are multiples 
#  of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.Find 
#  the sum of all the multiples of 3 or 5 below 1000
#

def maiorMultiplo(num, maximo):
	if(maximo >= num):
		if(maximo % num == 0):
			return maximo
		else:
			return maiorMultiplo(num, maximo - 1)
	else:
		return 0

def somaNumeriaca(a1, an, n):
	return ((a1 + an) * n)/2

def main():
	maximo = 1000000000
	maior3 = maiorMultiplo(3, maximo)
	maior5 = maiorMultiplo(5, maximo)
	maior15 = maiorMultiplo(15, maximo)
	
	print somaNumeriaca(3, maior3, maior3/3) + somaNumeriaca(5, maior5, maior5/5) - somaNumeriaca(15, maior15, maior15/15)
	
	return 0

if __name__ == '__main__':
	main()
	