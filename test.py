import assessment

if __name__ == '__main__':
	#test1 Basic test
	testTheater1 = assessment.Theater()
	output = testTheater1.seating("test1.txt")
	f = open("output.txt", "r")
	f1 = open("output1.txt", "w+")

	for line in f.readlines():
	    f1.write(line)

	f1.close()
	f.close()

	#test2 100 requests of 1
	testTheater2 = assessment.Theater()
	output = testTheater2.seating("test2.txt")
	f = open("output.txt", "r")
	f1 = open("output2.txt", "w+")

	for line in f.readlines():
	    f1.write(line)

	f1.close()
	f.close()

	#test3 1 request of 100 
	testTheater3 = assessment.Theater()
	output = testTheater2.seating("test3.txt")
	f = open("output.txt", "r")
	f1 = open("output3.txt", "w+")

	for line in f.readlines():
	    f1.write(line)

	f1.close()
	f.close()

	#test4 1 
	testTheater4 = assessment.Theater()
	output = testTheater4.seating("test4.txt")
	f = open("output.txt", "r")
	f1 = open("output4.txt", "w+")

	for line in f.readlines():
	    f1.write(line)

	f1.close()
	f.close()