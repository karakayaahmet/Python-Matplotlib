from cProfile import label
from cmath import rect
from turtle import color
from matplotlib import markers
from matplotlib.lines import lineStyles
from numpy import size
import pandas as pd
import matplotlib.pyplot as plt

x = ["1.ABD","2.Çin","3.Japonya","4.Almanya","5.İngiltere","6.Fransa"]
y = [12342,12334,23449,24234,31343,24324]
z = [11234,12344,43221,53223,53423,43221]

f = plt.figure()
axes = f.add_axes([0.1,0.1,0.9,0.9])

#scatter
#axes.scatter(x,y)

#histogram
#axes.hist(y)

#step
#axes.step(x,y)
axes.set_xlabel("Ülkeler")
axes.set_ylabel("Milli Gelir")
axes.set_title("Ülkelerine Göre Milli Gelir")

labels = ["Türkiye","ABD","Çin","Almanya"]
sizes = [35,25,23,17]
explode = (0.1,0,0,0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels)


plt.show()
