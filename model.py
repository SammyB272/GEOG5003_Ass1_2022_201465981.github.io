# -*- coding: utf-8 -*-
"""
Title: agentframework.py
Created on Mon Apr 11 15:15:07 2022
Version: 1
Author: Student ID - 201465981

The model creates a number of agents which have several effects on the input environment,
 in order to eat away at the environment and store the eaten properites. 

- The environment file is read into the model, which contains 300 pixels worth of data.
- The input parameters are created - number_of_agents, number_of_iterations and neighbourhood.
- The blank agents list is created and populated using random XY coordinates within the 
  environment from the __init__ method in the agentsframework module.
- Calls several methods from the agentsframework module to affect the environment.
    The move method changes the agents coordinates in small steps. 
    The eat method scoops up 10 values from the agents' pixel in the environment and stores them. 
    The greedy method removes values from the store and back into the environement.
    The share_with_neighbours method allows the agents to split their stores.
- The maximum and minimum distances are calculated and printed.
- An animation of the environment is created and displayed, plotting the agents 
  and showing the effects of their actions over a number of iterations.
- The output environment and store text files are written in the directory.
"""


"""Imports the following modules to be used in the code - matplotlib.pyplot, 
time, csv, random, matplotlib.animation, sys. Import the agentframework module 
created by the user"""
#import matplotlib
#import tkinter
#matplotlib.use('TkAgg') 
import matplotlib.pyplot
import time
import csv
import random
import matplotlib.animation
import sys
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
environment to create a 2D list.
Find and return the size of the environment."""
in_textfile_csv = open('in.txt', newline='') #open in.txt
in_textfile_reader = csv.reader (in_textfile_csv, quoting=csv.QUOTE_NONNUMERIC) #use csv reader, convert to float
environment = [] #create the environment variable as a blank list
for row in in_textfile_reader: #for each row of data within the in.txt file.
    rowlist = [] #create rowlist valiable as a blank list
    for value in row: #for each data value in the rows
        rowlist.append(value) #create a bunch of 1D lists
    environment.append(rowlist) #merge into a 2D list
in_textfile_csv.close() #close the textfile

#Find size of environment to detemine some model settings (commented out as no longer needed)
#size_of_environment = len(environment) #count the amount of rows in the environment list
#print("The size of the environment is " + str(size_of_environment)) #test print

"""Create the variables and input parameters for the code"""
#Input Parameters
number_of_agents = 10 #control the amount of agents used
number_of_iterations = 100 #control the number of agent actions on the environment
neighbourhood = 20 #control the search distance of the agents
#Model Variables
agents = [] #An empty list to hold the agents values
distance_list = [] #An empty list, to obtain the max and min distances between the agents

"""Input Parameters using the sys.argv function which allows user input using the 
command line"""
number_of_agents = int(sys.argv[1]) #the sys.argv list order is the same order as the input parameters should be entered
number_of_iterations = int(sys.argv[2])
neighbourhood = int(sys.argv[3])

"""Populate the agents list by appending Agents class within the agentframework
module to the amount specified within the number_of_agents variable by using a 
for loop to count the amount of iterations. Also link the envronment list to 
the agents list."""
for i in range(number_of_agents): #iterate through the number_of_agents parameter
    agents.append(agentframework.Agent(environment, agents)) #add the Agent object __init__ values

"""Create a new figure that is 7 by 7 inches, and create the axis from 0 to 1
in both directions. Create the carry_on variable to get the animation continuing/
stopping contidition.

Define a function to clear the figure then update with fresh changes in each
iteration based on the enbedded for loops.
An embedded for loop, the top line indicates how many iterations the remainder
of the block should loop based on the number_of_iterations variable. Shuffle the 
aggents list after each iteration to randomise the order of the agents carrying
out the called methods. The called move, eat, greedy and share_with_neighbours 
methods taken from the agentframework module. (The neighbourhood value is taken 
from the input parameter).
If a random.random return is under 0.1 then change the carry_on to false and 
stop iterating through the frame_number function.
Create a graph with a X and Y axis ranging from 0 to 300, and add the 
environments raster taken from the in.txt file.
Plot the amount of coordinates demoted by the number_of_agents variable by
iterating through the for loop, the coodrinates are taken from the iteration
container and then X and Y in turn.

Create a function called gen_function which iterates through the animation frames.

