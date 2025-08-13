import torch
import numpy as np

def describe(x):
  print ("The type of tensor is", x.dtype)
  print ("The shape of tensor is", x.shape)
  print ("The size of tensor is", x.device, x.size())
  print ("The dimensions of tensor is", x.dim(), type(x.dim()))
  print("Values in tensor are", x)
  print ("=================\n")

def main():
  print("Enter the type of tensor\n")
  x = torch.Tensor(2,3) #Declare a tensor with zero values, note that default type is float32
  describe(x)
  print ("============")
  y = torch.rand(2,3) #Uniform distribution in [0,1). All outcomes equally likely 
  describe(y) 
  print ("============")
  z = torch.randn(2,3) #Normal distribution with mean 0 and standard deviation as 1, sd-> how spread out values are 
  #Normal distribution above would result in a bell curve, i.e. most values are near mean, i.e. 0, while
  #some values are at extremes
  describe(z)
  print ("==============")
  a = torch.zeros(2,3) #Initialize tensor with all zeroes
  describe(a)
  print ("==========")
  b = torch.ones(2,3)
  describe(b)
  print ("========")
  c = b.fill_(8)
  describe(c)
  print ("========")
  d = torch.Tensor([[1,2],[3,4]])
  describe(d)
  print ("========")
  print("Now converting numPy arrays to tensor")
  npy = np.random.rand(2,3)
  e = torch.from_numpy(npy)
  describe(e)
  print("========")

if __name__ == "__main__":
  main() 
