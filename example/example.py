from squaremaker.square import indentify, areaCalculator, volCalculator
from triangledraw.draw.triplot import make_plot

side = 2
msg = indentify(side)
print(msg, "My area is", areaCalculator(side))
print(msg, "My volume is", volCalculator(side))

make_plot()