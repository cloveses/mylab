length=10

s_points = {1:(3, 4, 5, 6, 7, 8),
        2:(2, 9), 3:(2, ), 4:(3, 4, 5, 6, 7, 8),
        5:(9, ), 6:(2, 9), 7:(3, 4, 5, 6, 7, 8)}

h_points = {1: (2, 9), 2: (2, 9), 3: (2,9),
            4: (2, 3, 4, 5, 6, 7, 8, 9),
            5: (2, 9), 6: (2, 9), 7: (2,9)}

e_points = {1: (2, 3, 4, 5, 6, 7, 8, 9),
            2: (2, ), 3: (2, ),
            4: (2, 3, 4, 5, 6, 7, 8, 9),
            5: (2, ), 6: (2, ),
            7: (2, 3, 4, 5, 6, 7, 8, 9)}

f_points = {1: (2, 3, 4, 5, 6, 7, 8, 9),
            2: (2, ), 3: (2, ),
            4: (2, 3, 4, 5, 6, 7, 8, 9),
            5: (2, ), 6: (2, ),
            7: (2,)}
i_points = {1: (4, 5, 6, 7, 8),
            2: (6, ), 3: (6, ),
            4: (6,),
            5: (6, ), 6: (6, ),
            7: (4, 5, 6, 7, 8)}

l_points = {1: (3,),
            2: (3, ), 3: (3, ),
            4: (3,),
            5: (3, ), 6: (3, ),
            7: (3, 4, 5, 6, 7, 8, 9)}

d_points = {1: (2, 3, 4, 5, 6, 7, 8),
            2: (3, 9),
            3: (3, 9),
            4: (3, 9),
            5: (3, 9), 6: (3, 9),
            7: (2, 3, 4, 5, 6, 7, 8)}

def letter(points, word_index, line_index):
    start = ' ' * length * word_index
    if line_index in points:
        s = ''
        for i in range(length):
            if i in points[line_index]:
                s += '*'
            else:
                s += ' '
    else:
        s = ' ' * length
    return s

if __name__ == '__main__':
    words = 'SHEF'
    points = (s_points, h_points, e_points, f_points)
    for line_index in range(10):
        line = ''
        for word_index in range(len(words)):
            line += letter(points[word_index], word_index, line_index)
        print(line)

    words = 'FIELD'
    points = (f_points, i_points, e_points, l_points, d_points)
    for line_index in range(10):
        line = ''
        for word_index in range(len(words)):
            line += letter(points[word_index], word_index, line_index)
        print(line)
