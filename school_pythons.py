

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














