##Exercise5  Chapter1.1 The velocity of a freely falling object near Earth's surface.
##Abstact 
This program is to employ the Euler method to compute the solution that calculates v as a function of t.
##Process
First of all, Create two empty list to store the speed of each moment（v） and each time（t）, after the initialization of t0 and give the earth's surface gravity acceleration g.Then allowing the user to enter the t_end (representing the end time), dt (representing the time interval for each calculation), v0 (representing the initial speed).
Add the results of each calculation to the list that you created earlier.
##Result
Here is the program for Python
```python
# This program caculates the velocity of a freely falling object near 
# Earth's surface employing the Euler method.

from pylab import *

v=[] #establish list v
t=[] #establish list t
g=9.8
t0=0  #initialize t0
t_end=float(raw_input('please input the end time:'))  #input the end time
dt=float(raw_input('please input the time interval:'))   #input the time interval
v0=float(raw_input('please input the initial velocity:'))  #input the initial velocity v0
t.append(t0)
v.append(v0)
for i in range(int(t_end/dt)):
    v.append(v[i]+g*dt)
    i=i+1
    t.append(i*dt)
print t
print v
plot(t, v, 'bo', color='red', linewidth=1.0, linestyle='--', label='v=v0+gt')
title('v vs t')
xlabel('time axis')
ylabel('velocity axis')
legend(loc='upper left')
show()
```

