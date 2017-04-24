#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem19.py
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
# Counting Sundays
#
# You are given the following information, but you may prefer to do some research for yourself.
#                1 Jan 1900 was a Monday.
#                 Thirty days has September,
#                   April, June and November.
#                    All the rest have thirty-one,
#                     Saving February alone,
#                       Which has twenty-eight, rain or shine.
#                           And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

import datetime

INIT_DATE = (1, 1, 1900, 1)

WEEKDAYS = {
    1: 'sunday',
    2: 'monday',
    3: 'tuesday',
    4: 'wednesday',
    5: 'thursday',
    6: 'friday',
    7: 'saturday',
}


def is_leap(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


def count_sundays():
    day = 1
    month = 1
    year = 1901
    weekday = 3

    count = 0

    while not (day == 1 and month == 1 and year == 2001):

        if is_leap(year) and month == 2:
            day = (day + 1) % 30
        elif month == 2:
            day = (day + 1) % 29
        elif month in [9, 4, 6, 11]:
            day = (day + 1) % 31
        else:
            day = (day + 1) % 32

        if day == 0:
            day = 1
            month = (month + 1) % 13

            if month == 0:
                month = 1
                year += 1

        weekday = (weekday + 1) % 8
        if weekday == 0:
            weekday = 1
            date = datetime.date(day=day, month=month, year=year)

        if day == 1 and weekday == 1:
            count += 1
            print '%d/%d/%d - %s' % (day, month, year, WEEKDAYS.get(weekday)), '#', date.strftime("%d/%m/%Y %A")

    print count


def main():
    count_sundays()


if __name__ == '__main__':
    main()
