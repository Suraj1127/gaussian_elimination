#!/usr/bin/python3
# module to take in input

import numpy as np 

class Input:
	def __init__(self):
		'''
			Initialize coefficient matrix and rhs-vector to zero matrices
		'''
		self.degree = int(input("Enter the degree of the equations:\n"))
		self.coefficient_matrix = np.zeros((self.degree,self.degree))
		self.rhs_vector = np.zeros((self.degree,1))

	def get_coefficients_matrix(self):
		'''
			Get coefficient matrix from user
		'''
		print("\nEnter the coefficient matrix of the equations:")
		print("\'\'\'")
		print("\tFormat:")
		print("\tFor degree of 2, the sample coefficient matrix becomes:")
		print("\t1 2")
		print("\t4 5")
		print("\'\'\'")

		for i in range(self.degree):
			self.coefficient_matrix[i] = [int(j) for j in input().split()]

	def get_rhs_vector(self):
		'''
			Get rhs-vector from user
		'''
		print("\nEnter the RHS column vector separated by spaces.")
		print("\'\'\'")
		print("\tFormat for degree of 2:")
		print("\t10 12")
		print("\'\'\'")

		self.rhs_vector = np.array([int(j) for j in input().split()]).reshape(self.degree,1)

	def get_input(self):
		'''
			Get everything input from above functions
		'''
		self.get_coefficients_matrix()
		self.get_rhs_vector()

def main():
	input_class = Input()
	input_class.get_input()

	print(input_class.coefficient_matrix)
	print(input_class.rhs_vector)

if __name__ == "__main__":
	main()