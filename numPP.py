import numpy as np
import random 
x=np.random.randint(1,100)
print(x)
print("3 random samples:", random.sample(range(1, 50), 3))
import numpy as np

# 1. Create arrays
arr1 = np.array([1, 2, 3, 4, 5])
print("Array:", arr1)

# 2. Array of zeros and ones
print("Zeros:", np.zeros((2, 3)))
print("Ones:", np.ones((2, 3)))

# 3. Random numbers with numpy
print("Random array (0–1):", np.random.rand())  # 1D
print("Random 2x2 matrix:", np.random.rand(2, 2))

# 4. Arithmetic operations
arr2 = np.array([10, 20, 30, 40, 50])
print("arr1 + arr2:", arr1 + arr2)
print("arr2 - arr1:", arr2 - arr1)
print("arr1 * 2:", arr1 * 2)

# 5. Useful functions
print("Mean of arr2:", np.mean(arr2))
print("Max of arr2:", np.max(arr2))
print("Square root of arr2:", np.sqrt(arr2))

# 6. Random integers with numpy
print("Random integers (1–100):", np.random.randint(1, 101, size=5))
