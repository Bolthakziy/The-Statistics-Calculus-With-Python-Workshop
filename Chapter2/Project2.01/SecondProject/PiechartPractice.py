import matplotlib.pyplot as plt


electronicsProduct = ["Resistor", "Diode", "Microcontroller", "MOSFET", "Regulator"]
electronicsAmount = [242, 356, 16, 673, 152]

plt.pie(electronicsAmount, labels = electronicsProduct)
plt.show()
