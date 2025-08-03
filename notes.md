FloatTensor -> float32 numbers 

LongTensor -> int64 numbers

DoubleTensor -> float64 number

```
d = torch.Tensor([2,3]) #Constructor, legacy, doesn't accept arguments like dtype, device etc)
d1 = torch.Tensor(2,3) #Constructor
d2 = torch.tensor([[2,3],[4,5]], dtype=torch.int64)
```
=====
Note that below we are using torch.tensor, small type which is a factory function and that does accept dtype as an argument, also device as an argument, CPU/GPU

===On the other hand, the legacy torch.Tensor is a constructor and doesn't let you pass these=====


===============TENSOR OPERATIONS NOTES========


