
class Theater:
	def __init__(self):
		self.theater = [[0 for _ in range(20)] for _ in range(10)]
		self.rows = {0 : "A", 1 : "B", 
					 2 : "C", 3 : "D",
					 4 : "E", 5 : "F",
					 6 : "G", 7 : "H",
					 8 : "I", 9 : "J",}

	def seating(self, input):
		request = open(input, "r")
		f = open("output.txt", "w+")
		lines = request.readlines()
		self.reservations = {}

		#parsing the data and putting it into the dictionary
		for line in lines:
			curr = line.strip()
			r = curr.split(" ")
			self.reservations[r[0]] = r[1]

		#creating the seating arrangement, the function we use to create 
		#the seating arrangement should return a dictionary
		arrangements = self.assignSeats(self.reservations)

		#writing the seating arrangement into the output.txt
		for reservation in arrangements:
			output = reservation + " " + ",".join(arrangements[reservation])
			f.write(output)
			f.write("\n")
		f.close()
		return f


	##n should be the number of people we want to seat
	##function should return the seating for each person
	def assignSeats(self, requests):
		output = {}
		return "F16"



















