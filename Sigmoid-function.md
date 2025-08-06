To map any real number to a value between 0 and 1, you need a function that:

Accepts any input from −∞ to +∞,
Squashes that input into the range (0, 1),
Is smooth and monotonically increasing (bigger input → bigger output).

The answer is sigmoid function

f(x) = 1/(1+e^-x)

If x is large and positive, e^-x becomes close to 0, so f(x) ~=1
If x is large and negative, e^-x becomes >>1, so f(x) ~=0
If x=0, then f(x)=0.5

This gives the classic S-curve, where small/large values asymptotically approach 0 and 1 but never reach them.

In binary classification (e.g., spam vs. not spam), the model outputs a real number (logit). But we want a probability — a value between 0 and 1 that says how likely a sample belongs to class 1.

The sigmoid converts the logit (raw model score) to a probability:

If f(x)=0.9, high confidence it's class 1.
If f(x)=0.1, high confidence it's class 0.
If f(x)=0.5, model is unsure