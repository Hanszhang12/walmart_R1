# Walmart_R1 Instructions

Overview:
Implement an algorithm for assigning seats within a movie theater to  fulfill reservation requests. Assume the movie theater has the seating  arrangement of 10 rows x 20 seats, as illustrated to the right. 

##
Your homework assignment is to design and write a seat assignment  program to maximize both customer satisfaction and customer  safety. For the purpose of public safety, assume that a buffer of three  seats and/or one row is required. 

## Input Description 
You will be given a file that contains one line of input for each  reservation request. The order of the lines in the file reflects the order in  which the reservation requests were received. Each line in the file will be  comprised of a reservation identifier, followed by a space, and then the  number of seats requested. The reservation identifier will have the  format: R####. See the Example Input File Rows section for an  example of the input rows. 

## Output Description 
The program should output a file containing the seating assignments for  each request. Each row in the file should include the reservation number  followed by a space, and then a comma-delimited list of the assigned  seats. See the Example Output File Rows section for an example of  the output file content. 

## Requirements 
Implement your solution using a programming language that  you are comfortable with. We work in Java, but we are more  interested in understanding how you think than in language  specifics. 
The solution and tests should build and execute entirely via the  command line. 
The command for executing the program should accept the  complete path to the input file as an argument and should  return the full path to the output file. 
Create a README file that documents your assumptions and  includes instructions for building the solution and executing the  tests. 

## Walmart - Movie Theater Seating Challenge 

## Guidelines
10 rows x 20 seats, 200 seats in total. Buffer of 3 seats and one row is required. For customer satisfaction, we should put as many people in the front rows as possible while maintaining the other restrictions. 

## Assumptions
Let's make the assumption that the customers want to be seated closer with the screen. Each group must also be sitting on the same row. Groups that are together want to be seated right next to each other. If it's not possible to seat the whole group on one row, split the group into two and try finding available seating. We do this so that there isn't a case where 9 customers in a group are seated together while 1 is sitting on a separate row. 

We care most about our customer's safety so we should never break the guidelines. If necessary, we dont output the request if it goes over the capacity we are allowed to seat. If a reservation doesn't go through, it will have a "N/A" next to its reservation ID in the output file.

## Implementation
Use a 2D Array to represent the theater. Seats that are empty should be represented with a 0. Seats that are filled should be represented with their reservation identifier. Let's also initialize a dictionary that maps row numberIDs to their corresponding letter. This will make it easier for us later on when building up our output.

The Theater class is used to implement the algorithm. This class will encapsulate the 2D array and will be responsible for coming up with the seating arrangement. Each Theater class will take in one file input and will have a seating method that comes up with the seating arrangement.

## Methods
The seating method is the function that takes in the file.txt input. It's responsible for parsing the data and mapping the reservation ID to the number of seats requested. It's also responsible for writing the output to the file

For our assignSeats method, we should be returning a dictionary of request ID to an array of seat numbers. For our algorithm, we want to first sort the requests in descending order by the number of seats they are requesting and then assign them seats in that order. This would be better because it places the larger parties in the front and also maximizes the number of people we can seat in the theater. We can do this by using a max Heap. We do this by using the python minheap but inserting the values as negative values.

If the party is too big for any of the available rows, we would split the party up and see if it's possible to fit any of them in an available row. We would only do this if there's enough room for all of the members of the party. If we split them up and one part of the group doesn't have seating, we would only be able to give seating to part of the group.

## Tradeoffs
The safety guidelines restrict people from sitting in consecutive rows. Without this restriction, we can easily change parts of our code to accomodate for this. Another tradeoff would be that the people who requested a seat first wouldn't necessarily be getting an ideal seat. The reservations with a larger party would also be seated in a better spot. One issue that I ran into when running the tests was with test3. This test had 1 request of 100 people. Ideally, we would be able to fit them all into the theater but because we split up the groups when there isn't enough space, this couldn't be achieved. 









