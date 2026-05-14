import numpy as np
import matplotlib.pyplot as plt

# Calculate residuals
R_predicted = a * luminosity**b
residuals = np.log10(radius / R_predicted)

print("\nResiduals (log10):")
for i, name in enumerate(names):
    print(f"{name:20s}: {residuals[i]:+.3f}")

# Galaxy data: [name, luminosity (L_sun), halo_radius (kpc)]
galaxies = [
    ["Draco Dwarf",      2e5,   0.3],
    ["Sculptor Dwarf",   2e6,   0.5],
    ["NGC 3741",         3e7,   3.0],
    ["DDO 154",          5e7,   4.0],
    ["DDO 168",          8e7,   4.0],
    ["NGC 2366",         4e8,   6.0],
    ["NGC 1560",         6e8,   7.0],
    ["NGC 3109",         9e8,   8.0],
    ["NGC 2976",         2e9,   5.0],
    ["NGC 6503",         4e9,  10.0],
    ["NGC 2903",         2e10, 15.0],
    ["NGC 3198",         3e10, 30.0],
    ["Milky Way",        5e10, 25.0],
    ["NGC 2841",         6e10, 35.0],
    ["Andromeda M31",    7e10, 35.0],
    ["NGC 5055",         8e10, 40.0],
    ["NGC 7331",         1e11, 30.0],
    ["NGC 5533",         2e11, 50.0],
    ["NGC 5746",         4e11, 40.0],
    ["NGC 1961",         8e11, 60.0],
]

names = [g[0] for g in galaxies]
luminosity = np.array([g[1] for g in galaxies])
radius = np.array([g[2] for g in galaxies])

# Log-log plot
fig, ax = plt.subplots(figsize=(10, 7))

ax.scatter(luminosity, radius, color='steelblue', s=80, zorder=5)

for i, name in enumerate(names):
    ax.annotate(name, (luminosity[i], radius[i]),
                textcoords="offset points", xytext=(6, 4), fontsize=7)

# Fit power law: R = a * L^b
log_L = np.log10(luminosity)
log_R = np.log10(radius)
coeffs = np.polyfit(log_L, log_R, 1)
b, log_a = coeffs
a = 10**log_a

print(f"Power law fit: R = {a:.4e} * L^{b:.3f}")
print(f"Exponent: {b:.3f} (SMP model predicts ~0.33 to 0.50)")

# Plot fit line
L_fit = np.logspace(np.log10(luminosity.min()),
                    np.log10(luminosity.max()), 100)
R_fit = a * L_fit**b

ax.plot(L_fit, R_fit, 'r--', linewidth=2,
        label=f'Power law fit: R ∝ L^{b:.2f}')

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Luminosity (L☉)', fontsize=12)
ax.set_ylabel('Superfluid Radius (kpc)', fontsize=12)
ax.set_title('SMP Model: Superfluid Radius vs Galaxy Luminosity\n'
             '(thermal phase transition at 13.84 K)', fontsize=13)
ax.legend(fontsize=11)
ax.grid(True, which='both', alpha=0.3)

plt.tight_layout()
plt.savefig('SMP_luminosity_radius.png', dpi=150)
plt.show()
