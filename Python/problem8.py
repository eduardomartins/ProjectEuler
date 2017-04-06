#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem8.py
#
#  Copyright 2017 Eduardo Sant'Anna Martins <eduardo@eduardomartins.site>
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
#  ==========================================================
#  Largest product in a series
#
#   The four adjacent digits in the 1000-digit number that have the greatest product
#    are 9 × 9 × 8 × 9 = 5832.
#
#               73167176531330624919225119674426574742355349194934
#               96983520312774506326239578318016984801869478851843
#               85861560789112949495459501737958331952853208805511
#               12540698747158523863050715693290963295227443043557
#               66896648950445244523161731856403098711121722383113
#               62229893423380308135336276614282806444486645238749
#               30358907296290491560440772390713810515859307960866
#               70172427121883998797908792274921901699720888093776
#               65727333001053367881220235421809751254540594752243
#               52584907711670556013604839586446706324415722155397
#               53697817977846174064955149290862569321978468622482
#               83972241375657056057490261407972968652414535100474
#               82166370484403199890008895243450658541227588666881
#               16427171479924442928230863465674813919123162824586
#               17866458359124566529476545682848912883142607690042
#               24219022671055626321111109370544217506941658960408
#               07198403850962455444362981230987879927244284909188
#               84580156166097919133875499200524063689912560717606
#               05886116467109405077541002256983155200055935729725
#               71636269561882670428252483600823257530420752963450
#
#  Find the thirteen adjacent digits in the 1000-digit number that have the greatest
#   product. What is the value of this product?
DIGITS = '\
73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'

import numpy

def media_ponderada(list_n):
    m = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
    }

    for num in list_n:
        m[num] += 1

    r = 0.0
    for num, qtd in m.items():
        r += num * qtd

    return r/sum(m.values())


def mul(list_n):
    m = 1
    for l in list_n:
        m *= l
    return m


def problem():
    splited = []
    total = len(DIGITS)
    init = 0
    final = 13

    while(final <= total):
        slices = DIGITS[init:final]
        if '0' not in slices:
            splited.append("".join(sorted(slices, reverse=True)))
        init += 1
        final += 1

    splited.sort()
    #print splited
    result = []
    for greatest in splited:
        #greatest = splited[-1]
        tint = [int(num) for num in greatest]
        result.append((11.0 - numpy.var(tint), greatest, mul(tint)))
        #print greatest, ' -> ', mul(tint), sum(tint), numpy.var(tint)

    result.sort()
    for r in result:
        print r

def main():
    problem()


if __name__ == '__main__':
    main()
