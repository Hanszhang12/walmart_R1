f = open("test2.txt", "w+")

for i in range(1, 101):
	f.write("R"+ "{0:0=3d}".format(i) + " " + str(1))
	f.write("\n")

f.close()