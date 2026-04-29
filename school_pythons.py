

list_lengths = 5
num_of_lists = 500
matrix_size = list_lengths * num_of_lists

squares = [x**2 for x in range(1,matrix_size + 1)]

b = [ [square for square in squares[0+itter:list_lengths+itter]] for itter in range(0,matrix_size,list_lengths)   ]

c = [[square[itter//num_of_lists] for square in b] for itter in range(0,matrix_size,num_of_lists)]






def Rekurencja(a0, a1, k, m, n):

	if n == 0:
		return 0
	if n == 1:
		return 1

	for x in range(n-1):

		a2 = k * a0 + m * a1
		a0, a1 = a1, a2

	return a2


def Catalan_naive(n):


	1,1,2,5,14,42

	cat_nums = [1]

	for x in range(n):
		next_number = 0
		for index in range(len(cat_nums)):

			next_number += cat_nums[index] * cat_nums[-(index+1)]
			
		cat_nums.append(next_number)


	return cat_nums



def Catalan_true(n):

	1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796

	cat_nums = [1]


	for x in range(n):
		next_number = 0
		
		for index in range(len(cat_nums) // 2):
			next_number += cat_nums[index] * cat_nums[-(index+1)]
		

		if (len(cat_nums) % 2 == 0):
			cat_nums.append(next_number*2)

		else:
			cat_nums.append(next_number*2 + cat_nums[len(cat_nums)//2]**2)


	return cat_nums


def Pascal(row_number):

	row = [0 for x in range(row_number)]
	row[0] = 1


	counter = 0

	for x in range(row_number):
		counter += 1
		previous_val = 0
		for y in range(counter):

			temp = row[y]
			row[y] += previous_val
			previous_val = temp

	return row




def cool_game(rules, string_, iterations):

	changes = []


	for x in range(iterations):
		for letter in string_:

			try:
				changes.append(rules[letter])
			except KeyError as e:
				changes.append(letter)

		string_ = "".join(changes)
		changes.clear()

	return string_




game_rules = {

	"a" : "bab",
	"b" : "ac",
	"c" : "kamil"
}


rec = 100
cat = 40
pasc = 60
games = 4

print(f"{rec}th term of sequence: {Rekurencja(0,1,  1.1,-205,  100)}\n")
print(f"First {cat} Catalan numbers: {Catalan_true(cat)}\n")
print(f"{pasc}th pascal row: {Pascal(pasc)}\n")
print(f"{games} games played: {cool_game(game_rules,"a",games)}\n")



#WARNING. CHATGPT.
#WARNING. CHATGPT.
#WARNING. CHATGPT.

A = [9, 12, 13, 14, 23, 24, 26, 27, 34, 35, 38, 39, 41, 44, 45, 63, 65, 68, 71, 80, 82, 87, 88, 94, 98, 99]

def unique_subset_sums_by_length(arr):
    """
    Returns a list of sets: index i contains all unique sums of subsets of length i.
    """
    N = len(arr)
    sums_by_len = [set() for _ in range(N + 1)]
    sums_by_len[0].add(0)  # empty subset sum

    for x in arr:
        # iterate backwards to avoid modifying sets while iterating
        for length in range(N, 0, -1):
            # combine current element with sums of subsets of length-1
            sums_by_len[length].update(s + x for s in sums_by_len[length - 1])
    return sums_by_len

# Compute sums
sums_by_len = unique_subset_sums_by_length(A)

# Print number of unique sums for each subset length
for length, sums in enumerate(sums_by_len):
    print(f"Subset length {length}: {len(sums)} unique sums")

#WARNING. CHATGPT.
#WARNING. CHATGPT.
#WARNING. CHATGPT.


import random

def move_indices(indices, max_val):


	ind_len = len(indices)
	max_range = max_val - ind_len


	# finding, from the back, the first position that hasn't reached its max value
	place_to_change = None
	for x in range(ind_len-1,-1,-1):

		if indices[x] < max_range + x + 1:
			place_to_change = x
			break


	if place_to_change == None: return None


	# +1 to that position
	indices[place_to_change] += 1
	# indices_prime[ind_len-place_to_change] -= 1
	


	# reset everything to the right of the position
	for x in range(place_to_change+1, len(indices)):

		indices[x] = indices[x-1] + 1


	return indices


def find_subsets(A,n):

	Subsets_of_size_n = []
	Indices = list(range(n))

	while Indices is not None:
		
		Subsets_of_size_n.append([A[x] for x in Indices])
		Indices = move_indices(Indices,len(A)-1)

	return Subsets_of_size_n


def find_unique_sums(A,n):

	unique_sums = set()
	Indices = list(range(n))
	# Indices_prime = list(range(len(A)-1,n-1,-1)) 

	# print(Indices)

	while Indices is not None:
		
		unique_sums.add(sum([A[x] for x in Indices]))
		Indices = move_indices(Indices,len(A)-1)
		# Indices_prime = [list(range())]

	return unique_sums





A = list(range(1,23))
n = 5

A = [random.randint(1,100) for x in range(1,32)]

A = list(set(A))
A = [1, 2, 3, 5, 19, 22, 23, 31, 34, 35, 43, 45, 47, 56, 60, 66, 68, 69, 70, 76, 80, 81, 87]
# A = [1, 2, 3,4,5,6,7,8,9,10]

print(len(A))

for n in range(len(A)+1):
	# kamil = find_subsets(A,n)
	# itertools_ = [list(comb) for comb in itertools.combinations(A,n) ]
	# print(kamil == itertools_,"  ", len(kamil))

	print(len(find_unique_sums(A,n)))

	# print(len(kamil))
	# sums = [sum(sett) for sett in kamil]
	# print(len(set(sums)))



import functools
import sys

sys.setrecursionlimit(100000)

@functools.cache
def fib(n):
	if n == 0 or n == 1:
		return n
	return fib(n-1) + fib(n-2)

n = 999
# print(Rekurencja(0, 1, 1, 1, n))
# print(fib(n))









def power(base,exponent):


	result = 1
	b_exponent = (bin(exponent)[2:])[::-1]


	for j in range(len(b_exponent)):
		if b_exponent[j] == "1":
			result *= base**(2**j)


	return result

# print(power(29,911))



a = 252
b = 105

print(252 % 105)


def euklides(a,b):
	k_1, l_1 = 1,0
	k_2, l_2 = 0,1

	while b != 0:

		q = a // b
		a,b = b, a -q*b
		k_1,k_2 = k_2, k_1 -q*k_2
		l_1,l_2 = l_2, l_1 -q*l_2

	return (a,k_1,l_1)

print(euklides(1,10))

def inverse(n):

	result = []

	for x in range(1,n):

		NWD,a,b = euklides(x,n)
		
		if NWD == 1:
			result.append(a % n)
			continue
		result.append(None)

	return result
print(inverse(100))




exit()
c = 0
a = []
while c < 10:
	base  = random.randint(1,100_000)
	power = random.randint(1,100_000)

	result = 1
	expo = (bin(power)[2:])[::-1]

	# print(expo)

	for j in range(len(expo)):
		if expo[j] == "1":
			result *= base**(2**j)


	a.append(result == base ** power)
	# # print(result)
	# # print(base ** power)

	c+=1

print(all(a))





def cykle_perm(A):


	start = list(range(len(A)))
	cykle = []
	

	while start != []:

		cykl = [start[0]]
		start.remove(start[0])
		
		while 1:

			if cykl[0] != A[cykl[-1]]:
				start.remove(A[cykl[-1]])
				cykl.append(A[cykl[-1]])
				
				continue
			break

		cykle.append(cykl)
		cykl = []


	return cykle










	temp_A = list(enumerate(A[:]))
	cykle = []
	print(temp_A)
	end = [(None,None)] * len(A)
	used = []
	current = 0
	start = list(range(len(A)))
	
	while temp_A != None:

		if temp_A[0][0] != temp_A[0][1]:
			cykl = [temp_A[0][0], temp_A[0][1]]
		else:
			del temp_A[0]

		while 1:
			print(cykl)
			time.sleep(0.1)
			if cykl[0] != temp_A[cykl[-1]][1]:
				cykl.append(temp_A[cykl[-1]][1])
				
				continue
			break

		print(temp_A)
		temp_A = [(pos,x) for pos,x in temp_A if pos not in cykl]
		print(temp_A)
	
		cykle.append(cykl)
		cykl.clear()




# [1]
# [1 2] [2 1]
# [1 2 3] [1 3 2]

def znak(A):

	cykle = cykle_perm(A)

	k = 0
	for x in cykle:
		k += len(x) - 1

	return (-1) ** k


def composition(*permutations):

	l = lambda A, B : [B[A[x]] for x in range(len(A))]

	res = permutations[-1]
	for x in permutations[len(permutations)-2::-1]:
		res = l(res, x)


	return res



def inverse(A):
	inv = [None] * len(A)

	for (pos,x) in enumerate(A):
		inv[x] = pos

	return inv

def rand_perm(n): 
	a = list(range(n))
	random.shuffle(a)
	return a

def rand_perm2(n):
	
	a = list(range(n))
	b = []
	for x in range(n-1, -1, -1):
		r = random.randint(0,x)
		b.append(a[r])
		del a[r]
	return b

print((rand_perm2(100)))
a = [0,1,2,3,4,5,6]
random.shuffle(a)

  # [0, 1, 2, 3, 4, 5, 6]

A = [3, 4, 1, 5, 6, 0, 2]
B = [2, 5, 4, 3, 0, 6, 1]
C = [5, 6, 3, 2, 0, 1, 4]
D = [6, 0, 3, 5, 4, 1, 2]
E = [5, 6, 1, 4, 3, 2, 0]
F = [3, 1, 2, 0, 4, 5, 6]
G = [3, 0, 5, 1, 6, 2, 4]
A =        [3, 4, 1, 5, 6, 0, 2]
Ainverse = [5, 2, 6, 0, 1, 4, 3]
# print(inverse(A))
# A(B(C(D(E(F(G(x))))))) = [4, 1, 5, 6, 3, 2, 0]



print(cykle_perm(B))
print(znak(B))
# print(composition(A,B,C,D,E,F,G))
[3, 0, 5, 1, 6, 2, 4] 







def perm(a):
	n = len(a)
	s = list(range(n+1))

	for x in range(n):

		s[x] , s[x+a[x]] = s[x+a[x]] , s[x]

	return s


def move_index(l):

	max_vals = list(range(1,len(l)+1))[::-1]

	place_to_change = 0
	for x in range(len(l)-1,-1,-1):
		if l[x] == max_vals[x]:
			l[x] = 0
			continue
		l[x] += 1
		break

	return l


def kamilations(l):

	length = len(l)
	lim = math.factorial(length)
	indices = [0] * (length - 1)

	for x in range(lim):

		index_list = perm(indices)
		
		yield [l[n] for n in index_list]

		move_index(indices)


def get_perm(y,l):

	if y > math.factorial(len(l))-1:
		return -1
	
	lim = math.factorial(len(l)-1)

	length = len(l)

	index_list = []
	count = 1

	for x in range(2,length):
		for z in range(length):
			
			if z * lim <= y <= (z+1) * lim - 1:
				index_list.append(z)
				break
	
		y %= lim
		lim = math.factorial(len(l)-x)




	index_list.append(y%2)

	i_list = perm(index_list)
	return [l[n] for n in i_list]



for x in range(1,10):
	break

	l = [0] * x
	itter = 0
	correct_indexes = []
	for x in range(math.factorial(len(l)+1)):
		# print(itter,l,perm(l))
		correct_indexes.append( (itter,perm(l)) )
		l = move_index(l)
		itter += 1

	experimental_indexes = []
	for x in range(math.factorial(len(l)+1)):

		experimental_indexes.append( (x,get_perm(x,list(range(len(l)+1)))) )


	# print(experimental_indexes[-1])
	# print(correct_indexes[-1])
	print(l,experimental_indexes == correct_indexes)



print(get_perm(1000000000000000000000000000000000000000000000000000000000000000,[3,5,6,7,6,5,4,3,2,1,2,3,4,4,5,6,7,8,8,5,8,3,4,7,2,5,7,2,3,6,6,5,4,6,4,3,4,3,2,3,2,3,6,5,3,2,1,5,6,7]))


