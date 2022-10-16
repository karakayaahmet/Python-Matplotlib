from turtle import color
from matplotlib import markers
from matplotlib.lines import lineStyles
import pandas as pd
import matplotlib.pyplot as plt

x = ["1.ABD","2.Çin","3.Japonya","4.Almanya","5.İngiltere","6.Fransa"]
y = [12342,12334,23449,24234,31343,24324]
z = [11234,12344,43221,53223,53423,43221]

plt.plot(x,y,color="yellow", linewidth=5, linestyle = ":", marker="o", markersize=10, markerfacecolor="blue", markeredgewidth=4, markeredgecolor="red", alpha=0.5)
plt.xlabel("ülkeler")
plt.ylabel("milli gelir")
plt.title("ülkelere göre milli gelir")
plt.xlim([0,3])
plt.ylim([12000,25000])
plt.show()