f_input = input("Enter f(x, y) formula (use x and y): ")
f = lambda x, y: eval(f_input)

x0 = float(input("Enter initial x0: "))
h = float(input("Enter step size h: "))

y0 = float(input(f"Enter y({x0}): "))
y1 = float(input(f"Enter y({x0 + h}): "))
y2 = float(input(f"Enter y({x0 + 2*h}): "))
y3 = float(input(f"Enter y({x0 + 3*h}): "))

x_values = [x0, x0 + h, x0 + 2*h, x0 + 3*h, x0 + 4*h]

y4_pred = y0 + (4 * h / 3) * (2 * f(x_values[3], y3) - f(x_values[2], y2) + 2 * f(x_values[1], y1))
y4_corr = y2 + (h / 3) * (f(x_values[2], y2) + 4 * f(x_values[3], y3) + f(x_values[4], y4_pred))

print(f"Predicted y({x_values[4]}) = {y4_pred}")
print(f"Corrected y({x_values[4]}) = {y4_corr}")
