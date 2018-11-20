# Ejercicio5
# imprima el mensaje: "hola mundo!" 
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
print("hola mundo")

x = np.linspace(0, 10, 100)
y = np.cos(x)*np.sin(x)

plt.plot(x, y)
plt.savefig("wol.pdf")
