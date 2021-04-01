# -*- coding: utf-8 -*-
"""torch_numpy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Pf3hd4fqG5t_tWqsjCg1CSK0pHBbEQnS
"""

import torch
import numpy as np
import sys
import matplotlib as plt

print(f'python vesion: {sys.version}')
print(f'Numpy version: {np.version.version}')
print(f'PyTorch version: {torch.version.__version__}')
print("Torch Version", torch.__version__)
print(f'Matplotlib version: {plt.__version__}')
print(f'GPU present: {torch.cuda.is_available()}')

# details about math operation in torch can be found in: http://pytorch.org/docs/torch.html#math-operations

# Example - 10
# convert numpy to tensor or vise versa
np_data = np.arange(6).reshape((2, 3))
print("numpy data", np_data)
torch_data = torch.from_numpy(np_data)
print("Torch Data", torch_data)
tensor2array = torch_data.numpy()
print("Tensor to array data", tensor2array)

# youtube --> https://www.youtube.com/watch?v=c36lUUr864M

import torch
import numpy as np

# Empty Tensor
A = torch.empty(1) # 1 is size
print(A)
# It is a empty tensor, Value is not initilized

# 1 - D Tensor
# Change the size of the tensor
B = torch.empty(5)
# It is a 1-D vector with three elements in it
print(B)

# 2-D Tensor
C = torch.empty(3,3)
# 2-D i.e Matrix with 6 elements i.e 2 rows with 3 elements at each row
print(C)

# 3 - D Tensor
D = torch.empty(2, 2, 3)
# 3-D with 12 elements
print(D)

# 4 - D Tensor
F = torch.empty(2,2,2,3)
print(F)

# Tensor with Random Values
R1 = torch.rand(2,2)
print(R1)

# Same like numpy  in python
R2 = torch.zeros(2,2)
# All elements in the Tensor will be zero's
print(R2)

R3 = torch.ones(2,2)
# All elements in the Tensor will be one's
print(R3)

R3a = torch.eye(3, dtype=torch.double)
print(R3a)

R3b = torch.arange(6)
print(R3b)
R3c = torch.arange(6, dtype=torch.double)
print(R3c)

# Tensor from data  --> Check the size of this tensor later stage
R3A = torch.tensor([2.4, 3.9])
print(R3A)
print(R3A.size())

R3B = torch.tensor([[2.4, 3.9, 10],[1.8, 10.2, 10], [10.21, 22.12, 10]])
print(R3B)
print(R3B.size())

# Checking the Data type of the Tensor elements
R4 = torch.ones(3,3)
print(R4)
print(R4.dtype) # by default float32

# Tensor based on customized data type  --> use int and float16  --> Check output
R5 = torch.ones(2,3, dtype=torch.float16)
print(R5)
print(R5.dtype)

# Size of a Tensor object --> returns a torch.Size object
R6 = torch.ones(2,3,4, dtype=torch.float16)
print(R6)
print(R6.size())

# Basic Operations in Tensor
# Element-wise Additions
R7 = torch.rand(2,3)
R8 = torch.rand(2,3)
print(R7)
print(R8)
R9 = R7 + R8
print(R9)
R10 = torch.add(R7, R8)
print(R10)
print(torch.eq(R9, R10)) # Checking element-wise
print(torch.equal(R9, R10)) # Retures true iff all elements in both the tensor are same
print(torch.equal(R7,R8))
R7.add_(R8)

# Element-wise subtraction operation
R11 = R7 - R8
R12 = torch.sub(R7, R8)
print(R11)
print(R12)

# Element-wise multiplication operation
R13 = R7 * R8
R14 = torch.mul(R7, R8)
print(R13)
print(R14)

# Element-wise division operation
R15 = R7 / R8
R16 = torch.div(R7, R8)
print(R15)
print(R16)

# in-place operation in tensor
R17 = torch.tensor([1,2])
R18 = torch.tensor([10,11])
print(R17)
print(R18)
R18.add_(R17)
print(R18)

# Example - 104
# slicing operations in Tensor
R19 = torch.rand(5,3)
print(R19)
# All elements (row data) in one column
print(R19[:,0]) # here 0 specifies the first column index

# Examples
print(R19[:,1]) # Check output
print(R19[:, 2]) # Check output
print(R19[:, 3]) # Chcek output

# All elements (column data) in one row
print(R19[0, :]) # Here 0 specifes the first row index

print(R19[1, :]) # check output
print(R19[2, :]) # check output

print(R19[1,1]) # The element at 1,1 location
print(R19[1,1].item()) # The actual value of the element in tensor. It has to use for single element in tensor

# Reshaping a Tensor
R20 = torch.rand(4,4)
print(R20)
R21 = R20.view(16) # a tensor to be a View of an existing tensor. View tensor shares the same underlying data with its base tensor.
# avoids explicit data copy.  
print(R21) # 1 D vector with 16 elements
print(R21.size())
R22 = R20.view(-1, 8) # -1, it takes no of rows (here) automatically
print(R22) # 2 D
print(R22.size())

# Example - 101
R23 = torch.arange(6)
print(R23)
R26 = R23.reshape(2,3) # or R23.view(2,3) or R23.view(2,-1)
R27 = R23.reshape(2,3).unsqueeze(1) #unsqueeze --> Returns a new tensor with a dimension of size one inserted at the specified position
R28 = R23.reshape(2,3).unsqueeze(1).shape
print(R26)
print(R27)
print(R28)

# Example - 106
R29 = torch.empty(5,1,4,1, dtype=torch.int16)
R30 = torch.empty( 3,1,1, dtype=torch.int16)
print(R29)
print(R30)
R31 = R29 + R30
print(R31)
print(R31.size())
(R29+R30).size()

R31 = torch.empty(1)
R32 = torch.empty(3,1,7)
(R31+R32).size()

R33 = torch.empty(5,2,4,1)
R34 = torch.empty(3,1,1)
(R33+R34).size()

# Example - 107
R35 = np.arange(6)
R36 = torch.from_numpy(R35)
print(R35)
print(R36)
R36[2]=11
print(R36)
print(R35) #Changed the underlying numpy array too!

R37 = R35.copy()
R38 = R36.clone()
print(R37)
print(R38)
R38[0] = 13
print(R38)
print(R36)

# Example - 108
R39 = torch.eye(2)
print(R39)

