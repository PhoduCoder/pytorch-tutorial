To map any real number to a value between 0 and 1, you need a function that:

Accepts any input from −∞ to +∞,
Squashes that input into the range (0, 1),
Is smooth and monotonically increasing (bigger input → bigger output).

The answer is sigmoid function

f(x) = 1/(1+e^-x)

If x is large and positive, e^-x becomes close to 0, so f(x) ~=1
If x is small 

```
If 
𝑥
x is large and positive → 
𝑒
−
𝑥
≈
0
e 
−x
 ≈0 → 
𝜎
(
𝑥
)
≈
1
σ(x)≈1
If 
𝑥
=
0
x=0 → 
𝑒
−
𝑥
=
1
e 
−x
 =1 → 
𝜎
(
0
)
=
0.5
σ(0)=0.5
If 
𝑥
x is large and negative → 
𝑒
−
𝑥
≫
1
e 
−x
 ≫1 → 
𝜎
(
𝑥
)
≈
0
σ(x)≈0If 
𝑥
x is large and positive → 
𝑒
−
𝑥
≈
0
e 
−x
 ≈0 → 
𝜎
(
𝑥
)
≈
1
σ(x)≈1
If 
𝑥
=
0
x=0 → 
𝑒
−
𝑥
=
1
e 
−x
 =1 → 
𝜎
(
0
)
=
0.5
σ(0)=0.5
If 
𝑥
x is large and negative → 
𝑒
−
𝑥
≫
1
e 
−x
 ≫1 → 
𝜎
(
𝑥
)
≈
0
σ(x)≈0
```