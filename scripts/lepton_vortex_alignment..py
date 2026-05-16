import matplotlib.pyplot as plt
import numpy as np
import math

# Constants
e_charge = 1.602176634e-19
P_m = 10**34 # Matrix background pressure in Pa (J/m³)

# The 6 Leptons (Mass values in MeV/c²)
# Neutrino values are realistic cosmological estimates since the standard table only provides upper limits.
lepton_data_en = {
    'Electron (Gen I)': 0.511,
    'Muon (Gen II)': 105.7,
    'Tau (Gen III)': 1777.0,
    'Electron-neutrino (Gen I)': 0.1e-6,  # 0.1 eV estimate
    'Muon-neutrino (Gen II)': 10.0e-6,    # 10 eV estimate
    'Tau-neutrino (Gen III)': 100.0e-6    # 100 eV estimate
}

colors = ['darkblue', 'darkblue', 'darkblue', 'teal', 'teal', 'teal']

plt.figure(figsize=(11, 7))

# Plot the Matrix Pressure baseline
plt.axhline(y=P_m, color='red', linestyle='--', linewidth=2, label=r'Matrix Baseline Pressure ($P_m = 10^{34}$ Pa)')

# Calculate and plot each particle
for i, (name, mass) in enumerate(lepton_data_en.items()):
    E = (mass * 10**6) * e_charge
    V_v = E / P_m
    density = E / V_v # Mathematically constant at P_m due to E = P_m * V_v

    plt.scatter(V_v, density, color=colors[i], s=150, zorder=5)

    # Handle annotations cleanly using raw strings for LaTeX formatting
    offset_y = 15 if 'neutrino' not in name.lower() else -30
    plt.annotate(f"{name}\n" + r"$V_v \approx$" + f" {V_v:.1e} m³",
                 (V_v, density),
                 textcoords="offset points",
                 xytext=(0, offset_y),
                 ha='center',
                 fontweight='bold',
                 fontsize=9,
                 arrowprops=dict(arrowstyle="->", color='gray'))

# Graph styling in English
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Matrix Vortex-Volume ($V_v$) in m³ (Logarithmic Scale)', fontsize=12)
plt.ylabel('Energy Density ($J/m^3$) / Pressure (Pa)', fontsize=12)
plt.title('SMP Particle Analysis: The 6 Leptons inside the Matrix Medium', fontsize=14, fontweight='bold')
plt.grid(True, which="both", ls="--", color='lightgray')

# Legend setup
plt.scatter([], [], color='darkblue', s=100, label='Charged Vortices (Electron, Muon, Tau)')
plt.scatter([], [], color='teal', s=100, label='Acoustic Ripples (Neutrinos)')
plt.legend(loc='lower left')

plt.tight_layout()
plt.show()
