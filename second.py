import torch 

def describe(x):
  print("The type of tensor is", x.dtype)
  print("The size of tensor is", x.size)
  print("The values are", x)


def main():
  n1 = torch.FloatTensor([2,3])
  describe(n1)
  print("============")
  n2 = torch.LongTensor([2,2])
  describe(n2)
  print("===========")
  n3 = torch.DoubleTensor([2,3])
  describe(n3)
  print("==========")

if __name__ == "__main__":
  main()
  
