"UGroupOrder - Medium Problem"
"""
Two integers are relatively prime if they have no common factors other 
than 1. For example, 8 and 6 are not relatively prime since they are 
both divisible by 2. 27 and 10 are relatively prime since they have 
no common factors other than 1. Note that 1 is relatively prime to 
all numbers.
"""

"Definition"
"""
Class: UGroupOrder
Method: findOrders
Parameters: integer
Returns: tuple (integer)
Method signature: def findOrders(self, N):
"""

"Examples"
"""
## 0)
9
Returns: { 1, 6, 3, 6, 3, 2 }
1^1 mod 9 = 1
2^6 mod 9 = 1
4^3 mod 9 = 1
5^6 mod 9 = 1
7^3 mod 9 = 1
8^2 mod 9 = 1
## 1)
8
Returns: { 1, 2, 2, 2 }
This is the example given in the problem statement.
## 2)
15
Returns: { 1, 4, 2, 4, 4, 2, 4, 2 }
## 3)
51
Returns: { 1, 8, 4, 16, 16, 8, 16, 16, 4, 16, 2, 8, 16, 16, 16, 8, 8, 16, 16, 16, 8, 2, 16, 4, 16, 16, 8, 16, 16, 4, 8, 2 }
## 4)
10
Returns: { 1, 4, 4, 2 }
"""

# input is int
# output is tuple
from fractions import gcd
class UGroupOrder:
	def findOrders(self, N):
		# 2^5 is 2**5 in py
		# mod is % in py
		fin = []
		u_n = []
		# 1 is always going to be relatively prime
		fin.append(1)

		# to find order of U(N)
		for i in range(2, N):
			if gcd(i, N) is 1:
				u_n.append(i)
			else:
				pass

		# to find Orders
		for p in (u_n):	
			for j in range(1, N-1):
				pow_c = (p**j)
				mod_c = (pow_c % N)
				if (mod_c is 1):
					fin.append(j)
					break
				else:
					pass

		return fin

if __name__ == '__main__':
	N1 = 51
	c = UGroupOrder()
	print((c.findOrders(N1)))
	for_sure_ans = [1, 8, 4, 16, 16, 8, 16, 16, 4, 16, 2, 8, 16, 16, 16, 8, 8, 16, 16, 16, 8, 2, 16, 4, 16, 16, 8, 16, 16, 4, 8, 2]
	if for_sure_ans == (c.findOrders(N1)):
		print("Correct!")
	else:
		print("Try again")

	prob_a = [1,8,4,16,16,8,16,16,4,16,2,8, 16, 16, 16, 8, 8, 16, 16, 16, 8, 2, 16, 4, 16, 16, 8, 16, 16, 4, 8, 2]
	checke = [1,8,4,16,16,8,16,16,4,16,2,8, 16, 16, 16, 8, 8, 16, 16, 16, 8, 2, 16, 4, 16, 16, 8, 16, 16, 4, 8, 2]
	myy_sure_ans = (c.findOrders(51))
	print(for_sure_ans==myy_sure_ans)
	my_return_val_on_topcoder: [1,8,4,16,16,8,16,16,4,16,2,8,8,8,8,2,4,8,4,8,2]
	
