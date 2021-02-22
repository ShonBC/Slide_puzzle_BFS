ENPM 661 - Planning for Autonomous Robots: 
Project 1 - Slide puzzle challange
Shon Cortes

Packages Used:
	1. import copy
		- Used to do deep copy of lists

Run the program:
	To run the program go to line 141 and choose the desired test case to run.
	Update the "test_case =" to be one of the folowing:
		test_case_1, test_case_2, test_case_3, test_case_4, test_case_5
  Update the test case file name on line 142 to match the previously selected test case.

    Example if I want to run test case 1:
    line 140      # Chose initial state from test_case_1 - test_case_5
    line 141      test_case = test_case_1
    line 142      file = open("nodePath" + "_test_case_1" + ".txt", "a")

  The program should create a .txt file labeled with the chosen test case if it doesnt already exist 
  and write the nodes visited in order from initial state to goal state.