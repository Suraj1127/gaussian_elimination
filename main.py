import numpy as np 
from input_module import Input 
from solve import Solve


def main():
	# Getting input from user
	input_class = Input()
	input_class.get_input()

	# Solving the system of linear equations got from the user
	solve = Solve(input_class.coefficient_matrix, input_class.rhs_vector)
	solve.solve()
	print("\nThe solution array is: {}".format(solve.solution_matrix[:,0]))

if __name__ == "__main__":
	main()