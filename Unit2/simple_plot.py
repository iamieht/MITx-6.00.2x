import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)


# Plot mySamples (X values) and myXXXX (Y values)
# Linear Plot
plt.figure('lin')
plt.clf()                       # Clear any previously open Figure
plt.title('Linear') 
plt.xlabel('sample points')   
plt.ylabel('linear function')
plt.plot(mySamples, myLinear)

# Quadratic Plot
plt.figure('quad')
plt.clf()                       # Clear any previously open Figure
plt.title('Quadratic')
plt.xlabel('sample points')   
plt.ylabel('quadratic function')
plt.plot(mySamples, myQuadratic)

# Cubic Plot
plt.figure('cube')
plt.clf()                       # Clear any previously open Figure
plt.title('Cubic')
plt.xlabel('sample points')   
plt.ylabel('cubic function')
plt.plot(mySamples, myCubic)

# Exponencial Plot
plt.figure('expo')
plt.clf()                       # Clear any previously open Figure
plt.title('Exponential')
plt.xlabel('sample points')   
plt.ylabel('exponential function')
plt.plot(mySamples, myExponential)

# Display the plots
plt.show()