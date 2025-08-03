###Notes about perceptron 

Perceptron takes any number of inputs, associates weights with those inputs
Then does a dot product of weights and inputs (Linear operation since it is only addition and multiplication)

Then passes it to an activation function, which is the non linear component to produce y

Also pass a bias and weight to bias

So essentially the equation of perceptron becomes 

y = sgn(wT.x+w0.b)
wT= transpose vector of all the weights 
x = input vector 
w0= weight of the bias(which is also adjusted)
b=bias
sgn=Non linear function also referred to as activation function

Since w0 and b are both constants, it is reduced to just one constant and hence the equation for perceptron becomes

y = sgn(wT.x + w0)
wT.x = DOT PRODUCT OF A VECTOR CONTAINING THE INPUTS AND THE VECTOR CONTAINING THE WEIGHTS

===BIAS NOTES===
Remember that the bias or the intercept is introduced by an example
where we want to create a line that separates points of the XY plane, without bias
the line separating the points has to pass through the origin

While adding a bias helps you to choose any other line 
not necessarily passing through the origin 

=====
ONE can use PERCEPTRON AND MORE BROADLY DEEP LEARNING 
FOR CATEGORICAL/DISCRETE OR CONTINOUS PREDICTIONS

AS an example, if the image is cat or dog is a categorical prediction 
while a model which guess the temperature of the following day is a continuos prediction 
=====
The maths behind the categorical vs continous prediction changes slightly 
in terms of the activation function one uses 
=====
WHY ONLY LINE[HYPERPLANE] USED TO SEPARATE THE FEATURE SPACE?
WHY NOT CURVES OR OTHERS CURVEDPLANES? => IT CAN BE 
====

2d vector space

Cuts the feature space into decision boundaries 

====
ACTIVATION FUNCTION

It is the non linear component. It takes the linear part and applies a non linear function to produce the output. 

Most activation functions falls in one of the three categories
a) Sigmoid 
b) ReLu
c) Hyperbolic tangent 

Sigmoid functions are generally used at the last output layer
while relu and hyperbolic tangents are used for inside layer

====
Loss function 
is either MSME[Mean squared error] [Used for continuous problems] like predicting price of home, predicting 
the height 

For classification problems, loss function is cross entropy (logistic) loss

For each given sample, we find out how far the prediction is from the actual value
Then we calculate the individual loss using either of the two loss functions

Loss(Continous) = 1/2(y'-y)^2 

Loss (Classification) = -(ylog(y')+(1-y)log(1-y'))
====
Cost function is average of losses for all samples, i.e. we calculate the losses 
for each sample and then average over the losses

Sometimes, averaging may not be a great idea especially when we have a sensitive datasets
i.e. many outliers in that loss sample may hide that effect

For that reason, you will see losses to be calculated in batches of samples

So say for 1000 samples, instead of calculating average loss for entire sample
we would calculate the loss per batch of samples (say 50 samples)
======