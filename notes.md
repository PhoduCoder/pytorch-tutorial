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


## Essential core philosphy of Machine learning is below 

[ Gamble -> Reflect on outcome -> Adjust your bets ]

loop over the above, till you win .

Finally with the bets that made you win, do other gamble 

## Maths behind Neural Network - Universal Approximation Theorem

##Also the perceptron convergence theorem - which can be considered as a prelude to the above 
