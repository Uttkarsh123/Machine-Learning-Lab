#Linear Regression

x = [0,1,2,3,3,5,5,5,6,7,7,10]
y = [96,85,82,74,95,65,76,84,58,65,75,50]

n=len(x)
summation_x = sum(x)
summation_x_squared = summation_x **2
summation_y = sum(y)

sum_xy=0
summ_x_square=0

for i in range(n):
    sum_xy = sum_xy + (x[i]*y[i])
    summ_x_square += x[i]**2


m = float(format((((n*sum_xy) - (summation_x*summation_y))/((n*summ_x_square) - summation_x_squared)),".2f"))
print(m)

y_mean = float(format(summation_y/n,".2f"))
x_mean = float(format(summation_x/n,".2f"))

print(y_mean)
print(x_mean)

intercept = y_mean - (m*x_mean)

hours = float(input("Enter number of hours you watched tv :"))
value_y = m*hours + intercept
print(f"You will get {value_y} marks by studying {hours} hours")