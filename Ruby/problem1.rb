#  problem1.rb
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
#  the sum of all the multiples of 3 or 5 below 1000.
#

def sum(first, last, n)
	return ((first + last) * n)/2
end

def largest(n, max)
	if max  >= n then
		if max % n == 0 then
			return max
		else
			return largest(n, max-1)
		end
	else
		return n
	end
end

def main()
	n1, n2, n3, max = 3, 5, 15, 999
	l1, l2, l3 = largest(n1, max), largest(n2, max), largest(n3, max) 
	print sum(n1, l1, l1/n1) + sum(n2, l2, l2/n2) - sum(n3, l3, l3/n3), "\n"
end

main()