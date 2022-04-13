# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 14:45:26 2022

@author: sam-b
"""


"""Imports the following modules to be used in the code - matplotlib.pyplot, 
time, csv. Import the agentframework module created by the user"""
import matplotlib.pyplot
import time
import csv
import agentframework

"""Start the timer for the code"""
start = time.process_time()

"""Read the in.txt file in csv format by using the csv reader code, by using the
open function and starting a blank newline. Create a reader variable to use the
csv.reader function, and convert the values to floating point. iterate through 
the rows and values within the list to print the values. Close the in_txt after
finishing with it to prevent versioning issues.
Create environment list before any processing is done, and create rowlist before 
each row is processed. Append each value to rowlist then append each row to
environment to create a 2D list."""
in_textfile_csv = open('in.txt', newline='')
in_textfile_reader = csv.reader (in_textfile_csv, quoting=csv.QUOTE_NONNUMERIC)
environment = []
for row in in_textfile_reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
    #print(value)
in_textfile_csv.close()

"""Create a function to run the pythagorus' theorum code on a pair of agents.
The x and y coordinates are taken from the agentframework module."""
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.getx() - agents_row_b.getx())**2) + ((agents_row_a.gety() - agents_row_b.gety())**2))**0.5

"""Create an empty list called distance_list, used to obtain the maximum and 
minimum distances between the variables. (Note - the distance variable created
whilst calling the distance between function could just have easily been used
as a list with the same purpose, thus reducing the requirement to create an 
additional variable. However this is safer as it is unknown if the distance 
variable as part of the core code would clash with later practical exercises
if changed to list format.)"""
distance_list = []

"""Create a new variable to control the amount of agents used"""
number_of_agents = 3

"""Create a new variable to control the amount of iterations within the for loop 
to move the agents"""
number_of_iterations = 100

"""Create an empty list called with the variable name agents"""
agents = []

"""Populate the agents list by appending Agents class within the agentframework
module to the amount specified within the number_of_agents variable by using a 
for loop to count the amount of iterations. Also link the envronment list to 
the agents list."""
for i in range(number_of_agents):
    agents.append(agentframework.Agent(environment))

"""An embedded for loop, the top line indicates how many iterations the remainder
of the block should loop based on the number_of_iterations variable. The called 
move and eat methods taken from the agentframework module"""
for i in range(number_of_iterations):
    for i in range(number_of_agents):
        agents[i].move()
        agents[i].eat()

"""Prints the agents varibale to test the container works, using the __str__()
method from the agentframework module."""
for i in range(number_of_agents):
    print(agents[i].__str__())
    
"""Call the distance_between function iterating through every coodinate within
the agents list, and print the answer. Populate the distance_list with the 
outcome values. The 'if' statement is inlcuded to ensure there are no repeats
of pairs of agents and also they don't test against themselves."""
for agents_row_a in agents:
    for agents_row_b in agents:
        if agents_row_a != agents_row_b and agents_row_a.getx() <= agents_row_b.getx():
            distance = distance_between(agents_row_a, agents_row_b) 
            distance_list.append(distance)
            print("The distances are " + str(distance))

"""Find the maximum and minimum distance between the agents and print the results"""
maximum_distance = max(distance_list)
minimum_distance = min(distance_list)

print("Maximum Distance is " + str(maximum_distance))
print("Minimum Distance is " + str(minimum_distance))

"""Create a graph with a X and Y axis ranging from 0 to 100, and add the 
environments raster taken from the in.txt file"""
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.imshow(environment)

"""Plot the amount of coordinates demoted by the number_of_agents variable by
iterating through the for loop, the coodrinates are taken from the iteration
container and then X and Y in turn"""
for i in range(number_of_agents):
    matplotlib.pyplot.scatter(agents[i].getx(),agents[i].gety())

"""Display the graph and plots"""
matplotlib.pyplot.show()

"""Write the output envoronment as a text file, using the csv writer function.
Open the blank environment_output.txt file and call the csv.writer function
with the delimiter as a comma. Iterate and write through each row in environment
then close the textfile. (Please note the writin text file is in float format,
which is not optimal as it includes a .0 after each value which uses unessesay
space. Did not figure out how to convert the values to int)."""
write_environment = open('environment_output.txt', 'w', newline='')
writer = csv.writer(write_environment, delimiter=',')
for row in environment:
    writer.writerow(row)
write_environment.close()

"""Write the stored values as a text file using the write function, opening as
'a' to write and append the values. Open the blank stored_values.txt. Iterate 
through the number_of_agents and write the store value and a comma deliniation.
Write a new line after each session to begin the new append on a new line, then 
close the stored_values.txt."""
write_store = open('stored_values.txt', 'a')
for row in range(number_of_agents):
    write_store.write(str(agents[row].getstore()) + ", ")
