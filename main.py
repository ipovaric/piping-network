# Pipe Flow calculator/simulation
#
# Igor Povarich, P.E.
# 8/14/2026
# 
# Current Assumptions/Limitations
#   1. Assumes an incomressible fluid (e.g. water,oil)
#
import numpy as np

# example inputs (manual)
# process
Pin = 100           # pressure at inlet (psia)
Qin = 120           # volumetric flow rate at inlet (gpm)
rho = 62.4          # density of fluid (lbf/ft^3)
# N_pipe = 2         # number of pipe lengths (qty)
L = [300,500,200,1000] # pipe lengths (ft) [list]
# D = [0.167,0.167,0.25,0.25]  # pipe diams (ft) [list]
D = [2,2,3,3]       # pipe diams (in) [list]
idx = [0,1,2,3]     # pipe order index

inputs = {'Pin':Pin,
          'Qin':Qin,
          'rho':rho,
          'L':L,
          'D':D,
          'idx':idx}
data = {'inputs',inputs}

##########

def calcFlows(data):
    """ Calculate Velocity and Volumetric flow rates.
    Assumptions:
        * Single stream of flow (no branches)
    """
    inputs  = data['inputs']
    Qin     = inputs['Qin']
    D       = inputs['D']
    idx     = inputs['idx']

    A,V,Q,Q_gpm = [],[],[],[]

    # unit conversions
    in_ft = 1/12
    min_sec = 60
    gpm_cfm = 0.13368

    # inlet conditions to get starting mfr
    #   inlet area (ft^2)
    Ain = ((np.pi/4) * D[0]**2) * (in_ft**2)
    #   inlet velocity (ft/s)
    Vin = (Qin / Ain) * (gpm_cfm / min_sec)
    #   mass flow rate (lbm/min)
    w = rho * Vin * Ain * (min_sec)

    for i in idx:
        Ai = ((np.pi/4) * D[i]**2) * (in_ft**2)
        Qi = w / rho # (lbm/min) * (ft^3/lbm)
        Qi_gpm = Qi / gpm_cfm 
        Vi = (Qi / Ai) * (gpm_cfm / min_sec)

        A.append(Ai)
        Q.append(Qi)
        Q_gpm.append(Qi_gpm)
        V.append(Vi)

    print([f'{x:.3f}' for x in A])
    print([f'{x:.3f}' for x in Q])
    print([f'{x:.2f}' for x in Q_gpm])
    print([f'{x:.3f}' for x in V])

def calcMajor(data):
    """ Calculate Major (friction) Losses
    """

    
    inputs  = data['inputs']
    Pin     = inputs['Pin']
    Qin     = inputs['Qin']
    rho     = inputs['rho']

    dP = []

    # i = 1
    for i in range(len(inputs['idx'])):
        
        Di      = inputs['D'][i]
        Li      = inputs['L'][i]
        idx     = inputs['idx'][i]

        

        # friction factor calc
        f = 0.02 # assumed for now

        # equations
        # Darcy-Weisbach (dP form)
        dPi = f * (Li/Di) * (rho * V**2 / 2) * (1/144)     # [ΔP in psi]
        dP.append(dPi)

    dPTot = np.sum(dP)
    Pout = Pin - dPTot

    print(inputs)
    print([f'{x:.3f}' for x in dP])
    print(f'dP Total: {dPTot:.3f} psid')
    print(f'Pout: {Pout:0.2f} psia')

def calcRe(data):
    """ Calculate reynods number 
    Re = V·D·ρ / μ = V·D / ν
    """

    inputs = data['inputs']
    V = 

    Re = V·D·ρ / μ = V·D / ν

def main(data):
    calcMajor(data)

main(data)
# if __name__ == "__main__":
#     calcMain(inputs)

# unit conversions
# Volume Flow to Velocity
# V = Q / A
# Q[ft^3/min] = Q[gpm] * (0.13368 gpm / 1 cfm)
# V[ft/s] = Q[ft^3/min] * (pi/4) * D^2[ft^2]
# V[ft/s] = Q[gpm] * D^2[ft^2] * (0.13368 * pi/4)
# V[ft/s] = Q[gpm] * D^2[ft^2] * (0.104992 gpm/cfm)