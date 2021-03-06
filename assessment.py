import heapq

class Theater:
	def __init__(self):
		#create a 2D array representing the theater
		self.theater = [[0 for _ in range(20)] for _ in range(10)]
		#corresponding indexes to row letters
		self.rows = {0 : "A", 1 : "B", 
					 2 : "C", 3 : "D",
					 4 : "E", 5 : "F",
					 6 : "G", 7 : "H",
					 8 : "I", 9 : "J",}

	#input - file path
	#output - file containing the output
	def seating(self, input):
		request = open(input, "r")
		f = open("output.txt", "w+")
		lines = request.readlines()
		self.reservations = {}

		#parsing the data and putting it into the dictionary
		for line in lines:
			curr = line.strip()
			r = curr.split(" ")
			self.reservations[r[0]] = int(r[1])

		#creating the seating arrangement, the function we use to create 
		#the seating arrangement should return a dictionary
		arrangements = self.assignSeats(self.reservations)

		#writing the seating arrangement into the output.txt
		for reservation in self.reservations:
			if reservation in arrangements:
				output = reservation + " " + ",".join(arrangements[reservation])
				f.write(output)
				f.write("\n")
			else:
				f.write(reservation + " " + "N/A")
				f.write("\n")
		f.close()
		return f


	##function should return the seating for each person
	def assignSeats(self, requests):
		#we're only doing range(5) because we want there to be a buffer row between
		#each row. The rows array contains arrays. The first value in the inner array should be 
		#the number of available spots left in the row and the second value should be the next index 
		#that you can reserve a seat in that row. We start off with (20, 0) because there are 20 available
		#seats and the first index where you can place it at is 0. 

		rows = [[20, 0] for i in range(5)]
		totalAvailable = 100

		##used to sort the values in descending order
		maxHeap = []
		for r in requests:
			#we use negative values because we want a max heap
			heapq.heappush(maxHeap, (-requests[r], r))

		while maxHeap and totalAvailable > 0:
			reserve = heapq.heappop(maxHeap)
			numSeats = -reserve[0]
			ID = reserve[1]

			found = False
			#check each row to see if there are available seats
			for i in range(len(rows)):
				if numSeats < rows[i][0]:
					#set the elements in the theater equal to the ID
					for j in range(numSeats):
						##we're doing i*2 for the buffer rows
						self.theater[i * 2][rows[i][1] + j] = ID
					##we also subtract 3 to account for the buffer seats
					rows[i][0] = rows[i][0] - numSeats - 3
					rows[i][1] = rows[i][1] + numSeats + 3
					totalAvailable = totalAvailable - numSeats - 3
					found = True
					break
			#if there isn't enough space to place the party in one row,
			#we divide up the seats, add it back onto our heap
			if not found and numSeats > 1: 
				heapq.heappush(maxHeap, (-numSeats//2, ID))
				heapq.heappush(maxHeap, (-(numSeats-numSeats//2), ID))

		##self.build() should return a dictionary of IDs that map 
		##to their reserved seats
		return self.build()


	def build(self):
		output = {}
		#start building the output from self.theater
		for row in range(len(self.theater)):
			for col in range(len(self.theater[0])):
				ID = self.theater[row][col]
				if ID != 0:
					if ID in output:
						output[ID].append(self.rows[row] + str(col+1))
					else:
						output[ID] = [self.rows[row] + str(col+1)]
		return output















