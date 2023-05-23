from matplotlib import pyplot 
import numpy 
from textwrap import wrap 
import matplotlib.ticker as ticker 
 
with open('settings_1.txt') as file: 
    settings=[float(i) for i in file.read().split('\n')] 


data=numpy.loadtxt('data_1.txt', dtype=int) * settings[1] 
 
data_time=numpy.array([i*settings[0] for i in range(data.size)]) 

fig, ax=pyplot.subplots(figsize=(16, 10), dpi=500) 
 

ax.axis([data.min(), data_time.max()+1, data.min(), data.max()+0.2]) 
 

ax.xaxis.set_major_locator(ticker.MultipleLocator(2)) 

ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5)) 
 

ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5)) 
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1)) 
 

ax.set_title("\n".join(wrap('процесс заряда и разряда конденсатора в RC цепи', 60)), loc = 'center') 
 

ax.grid(which='major', color = 'k') 
ax.minorticks_on() 
ax.grid(which='minor', color = 'gray', linestyle = ':') 
 

ax.set_ylabel("напряжение, В") 
ax.set_xlabel("время, с") 
 

ax.plot(data_time, data, c='red', linewidth=1, label = 'V(t)') 
ax.scatter(data_time[0:data.size:20], data[0:data.size:20], marker = 's', c = 'blue', s=10) 
 
ax.legend(shadow = False, loc = 'right', fontsize = 30) 
 
 
fig.savefig('graph.png') 
fig.savefig('graph.svg')
