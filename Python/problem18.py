
# Maximum path sum I
# By starting at the top of the triangle below and moving to adjacent numbers on the
# row below, the maximum total from top to bottom is 23.
#               3
#             7  4
#           2  4  6
#         8  5  9  3
#
# Find the maximum total from top to bottom of the triangle below:

NUMBER = """\
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


triangle = [[int(n) for n in num.split(' ') if len(n)] for num in NUMBER.split('\n') if len(num)]


def max_index(n):
    i = max(n)
    return n.index(i)


def main():
    sums = []
    index = 0
    colunm = 0
    result = triangle[colunm][index]

    while colunm <= len(triangle[1:-1]):
        colunm += 1
        children = triangle[colunm][index:index+2]
        colunm += 1
        if colunm <= len(triangle):
            gchildren = triangle[colunm][index:index+4]
            sums.append(children[0] + gchildren[0])
            sums.append(children[0] + gchildren[1])
            sums.append(children[1] + gchildren[1])
            sums.append(children[1] + gchildren[2])
            idx = max_index(sums)

            result += sums[idx]

            if idx in [1, 2]:
                index += 1
            elif idx == 3:
                index += 2

            sums = []

    print result


if __name__ == '__main__':
    main()
