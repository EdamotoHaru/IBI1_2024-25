# Ask the user for the number of layers in a triangle and calculate the T value
# The T value is the sum of the first n natural numbers, which is given by the formula n(n+1)/2
# Initially, Print the first ten values as examples for n =1, 2, ..., 10
print("For example, the first ten values are:")
for i in range(1, 11):
    print("n =", i, "T value =", int(i*(i+1)/2))
n = int(input('How many layers the triangle has?'))
print("The T value for your triangle is", int(n*(n+1)/2))