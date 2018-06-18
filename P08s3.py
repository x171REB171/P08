# St. apl: 171REB171
g = 9.81
v0 = (1+1)*10
f = open('P08s3.dat','w')
for t in range(1+10):
    y = v0*t-(g*t**2)/2
    string = str(t)+' '+str(y)
    print(string)
    f.write(string+'\n')

from numpy import linspace, array
t = linspace(0,1+10,12)
y = v0*t-(g*t**2)/2

from matplotlib import pyplot as p
p.plot(t,y,color="#ff00ff",label="bumbas pozicija")
p.legend()
p.show()
