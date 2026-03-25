

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






