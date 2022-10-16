from django.forms import inlineformset_factory
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


x = ["1.ABD","2.Çin","3.Japonya","4.Almanya","5.İngiltere","6.Fransa"]
y = [12342,12334,23449,24234,31343,24324]
z = [11234,12344,43221,53223,53423,43221]

plt.plot(x,y)

plt.plot(x,z)

plt.plot(x,y,"r")
plt.xlabel("ülkeler")
plt.ylabel("milli gelir")
plt.title("ülkelere göre milli gelir")
plt.show()

plt.subplot(1,2,1)
plt.plot(x,y,"r")
plt.subplot(1,2,2)
plt.plot(x,z,"b")
plt.tight_layout()

plt.show()

f = plt.figure()
axes = f.add_axes([0.1,0.1,0.9,0.9])
axes.plot(x,y)
axes.set_xlabel("Ülkeler")
axes.set_ylabel("Milli Gelir")
axes.set_title("Ülkelere Göre Milli Gelir")
f.show()


fig,axes = plt.subplots(nrows=1,ncols=3)
axes[0].plot(x,y,"r")
axes[0].set_title("Milli Gelir")

axes[1].plot(x,z,"g")
axes[1].set_title("Kişi Başına")

axes[2].plot(y,z,"b")
axes[2].set_title("Ortalama")

fig.show()
fig.waitforbuttonpress()
