import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True) #pozbycie się notacji naukowej

wines = np.genfromtxt(
    r"C:\Users\dario\Documents\Python1\lista12\wine.txt", delimiter=',', skip_header=1)
#print(wines)

gatunek1 = wines[wines[:,0] == 1] #weź tylko te wiersze, które w pierwszej kolumnie mają 1
gatunek2 = wines[wines[:,0] == 2]
gatunek3 = wines[wines[:,0] == 3]

# a)

a_av = np.mean(wines[:, 1])
print(a_av)


print(np.sum(gatunek1[:,1] > a_av))
print(np.sum(gatunek2[:,1] > a_av))
print(np.sum(gatunek3[:,1] > a_av))

# b)
x = wines[:, 1] #kolumna nr 2
y = wines[:, 11]
plt.scatter(x,y, c=wines[:,0])
plt.colorbar(label="Class")
plt.title("Alcohol vs Hue")
plt.xlabel("Alcohol")
plt.ylabel("Hue")
plt.show()


# c)


x = wines[:, 6] #kolumna nr 7
y = wines[:, 10]
plt.scatter(x,y, c=wines[:,0])
plt.colorbar(label="Class")
plt.title("Flavanoids vs Color intensity")
plt.xlabel("Flavanoids")
plt.ylabel("Color intensity")
plt.show()