write_store.write("\n")
write_store.close()

"""End the timer for the code"""
end = time.process_time()

"""Print the time the code run by running the difference between the start and 
end clock"""
print("time = " + str(end - start))






"""Redundant Code (Archived code as the model has eveloved and stored below 
the live code to provide a record of changes)"""

"""Create a graph to check the in.txt environment 2D list diplays properly. 
(Now Redundant - both graphs environment and agents are displayed within the
 same graph)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()"""
    
"""Prints the maximum coordinate from the agents, using the operator.itemgetter
function to choose the second (or easterly) variable in each column in the list
(Now Redundant - Unfortuantely could not figure out how to continue the print most
 easterly funtion after importing from the agentframwork module as the list
 charateristics of the agents seemed to change. Lots of tinkering with this line
 but no successful results.)
print("Most Easternly Coordinate is " + str(max(agents, key=operator.itemgetter(1))))"""    

"""Create a new variable (object) from the Agent class within the agentframework
module. (Now Redundant - created to test the agentframework module properly, 
the test was successful)
a = agentframework.Agent()"""
    
"""Print the coordinates for object a to test it is proerly working, and print
the moved coordinates to test the move method is working. (Now Redindant - 
the test was successfully carried out)
print("Agent a coordinates are " + str(a.x), str(a.y))
a.move ()
print("Moved Agent a coordinates are " + str(a.x), str(a.y))"""
    
"""Test the agentframework module has properly connected to the main code page,
by creating and printing an agent.(Now Redundant - Test was Successful)
a = agentframework.Agent()
print(a)"""
    
"""Test the distance_list recall (Now Redundant - Test Successful)
print(distance_list)"""

"""Print the straight line distance between the yx0 and yx1 coordinate variables,
to check answer on calulator (Now Redundant - Python Code now not in play)
print(hypotenuse)"""
    
"""Perform Pythagorus' theorem to calculate the straight line distance 
between the yx0 and the yx1 coordinate variables (Now Redundant - Replaced by
distance_between function)
y_axis_calulation = (agents[0][0] - agents[1][0]) ** 2
x_axis_calcualtion = (agents[0][1] - agents[1][1]) ** 2
sum_of_axis_calculations = (y_axis_calulation + x_axis_calcualtion)
hypotenuse = sum_of_axis_calculations ** 0.5"""
    
"""Plot the eaternly coordinate as red and westernly coordinate as blue. (Now
Redundant - replaced by the for loop to plot the amount of iterations in 
number_of_agents variable)
matplotlib.pyplot.scatter(red[1],red[0],color='red')
matplotlib.pyplot.scatter(blue[1],blue[0],color='blue')"""

"""Create red and blue variables to encompass the most eastern and most western
coordinates from the list agents(Now Redundant - colour coding not required)
red = max(agents, key=operator.itemgetter(1))
blue = min(agents, key=operator.itemgetter(1))"""
    
"""Using the if/else statements increase or decrase the value of the coordinate
variables in steps of 1, dependant on if the random number is greater than 0.5
(Now Redundant - replaced by for loop to account for greater number of agents 
 created)
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1
if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1"""
    
"""Append random integers between 0 and 99 to the agents list, the list will
be a 2 dimensional list, with each column containing a value relating to an
X and Y coordinate (Now Redundant - Replaced by number_of_agents for loop
agents.append([random.randint(0,100),random.randint(0,100)])
agents.append([random.randint(0,100),random.randint(0,100)])"""

"""Create two sets of coordinate variables (yx0 and yx1) using the random.randint
function to include values between 0 and 99 (Now Redundant - Replaced by agents list)
y0 = random.randint(0,99)
x0 = random.randint(0,99)

y1 = random.randint(0,99)
x1 = random.randint(0,99)"""

"""Create a set of Y and X variables, to represent coordinates, 
and assign them the integer 50 (Now Redundant - Replaced by random.randint function)
y0 = 50
x0 = 50"""

"""Create a second set of coordinate variables (Now Redundant - Replaced by 
random.randint function)
y1 = 50
x1 = 50"""

"""Randomise the second set of coordinate varibales using the same method as above
 (Now Redundant - Replaced by random.randint function)
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1
    
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1"""
    
"""Print the two sets of coordinate variables to test they work(Now Redundant 
- Replaced by agents list)
print(y0, x0)
print(y1, x1)"""

"""print red and blue variables to test values and see output (Now Redundant -
testing only for purpose of determining code)
print(red)
print(blue)"""

"""Test the document properly runs code (Now Redundant - relpaced by model)
print ("Hello World")"""