Create the animaton using the matplotlib.animation.FuncAnimation function. The
figure is the created fig variable, then update the animation using the update
function, the frames are the gen_function function and do not repeat after the 
animation.
Display the animation.
"""
fig = matplotlib.pyplot.figure(figsize=(7, 7)) #create the 7x7 inch fugure
ax = fig.add_axes([0, 0, 1, 1]) #create the XY axis
carry_on = True #whilst carry_on equals true the animation will keep running

def update(frame_number): #create the update frame_number function
    fig.clear() #clear the fugure
    global carry_on #making the variable global allows the update to be used outside of the function
    for i in range(number_of_iterations):#controls the total amount of actions
        for i in range(number_of_agents):#makes sure each agent does the actions
            random.shuffle(agents) #randomising the starting agent 
            agents[i].move() #call the methods from the agentframework module
            agents[i].eat()
            agents[i].greedy()
            agents[i].share_with_neighbours(neighbourhood, agents)
    if random.random() < 0.1: #a 10% chance
        carry_on = False #make carry_on false
        #print("stopping condition") #Test print
    for i in range(number_of_agents):
        matplotlib.pyplot.ylim(0, 300) #create y axis between 0 and 300
        matplotlib.pyplot.xlim(0, 300) #create x axis between 0 and 300
        matplotlib.pyplot.imshow(environment)  #show the environment values
        matplotlib.pyplot.scatter(agents[i].getx(),agents[i].gety()) #plot the XY coordinate
        #print(agents[i].getx(),agents[i].gety()) #test print

def gen_function(b = [0]): #create the gen_function function
    a = 0 #create variable and set to 0
    global carry_on #check carry_on is true
    while (a < 10) & (carry_on) : #whilst a is under and carry_on
        yield a			# Returns control and waits next call.
        a += 1 #add 1 to a

animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.show() #display the animation

"""The GUI code to make the model popup window and allow the user to choose the 
run function. Managed to make this section mostly run good, but after completing
the run action and even closing the GUI, the rest of the code did not finish and
lest the command line in a suspended state. Would resolve this issue for future verions
of the model, however the decision was made to revert to the animation that occurs
automatically after the command line has been run."""
#def run():
#   animation = matplotlib.animation.FuncAnimation(fig, update, 
#                                                   frames=gen_function, repeat=False)
#   canvas.draw()
    
#root = tkinter.Tk()
#root.wm_title("Model")
#canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
#canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#menu_bar = tkinter.Menu(root)
#root.config(menu=menu_bar)
#model_menu = tkinter.Menu(menu_bar)
#menu_bar.add_cascade(label="Model", menu=model_menu)
#model_menu.add_command(label="Run model", command=run) 

"""Test print to check the agents can see each other by creating a variable called
look agents and selecting a diffent agent from the list that the check agent, then
calling the check_agent method against the newly created variable."""
# (Commented Out as used for test of code)
#look_agent = agents[0] #make variable from the item 0 in agents list
#look_agent.check_agent() #print if the look_agent is able to call the check_agent

"""Prints the agents varibale to return the final values after running the model, 
using the __str__() method from the agentframework module."""
for i in range(number_of_agents): #ensures all the agents are included
    print(agents[i].__str__()) #prints the __str__ return
 
"""Call the distance_between function iterating through every coodinate within
the agents list, and print the answer. Populate the distance_list with the 
outcome values. The 'if' statement is inlcuded to ensure there are no repeats
of pairs of agents and also they don't test against themselves. (Please note, this
could have been removed but the decision was made not to because the code block
displays elements from the additional work in the practicals.)
Find the maximum and minimum distance between the agents and print the results"""
for agents_row_a in agents: #for the first agent
    for agents_row_b in agents: #for the second agent
        if agents_row_a != agents_row_b and agents_row_a.getx() <= agents_row_b.getx(): #prevent same list position and going backwards in list position
            print_distance = agentframework.Agent.distance_between(agents_row_a, agents_row_b) #create vaireable using distance_between method
            distance_list.append(print_distance) #append distance values to a list
            #print("The distances are " + str(print_distance)) #Test print

maximum_distance = max(distance_list) #get max and min values from the distance_list
minimum_distance = min(distance_list)

print("Maximum Distance is " + str(maximum_distance)) #print max and min values from the distance_list
print("Minimum Distance is " + str(minimum_distance))

"""Write the output envoronment as a text file, using the csv writer function.
Open the blank environment_output.txt file and call the csv.writer function
with the delimiter as a comma. Iterate and write through each row in environment
then close the textfile. (Please note the writin text file is in float format,
which is not optimal as it includes a .0 after each value which uses unessesay
space. Did not figure out how to convert the values to int)."""
write_environment = open('environment_output.txt', 'w', newline='') #open write_environment
writer = csv.writer(write_environment, delimiter=',') #use csv writer
for row in environment: #call the rows in environment
    writer.writerow(row) #write the row values in the text file
write_environment.close() #close write_environment

"""Write the stored values as a text file using the write function, opening as
'a' to write and append the values. Open the blank stored_values.txt. Iterate 
through the number_of_agents and write the store value and a comma deliniation.
Write a new line after each session to begin the new append on a new line, then 
close the stored_values.txt."""
write_store = open('stored_values.txt', 'a') #open stored_values with an append function
for row in range(number_of_agents): #for each agent
    write_store.write(str(agents[row].getstore()) + ", ") #write the score comma seperated
write_store.write("\n") #start newline for next append
write_store.close() #close stored_values

"""End and print the timer for the code"""
end = time.process_time()
print("time = " + str(end - start))




"""Redundant Code (Archived code as the model has eveloved and stored below 
the live code to provide a record of changes)"""

"""Create a function to run the pythagorus' theorum code on a pair of agents.
The x and y coordinates are taken from the agentframework module. (Now Redundnat -
instead called as a method in the agentsframework module).
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.getx() - agents_row_b.getx())**2) + 
            ((agents_row_a.gety() - agents_row_b.gety())**2))**0.5"""
    
"""Create a graph to check the in.txt environment 2D list diplays properly. 
(Now Redundant - both graphs environment and agents are displayed within the
 same graph)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()"""
    
"""Prints the maximum coordinate from the agents, using the operator.itemgetter
function to choose the second (or easterly) variable in each column in the list
(Now Redundant - Unfortuantely could not figure out how to continue the print most
 easterly funtion after importing from the agentframework module as the list
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