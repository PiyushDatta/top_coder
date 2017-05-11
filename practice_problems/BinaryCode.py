"Binary Code Problem"
"Submission Successful"

"""
Class: BinaryCode
Method: decode
Parameters: string
Returns: tuple (string)
Method signature: def decode(self, message):
"""

"Examples:"
"""
0)
"123210122"
Returns: { "011100011", "NONE" }

The example from above.

1)
"11"
Returns: { "01", "10" }

We know that one of the digits must be '1', and the other must be '0'. 
We return both cases.

2)
"22111"
Returns: { "NONE", "11001" }

Since the first digit of the encrypted string is '2', the first two 
digits of the original string must be '1'. Our test fails when we 
try to assume that P[0] = 0.
"""
"Algorithm:"
"""
An encrypted string given to you in this format can be decoded as 
follows (using 123210122 as an example):

Assume P[0] = 0.
Because Q[0] = P[0] + P[1] = 0 + P[1] = 1, we know that P[1] = 1.
Because Q[1] = P[0] + P[1] + P[2] = 0 + 1 + P[2] = 2, we know that P[2] = 1.
Because Q[2] = P[1] + P[2] + P[3] = 1 + 1 + P[3] = 3, we know that P[3] = 1.
Repeating these steps gives us P[4] = 0, P[5] = 0, P[6] = 0, P[7] = 1, 
and P[8] = 1. We check our work by noting that Q[8] = P[7] + P[8] = 1 + 1 = 2. 
Since this equation works out, we are finished, and we have recovered 
one possible original string. Now we repeat the process, assuming the 
opposite about P[0]:

Assume P[0] = 1.
Because Q[0] = P[0] + P[1] = 1 + P[1] = 1, we know that P[1] = 0.
Because Q[1] = P[0] + P[1] + P[2] = 1 + 0 + P[2] = 2, we know that P[2] = 1.
Now note that Q[2] = P[1] + P[2] + P[3] = 0 + 1 + P[3] = 3, which leads 
us to the conclusion that P[3] = 2. However, this violates the fact 
that each character in the original string must be '0' or '1'. 
Therefore, there exists no such original string P where the first 
digit is '1'.

"""
class BinaryCode:
	def decode(self, message):
		p_equal_0 = [0]
		p_equal_1 = [1]
		p_0 = ""
		p_1 = ""
		combined_0 = 0
		combined_1 = 1
		# using p[0] = 0
		for i in range(len(message)):
			# len(message) = 9
			# i = 0, starting out
			# p[1] = mess[0] - p[0]
			# p[0] = 0
			new_p = int(message[i]) - combined_0
			if (new_p > 1) or (new_p < 0):
				p_equal_0 = "NONE"
				break
			else:
				p_equal_0.append(new_p)
				if len(p_equal_0) < 2:
					combined_0 = sum(p_equal_0)
				else:
					combined_0 = sum(p_equal_0[-2:])

		# using p[0] = 1
		for i in range(len(message)):
			new_p = int(message[i]) - combined_1
			if (new_p > 1) or (new_p < 0):
				p_equal_1 = "NONE"
				break
			else:
				p_equal_1.append(new_p)
				if len(p_equal_1) < 2:
					combined_1 = sum(p_equal_1)
				else:
					combined_1 = sum(p_equal_1[-2:])


		if p_equal_0 is not "NONE":
			for i in range(len(p_equal_0)-1):
				p_0 += str(p_equal_0[i])
			
		else:
			p_0 = "NONE"

		if p_equal_1 is not "NONE":
			for i in range(len(p_equal_1)-1):
				p_1 += str(p_equal_1[i])
		else:
			p_1 = "NONE"

		return p_0, p_1


if __name__ == '__main__':
	message1 = "123210122"
	message2 = "11"
	c = BinaryCode()
	print(c.decode(message2))
	# Returns: { "011100011", "NONE" }
	# Returns: { "01", "10" }
	# 9 digits

