Uniform Distribution : Evvery outcome is equally likely [Rolling of a dice]

Random Distribution : Outcome are produced by a random process and the probabilities of each outcome
can be unequal. 

Random → generic term: any distribution where outcomes are unpredictable. Could be uniform, normal, exponential, etc. “Random” alone doesn’t tell you the shape or probabilities.

Uniform distribution → special case of random where all outcomes in the range are equally likely. Example: torch.rand() → values between 0 and 1, flat probability.

Normal distribution → specific type of random distribution where values cluster around a mean and extremes are rare (bell curve). Example: torch.randn() → mean = 0, std = 1.

=========

torch.rand(2,3) → draws values from a uniform distribution over [0,1]

All values between 0 and 1 are equally likely.

Used when you want flat, unbiased initialization 

============
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


## Essential core philosphy of Machine learning is below 

[ Gamble -> Reflect on outcome -> Adjust your bets ]

loop over the above, till you win .

Finally with the bets that made you win, do other gamble 

## Maths behind Neural Network - Universal Approximation Theorem

##Also the perceptron convergence theorem - which can be considered as a prelude to the above 
