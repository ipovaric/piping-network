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
Pin = 100            # pressure at inlet (psia)
Qin = 80             # volumetric flow rate at inlet (gpm)
rho = 62.4          # density of fluid (lbf/ft^3)
# geometric
N_pipe = 2          # number of pipe lengths (qty)
L = [3, 5]          # pipe lengths (ft) [list]
D = [0.167, 0.167]  # pipe diams (ft) [list]
idx = [0,1]         # pipe order index

inputs1 = {'Pin':Pin,
          'Qin':Qin,
          'rho':rho,
          'L':L,
          'D':D,
          'idx':idx}

##########

def calcMain(inputs):

    i = 1
    Di = D(i)
    Li = L(i)
    # intermediate calculations
    # Conv volumetric flow (gpm) to Velocity (ft/s)
    #V = 0.4085 · Q(gpm) / D**2
    V = Q1 * Di**2 * 0.104992

    f = 0.02 # assumed for now

    # equations
    # Darcy-Weisbach (dP form)
    # ΔP = f · (L/D) · (ρ V² / 2) · (1/144)      [ΔP in psi]
    dP = f * (Li/Di) * (rho * V**2 / 2) * (1/144)     # [ΔP in psi

if __name__ == "__main__":
    calcMain(inputs)

# unit conversions
# Volume Flow to Velocity
# V = Q * A
# Q[ft^3/min] = Q[gpm] * (0.13368 gpm / 1 cfm)
# V[ft/s] = Q[ft^3/min] * (pi/4) * D^2[ft^2]
# V[ft/s] = Q[gpm] * D^2[ft^2] * (0.13368 * pi/4)
# V[ft/s] = Q[gpm] * D^2[ft^2] * (0.104992 gpm/cfm)