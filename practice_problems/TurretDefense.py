"TurretDefense problem - Easy"
"Python 3"
"Submission successful"

# Class: TurretDefense
# Method: firstMiss
# Parameters: tuple (integer), tuple (integer), tuple (integer)
# Returns: integer
# Method signature: def firstMiss(self, xs, ys, times)

"Examples"
# 0)
# {3,5,6}
# {7,5,6}
# {11,15,16}
# Returns: 2
# From above.
# 1)
# {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
# {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
# {2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32}
# Returns: -1
# A target arrives every 2 seconds. Luckily it only takes 2 seconds to switch from target to target

# If you could shoot them all down, return -1. 
# Else return number shot down.

class TurretDefense:
	 def firstMiss(self, xs, ys, times):
	 	curr_x = 0
	 	curr_y = 0
	 	prev_time = 0
	 	total_shot = 0
	 	total_rem_time = 0
	 	end_time = 0
	 	for x, y, time in zip(xs, ys, times):
	 		rem_x = abs(x - curr_x)
	 		rem_y = abs(y - curr_y)
	 		total_rem_time = (rem_x + rem_y)
	 		
	 		if prev_time + total_rem_time > time:
	 			return total_shot
	 		else:
	 			total_shot += 1
	 			# make sure to save the previous time check with the next time stamp
	 			prev_time = time
	 			curr_x = x
	 			curr_y = y
	 	
	 	return -1


if __name__ == '__main__':
	xs1 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
	ys1 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
	times1 = (2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32)
	c = TurretDefense()
	print(c.firstMiss(xs1, ys1, times1))