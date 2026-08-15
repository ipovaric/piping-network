# Pipe Flow calculator/simulation
#
# Igor Povarich, P.E.
# 8/14/2026
# 
# Current Assumptions/Limitations
#   1. Assumes an incomressible fluid (e.g. water,oil)
#
import numpy as np

# inputs (manual)
# process
P1 = 100            # pressure at inlet (psia)
Q1 = 80             # volumetric flow rate at inlet (gpm)
rho = 62.4          # density of fluid (lbf/ft^3)
# geometric
N_pipe = 2          # number of pipe lengths (qty)
L = [3, 5]          # pipe lengths (ft) [list]
D = [0.167, 0.167]  # pipe diams (ft) [list]
i = [0,1]           # pipe order index

# intermediate calculations
# Conv volumetric flow (gpm) to Velocity (ft/s)
#V = 0.4085 · Q(gpm) / D**2
V = 0.104992 * 




# equations
# Darcy-Weisbach (dP form)
# ΔP = f · (L/D) · (ρ V² / 2) · (1/144)      [ΔP in psi]




ΔP = f · (L/D) · (ρ V² / 2) · (1/144)      [ΔP in psi]


# unit conversions
# ft^3/min = gpm * (0.13368 gal/min / 1 ft^3/min)
# ft/s = ft^3/min * (pi/4) * D^2