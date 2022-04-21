# GEOG5003 Assignment 1 2022 StudID - 201465981.github.io
 Assignment 1 Portfolio for Programming for Geographical Information Analysis Module


The aim of this README documentation is to familiarise the user with the contents of the GitHub
repository and to describe what the software is and how to run it. 


The contents for the GitHub repository (reading from top to bottom) are as follows:-
- __pycache__ - a sub-repository containing some auto-created cached files.
- backup_flies_sub_repository - a sub-repository containing the backup files created from working through
the practical elements of the course.
- .gitattributes - a file auto-created when setting up the github repository.
- LICENSE - the license file stipulates the open source licence for the code
- README.md - this document, provides initial instructions and overview for user orientation
- _config.yml - the file to set the theme for the landing page, the chosen theme was a Jekyll Slate theme.
- agentframework.py - this is the bespoke module code which links to the model.py code.
- environment_output.txt - this is the output text file which is written after the data changes have taken effect from running the code.
- in.txt - this is the input text file which reads the initial environment into the model.
- index.md - the file which provides the text in the landing page.
- model.py - the main python file code which runs the agent model.
- stored_values,txt - the output text file which is written from the stored values from the agents after running the model.


A brief description of the agent model:-
- The model creates a number of agents which have several effects on the input environment, in order
  to eat away at the environment and store the eaten properties. 

- The environment file is read into the model, which contains 300 pixels worth of data.
- The input parameters are created - number_of_agents effects the agents made, 
  number_of_iterations affects the amount of actions each agent takes, and neighbourhood
  affects the sharing search distance of the agents in pixels.
- The blank agents list is created and populated using random XY coordinates within the 
  environment from the __init__ method in the agentsframework module, using the number_of_agents
  input parameter.
- Calls several methods from the agentsframework module to affect the environment using the agents
  by the number_of_iterations. The move method changes the agents coordinates in small steps. The 
  eat method scoops up 10 values from the agents' pixel in the environment and stores them. The greedy
  method removes values from the store and back into the environment at the agents' pixel when a defined
  limit has been reached. The share_with_neighbours method allows the agents to split their stores if 
  within the neighbourhood parameter distance.
- The maximum and minimum distances are calculated and printed.
- An animation of the environment is created and displayed, plotting the agents and showing the effects of
  their actions over a number of iterations.
- The output environment and store text files are written in the directory.


To run the model use the instructions below:-
- Create a local directory.
- Download and save the following files from the github repository and into the directory, 
  model.py, agentframework.py, in.txt.
- Either download the files from the repository, or as a better option create two blank text files in the
  directory named 'environment_output.txt' and 'stored_values.txt'.
- Open a cmd prompt on the system.
- Navigate to the local directory in the cmd prompt using the cd function.
- Type model.py and the input parameters in the cmd, there are three parameters and the entered value
  must be a whole number. They must be entered in the following order and separated by a space, number_of_agents,
  number_of_iterations and neighbourhood. An example user input method is 'agent.py 10 20 30'.
- Hit the enter key, to run the model and get the results.

- Please note the matplotlib module may not be available to run on cmd as standard, if this error is 
  encountered then there is a useful troubleshooting guide which can be accessed [here](https://pythonguides.com/no-module-named-matplotlib/#:~:text=the%20above%20topics.-,modulenotfounderror%3A%20no%20module%20named%20'matplotlib'%20pycharm,most%20probably%20it%20will%20work.)
  

The expected output after running the model:-
- Within the cmd the following data will be printed:- 
    - a line for each time a sharing action took place between the agents (this may be blank if no sharing took place)
	- the final coordinate values and sharing values for each agent.
	- the maximum and minimum distance between the agents.
	- the time in seconds it took for the model to run.
- A popup animation will display which contains the environment which has been actioned by the agents,
  and also display the final stopping place of the agents, this may loop through a number of frames
  depending on the random generator.
- The environment_output.txt file will be populated with the amended environment data.
- The stored_values.txt file will be populated with the data (this will not clear after each model runthrough).

- Please note the user may print additional lines of data when running the model if required, 
  which were used during the model testing. These have been blanked out in the model.py code,
  however the user may remove the # where appropriate. 