'''
Author: Niall Naughton
Date: 26/03/2025
----------------------------------------------------------------------------------
Task Description:
Write a program called plottask.py that displays:
a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
and a plot of the function  h(x)=x3 in the range 0 to 10, 
on the one set of axes.
Some marks will be given for making the plot look nice (legend etc).
Please put a copy of the image of the plot (.png file) into the repository
----------------------------------------------------------------------------------
Approach:
Use the numpy.random.normal function to generate 1000 random values with a normal distribution (mean = 5, std = 2) 
Populate in a 1-D numpy Array
Use a Dictionary to store x,y values for H(x) = x3 plot (x-key, y= value)
Use latex for Displaying Mathematically Formatted Text (i.e. x**3) in Labels and Legend
Break up code into a series of function calls Extract Data & Plot data
Plot 2 graphs in a 2x1 grid

https://numpy.org/doc/2.1/reference/random/generated/numpy.random.normal.html
https://en.wikipedia.org/wiki/LaTeX#:~:text=The%20LaTeX%20system%20is%20a,as%20new%20environments%20and%20commands.
https://matplotlib.org/stable/users/explain/text/mathtext.html
'''

#import required modules 
import numpy as np
import matplotlib.pyplot as plt

#Generate the Normal Random Distribution of 1000 Values
def generateNormalDist():
    mean = 5
    std = 2
    numValues = 1000
    mydata = np.random.normal(loc=mean, scale=std, size=numValues)
    return mydata

#Generate the Dictionary of 10 Values in H(x) = x**3
def generateExponentialData():
    numValues = 10
    dictValues = {}
    for x in range(1, numValues + 1):
        dictValues[x] = x**3
    return dictValues



#Plot Histogram of 1000 values with 20 bins
def plotHisto(data):
    plt.hist(data, bins=20, edgecolor='black', color='red', label='Normal Distribution')
    plt.title(f' Histogram of Normal Distribution of 1000 Random values', fontsize=14, fontweight='bold') #Use bold text
    plt.xlabel('Value')
    plt.ylabel('Frequency') 
    plt.legend()
    

#Plot line graph of 10 Dictionary values
def plotLine(data):
    # Get Dictionary of values and extract key/value pairs for plot x,y value
    x = list(data.keys())  
    y = list(data.values())  
    # Create the plot
    plt.plot(x, y, marker='o', linestyle='-', color='b', label=r'$x^3$')
    plt.xlabel('x')
    plt.ylabel(r'$x^3$')
    plt.title(r'Plot of Exponential $x^3$', fontsize=14, fontweight='bold')#Use bold text
    plt.legend()
    plt.grid(True)

#Generate data 
norm_data = generateNormalDist()
exp_data = generateExponentialData()

#Plot 2 graphs in a 2x1 grid
plt.figure(figsize=(10, 20), facecolor='ivory') #Adjust size of 2 graphs (width, height) and background color
plt.subplot(2, 1, 1)
plotHisto(norm_data)
plt.subplot(2, 1, 2)
plotLine(exp_data)
plt.show()
