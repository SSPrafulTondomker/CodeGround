n = input()
l = map(int, raw_input().split())
r = []
for i in range (50) :
	r.append(0)

r[0] = l[0]
i = 1

i = 0
k = len(l)
s = ""
j = 1
while j < n :
	#print s
	if i%2 == 0 and i != 0:
		i = 2*(i+2)
	elif i != 0 :
		i = 2*(i+1)
	if j%2 != 0 :
		while i < k :
			s += str(l[i]) + " "
			i = 2*i+1
		i = (i-1)/2
		i += 1
	else :
		while i < k :
			s += str(l[i]) + " "
			i = 2*i + 2
		i = (i-2)/2
		i += 2
	while i < k :
		s += str(l[i]) + " "
		i += 1
	i -= 1
	#print s
	if i%2 == 0 :
		i = (i-2)/2
	else :
		i = (i-1)/2
	while i > 0 :
		s += str(l[i]) + " "
		if i%2 == 0 :
			i = (i-2)/2
		else :
			i = (i-1)/2

	j += 1
s = s.strip(" ")
print s[:len(l)*4]
	

#print r



