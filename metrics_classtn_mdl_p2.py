x=[2,4,6,8]
y=[3,7,5,10]

n=len(x)

sum_x=sum(x)
sum_y=sum(y)
sum_x2 = sum(i**2 for i in x)
sum_xy = sum(x[i] * y[i] for i in range(n))

b=(n*sum_xy - sum_x * sum_y)/ (n*sum_x2 - sum_x**2)

a=(sum_y* sum_x2 -sum_x*sum_xy)/ (n*sum_x2 - sum_x**2)

print ("sum X = ", sum_x)
print ("sum Y = ", sum_y)
print ("sum X^2 = ", sum_x2)
print ("sum XY = ", sum_xy)

print("\nSlope (b) =", b)
print("\Intercept (a) =", a)

print("\nLinear regression equation:")
print("Y =", round(a,2),"+", round(b,2), "x")

y_pred = []

for value in x:
    prediction = a + b * value
    y_pred.append(prediction)

print("\predicted Y values:")

for i in range(n):
    print("x=",x[i], "actual Y =", y[i],
          "predicted Y=",round(y_pred[i],2))