# Vector Code

'''Basic Operations on Vectors'''

import numpy as  np
A=np.array([1,2,3])
B=np.array([5,4,6])

print(" Vector A : ",A)
print(" Vector B : ",B)
print("Addition of Vector :",A+B)
print("Subtraction of Vector :",A-B)
print("Dot Product : ",np.dot(A,B))
print("Cross Product : ",np.cross(A,B))
print("Magnitude of A : ",np.linalg.norm(A))

'''Calculation of Angle'''

import numpy as np
# Define two vectors
A = np . array ([1 , 2 , 3])
B = np . array ([4 , 5 , 6])
# Calculate dot product
dot_product = np . dot (A , B )
# Calculate magnitudes of the vectors
magnitude_A = np . linalg . norm ( A )
magnitude_B = np . linalg . norm ( B )
# Calculate the cosine of the angle
cos_theta = dot_product / ( magnitude_A * magnitude_B )
# Calculate the angle in radians
angle_radians = np . arccos ( cos_theta )
# Convert the angle to degrees ( optional )
angle_degrees = np . degrees ( angle_radians )
print ("Dot Product :", dot_product )
print (" Magnitude of A:", magnitude_A )
print (" Magnitude of B:", magnitude_B )
print (" Cosine of the angle :", cos_theta )
print (" Angle in radians :", angle_radians )
print (" Angle in degrees :", angle_degrees )

'''Vector and Scalar Triple Product'''

import numpy as np
# Define three vectors
A = np . array ([1 , 2 , 3])
B = np . array ([4 , 5 , 6])
C = np . array ([7 , 8 , 9])
# Vector Triple Product : A x (B x C)
# First compute the cross product B x C
cross_product_BC = np . cross (B , C )
# Then compute A x (B x C)
vector_triple_product = np . cross (A , cross_product_BC )
# Scalar Triple Product : A . (B x C)
scalar_triple_product = np . dot (A , cross_product_BC )
print (" Vector Triple Product (A x (B x C)):",vector_triple_product )
print (" Scalar Triple Product (A . (B x C)):",scalar_triple_product )




