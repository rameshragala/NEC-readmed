# -*- coding: utf-8 -*-
"""GPU_CUDA_Example.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p3nItdEgEhXy4CkEfdG5VRXgPnazdV-a
"""

import torch
import numpy as np
import sys
import matplotlib as plt

t = torch.tensor([1,2,3], device='cpu',requires_grad=False,dtype=torch.float32)
print(t.dtype)
print(t.device)
print(t.requires_grad)
t2 = t.to(torch.device('cuda'))
t3 = t.cuda() # another one shortcut
t4 = t.cpu()
print(t2)
print(t3)
print(t4)

