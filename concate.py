import numpy as np

# Load the numpy arrays
array1 = np.load('array1.npy')
array2 = np.load('array2.npy')
array3 = np.load('array3.npy')
array4 = np.load('array4.npy')

# Print the shapes of the arrays
for i in range(1, 5):
    exec(f"print('Shape of array{i}:', array{i}.shape)")

# Concatenate the arrays along the first axis (adjust axis as needed)
concatenated_array = np.concatenate((array1, array2, array3, array4), axis=0)

# Save the concatenated array to a new file
np.save('concatenated_array.npy', concatenated_array)

print("Arrays concatenated and saved as 'concatenated_array.npy'")