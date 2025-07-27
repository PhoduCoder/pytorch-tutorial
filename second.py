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
  print("Note that below we are using torch.tensor, small type which is a factory function and that does accept dtype as an argument, also device as an argument, CPU/GPU\n")
  print("===On the other hand, the legacy torch.Tensor is a constructor and doesn't let you pass these=====\n")
  n4 = torch.tensor([[2,3],[4,5]],dtype=torch.int64)
  describe(n4)

if __name__ == "__main__":
  main()
  
