# Store walk to bus stop (15 mins) in variable a
a = 15
# Store bus journey (1 hr 15 mins = 75 mins) in variable b
b = 75
# Calculate total bus commute time (a + b) and store in c
c = a + b
# Store drive time (1 hr 30 mins = 90 mins) in variable d
d = 90
# Store walk from car park (5 mins) in variable e
e = 5
# Calculate total car commute time (d + e) and store in f
f = d + e
# Compare c and f to determine which commute is quicker
# c = 90 mins (bus), f = 95 mins (car), so bus is quicker
print("Bus commute time (c):", c, "minutes")
print("Car commute time (f):", f, "minutes")
print("Bus is quicker than car:", "c < f")
#It's strange that the guidance requires us to compare c and e.
print( "c = 90, e = 5, c > e" )
# Comment: The bus commute (90 minutes) is quicker than the car commute (95 minutes).

X = True
Y = False
W = X and Y
print("X:", X, "Y:", Y, "W (X and Y):", W)
# Truth table for W (X and Y):
# X     Y     W
# T     T     T
# T     F     F
# F     T     F
# F     F     F