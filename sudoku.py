#Source: https://github.com/attractivechaos/plb2/blob/master/src/python/sudoku.py


def sd_genmat():
    C = [[n//9, n//81*9 + n%9 + 81, n%81 + 162, n%9*9 + n//243*3 + n//27%3 + 243] for n in range(729)]
    R = [[] for c in range(324)]
    for r in range(729):
        for c2 in range(4):
            R[C[r][c2]].append(r)
        
    return R, C

def sd_update(R, C, sr, sc, r, v):
	m = 10
	m_c = 0
	for c in C[r]: sc[c] += v<<7
	for c in C[r]:
		if v > 0:
			for rr in R[c]:
				sr[rr] += 1
				if sr[rr] == 1:
					for cc in C[rr]:
						sc[cc] -= 1
						if sc[cc] < m:
							m, m_c = sc[cc], cc
		else:
			for rr in R[c]:
				sr[rr] -= 1
				if sr[rr] == 0:
					p = C[rr]
					sc[p[0]] += 1; sc[p[1]] += 1; sc[p[2]] += 1; sc[p[3]] += 1;
	return m, m_c

def sd_solve(R, C, s):
    ret, out, hints = [], [], 0
    sr = [0] * 729
    sc = [9] * 324
    cr = [-1] * 81
    cc = [-1] * 81
    
    for i in range(81):
        if ord(s[i]) >= 49 and ord(s[i]) <= 57:
            a = ord(s[i]) - 49
        else:
            a = -1;
        if a >= 0:
            # print(sc, "\n")
            sd_update(R, C, sr, sc, i * 9 + a, 1)
            hints += 1
        out.append(a + 1)

    # print("out: ", out, "\n")
    # print("R: ", R, "\n")
    # print("C: ", C, "\n")
    # print("s: ", s, "\n")
    # print("sr: ", sr, "\n") #check
    # print("sc: ", sc, "\n") # no check
    # print("cr: ", cr, "\n")
    # print("cc: ", cc, "\n")
        
    i, m, d = 0, 10, 1
    while True:
        # print("sr: ", sr, "\n") #check
        # print("sc: ", sc, "\n") # no check
        # print("cr: ", cr, "\n")
        # print("cc: ", cc, "\n")
        while i >= 0 and i < 81 - hints:
            if d == 1:
                if m > 1:
                    for c in range(324):  # using enumerate() here is slower
                        if sc[c] < m:
                            m, cc[i] = sc[c], c
                            if m < 2:
                                break
                if m == 0 or m == 10:
                    cr[i], d = -1, -1
                    i -= 1
            c = cc[i]
            if d == -1 and cr[i] >= 0:
                sd_update(R, C, sr, sc, R[c][cr[i]], -1)
            r2_ = 9
            for r2 in range(cr[i] + 1, 9):
                if sr[R[c][r2]] == 0:
                    r2_ = r2
                    break
            if r2_ < 9:
                m, cc[i+1] = sd_update(R, C, sr, sc, R[c][r2_], 1)
                cr[i], d = r2_, 1
                i += 1
            else:
                cr[i], d = -1, -1
                i -= 1
        if i < 0:
            break
        y = out[:81]
        for j in range(i):
            r = R[cc[j]][cr[j]]
            y[r//9] = r%9 + 1
        ret.append(y)
        i -= 1
        d = -1

    return ret



hard20 = """
..............3.85..1.2.......5.7.....4...1...9.......5......73..2.1........4...9
.......12........3..23..4....18....5.6..7.8.......9.....85.....9...4.5..47...6...
.2..5.7..4..1....68....3...2....8..3.4..2.5.....6...1...2.9.....9......57.4...9..
........3..1..56...9..4..7......9.5.7.......8.5.4.2....8..2..9...35..1..6........
12.3....435....1....4........54..2..6...7.........8.9...31..5.......9.7.....6...8
1.......2.9.4...5...6...7...5.9.3.......7.......85..4.7.....6...3...9.8...2.....1
.......39.....1..5..3.5.8....8.9...6.7...2...1..4.......9.8..5..2....6..4..7.....
12.3.....4.....3....3.5......42..5......8...9.6...5.7...15..2......9..6......7..8
..3..6.8....1..2......7...4..9..8.6..3..4...1.7.2.....3....5.....5...6..98.....5.
1.......9..67...2..8....4......75.3...5..2....6.3......9....8..6...4...1..25...6.
..9...4...7.3...2.8...6...71..8....6....1..7.....56...3....5..1.4.....9...2...7..
....9..5..1.....3...23..7....45...7.8.....2.......64...9..1.....8..6......54....7
4...3.......6..8..........1....5..9..8....6...7.2........1.27..5.3....4.9........
7.8...3.....2.1...5.........4.....263...8.......1...9..9.6....4....7.5...........
3.7.4...........918........4.....7.....16.......25..........38..9....5...2.6.....
........8..3...4...9..2..6.....79.......612...6.5.2.7...8...5...1.....2.4.5.....3
.......1.4.........2...........5.4.7..8...3....1.9....3..4..2...5.1........8.6...
.......12....35......6...7.7.....3.....4..8..1...........12.....8.....4..5....6..
1.......2.9.4...5...6...7...5.3.4.......6........58.4...2...6...3...9.8.7.......1
.....1.2.3...4.5.....6....7..2.....1.8..9..3.4.....8..5....2....9..3.4....67.....
"""

a = ['', '..............3.85..1.2.......5.7.....4...1...9.......5......73..2.1........4...9', '.......12........3..23..4....18....5.6..7.8.......9.....85.....9...4.5..47...6...', '.2..5.7..4..1....68....3...2....8..3.4..2.5.....6...1...2.9.....9......57.4...9..', '........3..1..56...9..4..7......9.5.7.......8.5.4.2....8..2..9...35..1..6........', '12.3....435....1....4........54..2..6...7.........8.9...31..5.......9.7.....6...8', '1.......2.9.4...5...6...7...5.9.3.......7.......85..4.7.....6...3...9.8...2.....1', '.......39.....1..5..3.5.8....8.9...6.7...2...1..4.......9.8..5..2....6..4..7.....', '12.3.....4.....3....3.5......42..5......8...9.6...5.7...15..2......9..6......7..8', '..3..6.8....1..2......7...4..9..8.6..3..4...1.7.2.....3....5.....5...6..98.....5.', '1.......9..67...2..8....4......75.3...5..2....6.3......9....8..6...4...1..25...6.', '..9...4...7.3...2.8...6...71..8....6....1..7.....56...3....5..1.4.....9...2...7..', '....9..5..1.....3...23..7....45...7.8.....2.......64...9..1.....8..6......54....7', '4...3.......6..8..........1....5..9..8....6...7.2........1.27..5.3....4.9........', '7.8...3.....2.1...5.........4.....263...8.......1...9..9.6....4....7.5...........', '3.7.4...........918........4.....7.....16.......25..........38..9....5...2.6.....', '........8..3...4...9..2..6.....79.......612...6.5.2.7...8...5...1.....2.4.5.....3', '.......1.4.........2...........5.4.7..8...3....1.9....3..4..2...5.1........8.6...', '.......12....35......6...7.7.....3.....4..8..1...........12.....8.....4..5....6..', '1.......2.9.4...5...6...7...5.3.4.......6........58.4...2...6...3...9.8.7.......1', '.....1.2.3...4.5.....6....7..2.....1.8..9..3.4.....8..5....2....9..3.4....67.....', ''] 


def main(n):
    R, C = sd_genmat()
    #print(R)
    #print(C)
    for i in range(n):
        for l in a:
            if len(l) >= 81:
                print(l)
                ret = sd_solve(R, C, l)
                print(ret)
                break
                    #if i == 1: print(ret)
                    # for j in ret:
                    #         print(''.join(map(str, j)))
                    # print('');



main(1)
# BENCHMARKING:
# import time

# for i in range(20):
#     start_time = time.time()
#     main(20)
#     end_time = time.time()
    
#     execution_time = end_time - start_time
#     print(str(round(execution_time, 4)).replace(".",","))
