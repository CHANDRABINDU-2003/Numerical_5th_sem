import numpy as np
import matplotlib.pyplot as plt
import math

# === Function Definition ===
def f(x):
    return x**3 - 0.165*x**2 + 3.993e-2 

# === Find a valid initial interval for Bisection ===
x_values = np.linspace(0, 1, 1000)
a, b = None, None
for i in range(len(x_values)-1):
    if f(x_values[i]) * f(x_values[i+1]) < 0:
        a = x_values[i]
        b = x_values[i+1]
        break

if a is None or b is None:
    raise ValueError("Could not find a valid initial interval where f(a)*f(b) < 0")

print(f"Initial interval found for Bisection: a = {a:.6f}, b = {b:.6f}")

# === Bisection Method ===
iterations = 3         
results = []           
prev_mid = None       

print("\nPerforming Bisection Method:\n")

for i in range(1, iterations + 1):
    mid = (a + b) / 2
    fa = f(a)
    fm = f(mid)

    if fa * fm < 0:
        b = mid
    else:
        a = mid

    if prev_mid is None:
        abs_rel_err = None
    else:
        abs_rel_err = abs((mid - prev_mid) / mid) * 100

    results.append((i, a, b, mid, fm, abs_rel_err))
    prev_mid = mid

# === Significant digits estimation ===
final_a, final_b = a, b
final_mid = mid
error_bound = (final_b - final_a) / 2
rel_error_bound = error_bound / abs(final_mid)
sig_digits = math.floor(-math.log10(2 * rel_error_bound))

# === Table Output ===
print(f"{'Iter':>4} {'a':>12} {'b':>12} {'mid':>12} {'f(mid)':>14} {'Abs Rel Error (%)':>20}")
for r in results:
    i, a, b, mid, fm, err = r
    err_str = f"{err:.6f}" if err is not None else "   ---   "
    print(f"{i:4d} {a:12.8f} {b:12.8f} {mid:12.8f} {fm:14.8e} {err_str:>20s}")

print("\nEstimated root (after {} iterations) = {:.6f}".format(iterations, final_mid))
print("Error bound = {:.6e}".format(error_bound))
print("Number of significant digits correct ≈ {}\n".format(sig_digits))

# === Plot ===
x = np.linspace(0, 1, 400)
y = f(x)

plt.figure(figsize=(8,5))
plt.plot(x, y, label='f(x)')
plt.axhline(0, color='black', linestyle='--')

midpoints = [row[3] for row in results]
plt.scatter(midpoints, [f(m) for m in midpoints], color='red', label='Midpoints')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Graph of f(x) with Bisection Midpoints")
plt.grid(True)
plt.legend()
plt.show()
