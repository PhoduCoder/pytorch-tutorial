import torch

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
  y = torch.rand(2,3) #Uniform distribution
  describe(y) 
  print ("============")
  z = torch.randn(2,3) #Random distribution
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


if __name__ == "__main__":
  main() 
