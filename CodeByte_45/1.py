def chmove (i,j, l, n, m) :
	l[i][j] = 0
	if i+1 < n and l[i+1][j] == 0 :
		l[i+1][j] = 3
		return 0
	elif i-1 >= 0 and l[i-1][j] == 0 :
		l[i-1][i] = 3
		return 0
	elif j+1 < m and l[i][j+1] == 0 :
		l[i][j+1] = 3
		return 0
	elif j-1 < m and l[i][j-1] == 0 :
		return 0
	else :
		return -1
def up(i, j, l, n, m) :
	if i >= 0 and i < n and j >= 0 and j < m :
		if i+1 < n and l[i+1][j] == 0 :
			l[i][j] = 5
			return 1
		elif i-1 >= 0 and l[i-1][j] == 0 :
			l[i-1][j] = 5
			return 1
		elif j+1 < m and l[i][j+1] == 0 :
			l[i][j+1] = 5
			return 1
		elif j-1 >= 0 and l[i][j-1] == 0:
			l[i][j-1] = 5
			return 1
		elif (i+1 < n and l[i+1][j] == 3 ) :
			if chmove(i+1,j, l, n, m) == 0 :
				l[i+1][j] = 5
				return 1
			else :
				return -1
		elif i-1 >= 0 and l[i-1][j] == 3:
			if chmove(i-1,j, l, n, m) == 0 :
				l[i-1][j] = 5
				return 1
			else :
				return -1
		elif j-1 >= 0 and l[i][j-1] == 3 :
			if chmove(i,j-1, l, n, m) == 0 :
				l[i][j-1] = 5
				return 1
			else :
				return -1
		elif j+1 < m and l[i][j+1] == 0 :
			if chmove(i,j+1, l, n, m) == 0 :
				l[i][j+1] = 5
				return 1
			else :
				return -1
		else :
			return 0
	else :
		return 0
n, m = map(int, raw_input().split())
r = []
l = []
te = []
rt = []
for i in range (m) :
	te.append(0)
for i in range (n) :
    r = map(int, raw_input().split())
    l.append(r)
    rt.append(te)
s = n+m
c = 0
for i in range (n) :
    for j in range (m) :
        if l[i][j] == 3 :
            	d1, d2 = i, j
	elif l[i][j] == 1 or l[i][j] == 5:
		c += 1
p = c

c = 0
if d1-1 < 0 or (d1-1 >= 0 and l[d1-1][d2] == 1) :
    c += 1
if d1+1 > n or (d1+1 < n and l[d1+1][d2] == 1) :
    c += 1
if d2-1 >= 0 or (d2-1 >= 0 and l[d1][d2-1] == 1) :
    c += 1
if d2+1 >= 0 or (d2+1 < m and l[d1][d2+1] == 1) :
    c += 1
if c == 4 :
    print "-1"
else :
	c = p
	k1 = 0
	k = 1
	pt = n+m
	f = 0
	while k != 0 :
		for i in range (n):
			for j in range (m) :
				if l[i][j] == 5 and rt[i][j] == 0:
					e = up(i+1, j, l, n, m)
					if e == -1 :
						break
					c += e
					e = up(i-1,j, l, n ,m)
					if e == -1 :
						break
					c += e
					e = up (i,j-1, l, n, m)
					if e == -1 :
						break
					c += e
					e = up(i,j+1, l, n, m)
					if e == -1 :
						break
					c += e
			if e == -1 :
				break
			for i in l :
				print i
			print "++++++++++"
		if e == -1 :
			break
		if pt == 0 :
			f = 1
			break
		pt -= 1
		print pt
		k1 += 1
	if f == 1 :
		print "-1"
	else :
		print k1

					



