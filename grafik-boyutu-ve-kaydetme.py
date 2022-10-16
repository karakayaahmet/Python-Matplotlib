from cProfile import label
from cmath import rect
from turtle import color
from matplotlib import markers
from matplotlib.lines import lineStyles
import pandas as pd
import matplotlib.pyplot as plt

x = ["1.ABD","2.Çin","3.Japonya","4.Almanya","5.İngiltere","6.Fransa"]
y = [12342,12334,23449,24234,31343,24324]
z = [11234,12344,43221,53223,53423,43221]

f = plt.figure(figsize=(7,3))
axes = f.add_axes([0,0,1,1])
axes.plot(x,y,"r")
axes.set_xlabel("Ülkeler")
axes.set_ylabel("Milli Gelir")
axes.set_title("Ülkelerine Göre Milli Gelir")

ax = f.add_axes([0,0,1,1])
ax.plot(x,y,"r", label="milli gelir")
ax.plot(x,z,"y", label="kişi başına")

ax.legend(loc=1)

f.savefig("resim.png")
plt.show()


