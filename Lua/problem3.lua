 -- problem3.lua
 -- 
 -- Copyright 2014 Eduardo Sant Anna Martins <eduardomartins993@hotmail.com>
 -- 
 -- This program is free software; you can redistribute it and/or modify
 -- it under the terms of the GNU General Public License as published by
 -- the Free Software Foundation; either version 2 of the License, or
 -- (at your option) any later version.
 --
 -- This program is distributed in the hope that it will be useful,
 -- but WITHOUT ANY WARRANTY; without even the implied warranty of
 -- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 -- GNU General Public License for more details.
 -- 
 -- You should have received a copy of the GNU General Public License
 -- along with this program; if not, write to the Free Software
 -- Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 -- MA 02110-1301, USA.
 -- =======================================================================
 -- Largest prime factor
 -- Problem 3
 -- The prime factors of 13195 are 5, 7, 13 and 29.
 -- What is the largest prime factor of the number 600851475143 ?
 --
 -- for more information: https://projecteuler.net/problem=3


function prime(n, k)
	if k == nil then k = 2 end
	if k <= n/2 then
		if n % k ~= 0 then
			return prime(n, k+1)
		else 
			return false
		end
	else
		return true
	end
end

function main()
	largest, num = 2, 600851475143
	while num > 1 do
		if prime(largest) and num % largest == 0 then
			num = num / largest
		else
			largest = largest + 1
		end
	end
	print(largest)
end

main()