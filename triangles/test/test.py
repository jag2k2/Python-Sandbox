import os, sys
print(sys.path)

current_script_directory = os.path.dirname(__file__)
relative_path = '..'
absolute_path = os.path.abspath(os.path.join(current_script_directory, relative_path))
sys.path.insert(0, absolute_path)

print(sys.path)

from geometry import graphics

graphics.draw_triangle([
    (0.2, 0.2),
    (0.2, 0.6),
    (0.4, 0.4)
])

graphics.draw_triangle([
    (0.6, 0.8),
    (0.8, 0.8),
    (0.5, 0.5)
])

graphics.draw_triangle([
    (0.6, 0.1),
    (0.7, 0.3),
    (0.9, 0.2)
])

graphics.show()