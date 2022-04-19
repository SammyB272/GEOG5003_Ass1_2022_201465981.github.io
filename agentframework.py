# -*- coding: utf-8 -*-
"""
Title: agentframework.py
Created on Mon Apr 11 15:15:07 2022
Version: 1
Author: Student ID - 201465981

This code exists as a bespole module which is to be imported into the model.py 
code. It contains one object called Agent, which has an __init__ method and 
various additional methods for the model. It also takes in the environment and 
agents variables from model.py, to use in some of the methods.
"""


"""Imports the following modules to be used in the code - random"""
import random


"""Create a Class called Agent and define the class with the init function 
and the parameter label as self. Create a self.x and self.y label randomised 
betweent the ingegers 0 and 99. Create a self.environment label to take in the 
environments list created in the model.py and enbed it into the Agent object.Create
a self.store label to store 'eaten' values.

The get() method is used to only retrieve the __init__ data without being able to
change the values. The set() method allows the user to chnage the value of the 
object different to that assigned from __init__. 

The distance_between() method calcualted the straight line distance from and to
the agents using pythagorus' theorum. 

The move() method is created to move the agent class a place along the X and Y
axis every time. Tarus code used to prevent spillage outside of the chart.

The eat() method makes the agents eat what is in the environment, if there are
over 10 units in the environment, it takes 10 away from the environment and 
adds 10 to the store. The elif satement will remove the remaining value from the
envronment if it is under 10 using the modulo function.

The greedy() method returns 20 units beck to the envronment and loses them from
the store after 20 units have been consumed.(Please note that although the 
instruction mentions 100 units, I chose 20 instead to reduce the impact on the
colour ramp scale)

The share_with_neighbours() method which takes in the neighbourhood variable from 
the model.py. The method loops through the agents in self.agent and for each
iteration calls the distance_between method into a new variable. If the distance 
is closer than the neighbourhood value then calculate the average between the
self._store and the agent._store and distribute them evenly, else return 0.

The check_agent() method selects and agent from the list and prints it's values.

The __str__() method allows a default print return when called in the main code."""

class Agent(): #Create Agent object
    
    def __init__(self, environment, agents): #define the intial data
            self._x = random.randint(0,300) #set x coordinate as random 0-300 (size of environment)
            self._y = random.randint(0,300) #set y coordinate as random 0-300
            self._store = 0 #set store to 0, to be added to later
            self.environment = environment #set environment as the variable value
            self.agents = agents #set agents as the variable value
    
    #get method for x, y and store, returns its own value
    def getx(self):
        return self._x
    def gety(self):
        return self._y
    def getstore(self):
        return self._store
    
    #set method for x, y and store, returns input value (commented out as not used)
    #def setx(self, value):
    #    self._x = value
    #def sety(self, value):
    #    self._y = value
    #def setstore(self, value):
    #    self._store = value

    def distance_between(self, agent):  #take in self and agent values
        return (((self.getx() - agent.getx())**2) + 
                ((self.gety() - agent.gety())**2))**0.5 #return pythagorus' therum on two agents' XY values
    
    def move(self): #move method
        if random.random() < 0.5: #to get 50% chance
            self._y = (self._y + 1) % 300 #moves agent one place up (goes to bottom at top)
        else: #to get remaining 50% chance
            self._y = (self._y - 1) % 300 #moves agent one place down
        
        if random.random() < 0.5: #to get 50% chance
            self._x = (self._x + 1) % 300 #moves agent one place left
        else: #to get remaining 50% chance
            self._x = (self._x - 1) % 300 #moves agent one place right
    
    def eat(self): #eat method
        if self.environment[self._y][self._x] > 10: #if the environment value is over 10
            self.environment[self._y][self._x] -=10 #remove 10 off environment value
            self._store +=10 #add 10 to store
        elif self.environment[self._y][self._x] < 10: #if environment value under 10
            self.environment[self._y][self._x] -=self.environment % 10 #remove remainder value
            
    def greedy(self): #greedy method
        if self._store > 20: #if store is over 20 for agent
            self.environment[self._y][self._x] +=20 #add 20 to environment
            self._store -=20 #take 20 from store
    
    def share_with_neighbours(self, neighbourhood, agents): #take in self and neighbourhood values
        for agent in self.agents: #make variable iterating through agents
            distance = self.distance_between(agent) #make distance variable
            if distance != 0 and distance <= neighbourhood: #if distance is within neighbourhood but not 0
                    share = (self.getstore() + agent.getstore()) / 2 #add the stores and divide by 2
                    self._store = share #share the store values between the two agents
                    agent._store = share
            else: 
                share = 0 #else to give value of 0 if not shared
        if share > 0: #only print is value is over 0 to reduce redundant print lines     
            print("The distance between the agents is " + str(distance) + 
                    " the sharing value is " + str(share)) #prints string, distance and share values
    
    #check_agent method (commented out as used for test)
    #def check_agent(self): 
    #    check = self.agents[2] #make variable from the item 2 in agents list
    #    print("This is the agent check, " + str(check)) print check vale
        
    def __str__(self): #__str__ method
        return("The XY Coordinate is " + str(self._x) + " " + str(self._y) + 
               ", The store value is " + str(self._store)) #returns string, XY and store values