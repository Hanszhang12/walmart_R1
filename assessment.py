
class Theater:
	def __init__(self):
		self.theater = [[0 for _ in range(20)] for _ in range(10)]

	def seating(self, input):
		request = open(input, "r")
		f = open("output.txt", "w+")
		lines = request.readlines()
		for line in lines:
			curr = line.strip()
			r = curr.split(" ")

			seats = self.findAvailable(r[0])
			output = r[0] + " " + seats
			print(output)
			f.write(output)
			f.write("\n")
		f.close()
		return f


	##n should be the number of people we want to seat
	##function should return the seating for each person
	def findAvailable(self, n):
		return "F16"