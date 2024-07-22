import numpy as np

# Length of the vector
def compute_vector_length(vector):
    len_of_vector = np.linalg.norm(vector)
    return len_of_vector

vector = np.array([3, 4])
print("Length of the vector:", compute_vector_length(vector))

# Dot product
def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)
    return result

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
print("Dot product:", compute_dot_product(vector1, vector2))

# Multiplying a vector by a matrix
def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result

matrix = np.array([[1, 2], [3, 4]])
vector = np.array([5, 6])
print("Matrix multiplied by vector:", matrix_multi_vector(matrix, vector))

# Multiplying a matrix by a matrix
def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
print("Matrix multiplied by matrix:", matrix_multi_matrix(matrix1, matrix2))

# Matrix inverse
def inverse_matrix(matrix):
    result = np.linalg.inv(matrix)
    return result

matrix = np.array([[-2, 6], [8, -4]])
print("Matrix inverse:", inverse_matrix(matrix))

# Eigenvalues and eigenvectors
def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

matrix = np.array([[0.9, 0.2], [0.1, 0.8]])
eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)

# Cosine Similarity
def compute_cosine(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    cos_sim = dot_product / (norm_v1 * norm_v2)
    return cos_sim

v1 = np.array([1, 2, 3, 4])
v2 = np.array([1, 0, 3, 0])
print("Cosine Similarity:", compute_cosine(v1, v2))
