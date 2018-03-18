import numpy as np 
import sys

class Solve:
	def __init__(self, coefficient_matrix, rhs_vector):
		'''
			Do the initialization of coef. matrix, rhs-vector, 
			solution-matrix and transformation matrix
		'''
		self.coefficient_matrix = coefficient_matrix
		self.rhs_vector = rhs_vector
		self.degree = rhs_vector.shape[0]
		self.solution_matrix = np.zeros((self.degree,1))
		self.transformation_matrix = np.eye(self.degree)

	def solve(self):
		'''
			Solve the linear system here by elimination
		'''

		for j in range(self.degree):
			pivot = self.coefficient_matrix[j][j]
			
			# In case pivot is equal to 0, exchange the rows
			if pivot == 0:
				for k in range(j+1, self.degree):
					if self.coefficient_matrix[k][j] != 0:
						transformation_matrix_t = np.eye(self.degree)
						status = True
						temp_1 = np.copy(transformation_matrix_t[k])
						temp_2 = np.copy(transformation_matrix_t[j])
						transformation_matrix_t[j] = temp_1
						transformation_matrix_t[k] = temp_2
						self.coefficient_matrix = np.matmul(transformation_matrix_t, self.coefficient_matrix)
						self.transformation_matrix = np.matmul(transformation_matrix_t, self.transformation_matrix)
						break

				
			pivot = self.coefficient_matrix[j][j]

			'''
				If we can't get pivot non-zero number by exchanging the rows, the system
				does not have unique finite solution
			'''
			if pivot == 0:
				print("The system of equations does not have unique and finite solution.")
				sys.exit()

			# Transforms coefficient matrix to upper triangular matrix by doing Gaussian elimination
			# Transformation matrix stores the net transformation the coefficient matrix goes through
			for i in range(j+1,self.degree):
				if self.coefficient_matrix[i][j] == 0:
					continue
				transformation_matrix_t = np.eye(self.degree)
				transformation_matrix_t[i][j] = - self.coefficient_matrix[i][j]/pivot
				self.transformation_matrix = np.matmul(transformation_matrix_t,self.transformation_matrix)
				self.coefficient_matrix = np.matmul(transformation_matrix_t, self.coefficient_matrix)
		
		# Transforming rhs_vector with transformation_matrix
		self.rhs_vector = np.matmul(self.transformation_matrix, self.rhs_vector)

		# Solving for the last variable by doing pivot division
		self.solution_matrix[-1][0] = self.rhs_vector[-1][0]/self.coefficient_matrix[-1][-1]

		# Solving for the rest of the variables
		for i in range(2,self.solution_matrix.shape[0]+1):
			temp = np.copy(self.coefficient_matrix[-i])
			temp[-i] = 0
			temp_product = np.dot(temp, self.solution_matrix[:,0])
			self.solution_matrix[-i][0] = (self.rhs_vector[-i][0]-temp_product)/self.coefficient_matrix[-i][-i]

def main():
	solve = Solve(np.array([[4,2,0],[2,1,0],[5,3,9]]), np.array([[1],[3],[7]]))
	solve.solve()
	print(solve.solution_matrix)


if __name__ == "__main__":
	main()
