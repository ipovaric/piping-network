# Pipe Flow calculator/simulation
#
# Igor Povarich, P.E.
# 8/14/2026
# 
# Current Assumptions/Limitations
#   1. Assumes an incomressible fluid (e.g. water,oil)
#
import numpy as np
# import math

# surface roughness
eps = np.array(0.0018) # in (0.00015 ft for welded steel)

# test inputs (manual)
inputs = {
    'Pin':100,              # pressure at inlet (psia)
    'Qin':120,              # volumetric flow rate at inlet (gpm)
    'rho':62.4,             # density of fluid (lbf/ft^3)
    'mu':1.8e-5,            # visc of fluid (lbf*s/ft^2)
    'L':[300,500,200,1000], # pipe lengths (ft) [list]
    'D':[2,2,3,3],          # pipe diams (in) [list]
    'idx':[0,1,2,3]}        # pipe order index
data = {'inputs':inputs}

##########

def calcFlows(data):
    """ Calculate Velocity and Volumetric flow rates.
    Assumptions:
        * Single stream of flow (no branches)
    """
    inputs  = data['inputs']
    Qin     = np.array(inputs['Qin'])
    rho     = np.array(inputs['rho'])
    mu      = np.array(inputs['mu'])
    D       = np.array(inputs['D'])
    idx     = inputs['idx']

    A,V,Q,Q_gpm = [],[],[],[]

    # unit conversions
    in_ft = 1/12
    min_sec = 60
    gpm_cfm = 0.13368
    gc = 32.174 # lbm*ft/(lbf*s^2)

    # inlet conditions to get starting mfr
    #   inlet area (ft^2)
    Ain = ((np.pi/4) * D[0]**2) * (in_ft**2)
    #   inlet velocity (ft/s)
    Vin = (Qin / Ain) * (gpm_cfm / min_sec)
    #   mass flow rate (lbm/min)
    w = rho * Vin * Ain * (min_sec)

    # calc each flow rate
    for i in idx:
        Ai = ((np.pi/4) * D[i]**2) * (in_ft**2)
        Qi = w / rho # (lbm/min) * (ft^3/lbm) = ft^3/min
        Qi_gpm = Qi / gpm_cfm 
        Vi = (Qi / Ai) * (gpm_cfm / min_sec)

        A.append(Ai)
        Q.append(Qi)
        Q_gpm.append(Qi_gpm)
        V.append(Vi)

    # calc Reynolds number
    Re = V * D * rho / (mu*gc)

    # print to console
    val1 = ", ".join(f"{v:8.3f}" for v in A)
    print(f"A:  {val1} ft^2")
    val2 = ", ".join(f"{v:8.3f}" for v in Q)
    print(f"Q:  {val2} ft^3/min")
    val3 = ", ".join(f"{v:8.1f}" for v in Q_gpm)
    print(f"Q:  {val3} gal/min")
    val4 = ", ".join(f"{v:8.3f}" for v in V)
    print(f"V:  {val4} ft/sec")
    val5 = ", ".join(f"{v:8.2e}" for v in Re)
    print(f"Re: {val5}")

    # pack into data
    flows = {'w':w,
             'A':A,
             'Q':Q,
             'Q_gpm':Q_gpm,
             'V':V,
             'Re':Re}
    data['flows'] = flows
    return data

def calcFriction(data):
    """ Calculate Darcy Friction factors
        Uses Swamee-Jain explicit approximation of Colebrook
    """
    # f = 0.25 / { log10[ (ε/D)/3.7 + 5.74/Re^0.9 ] }²

    inputs  = data['inputs']
    flows   = data['flows']
    Qin     = np.array(inputs['Qin'])
    rho     = np.array(inputs['rho'])
    D       = np.array(inputs['D'])
    Re      = flows['Re']
    idx     = inputs['idx']

    f = 0.25 / (np.log10( (eps/D)/3.7 + 5.74/Re**0.9))**2

    val1 = ", ".join(f"{v:8.2e}" for v in f)
    print(f"f:  {val1}")

    friction = {'f':f}
    data['friction'] = friction
    return data

def calcMajor(data):
    """ Calculate Major (friction) Losses
    """

    inputs  = data['inputs']
    flows   = data['flows']
    friction= data['friction']
    Pin     = np.array(inputs['Pin'])
    L       = np.array(inputs['L'])
    D       = np.array(inputs['D'])
    rho     = np.array(inputs['rho'])
    idx     = inputs['idx']
    V       = flows['V']
    f       = friction['f']    

    dP = []

    # i = 1
    for i in range(len(idx)):

        # equations
        # Darcy-Weisbach (dP form in psi)
        dPi = f[i] * (L[i]/D[i]) * (rho * V[i]**2 / 2) * (1/144)     
        dP.append(dPi)

    dPTot = np.sum(dP)
    Pout = Pin - dPTot

    
    # print([f'{x:.3f}' for x in dP])
    val1 = ", ".join(f"{v:8.3f}" for v in dP)
    print(f"dP: {val1} psia")
    print(f'dPTot:{dPTot:6.3f} psid')
    print(f'Pout:  {Pout:6.2f} psia')

def calcMinor(data):
    inputs  = data['inputs']
    flows   = data['flows']
    friction= data['friction']


def main(data):
    """ Main Function 
    data: tracking dictionary
    """
    print(inputs)
    calcFlows(data)
    calcFriction(data)
    calcMajor(data)
    
    # print('')
    # print(data)

main(data)
# if __name__ == "__main__":
#     calcMain(inputs)

################
# unit conversions
# Volume Flow to Velocity
# V = Q / A
# Q[ft^3/min] = Q[gpm] * (0.13368 gpm / 1 cfm)
# V[ft/s] = Q[ft^3/min] * (pi/4) * D^2[ft^2]
# V[ft/s] = Q[gpm] * D^2[ft^2] * (0.13368 * pi/4)
# V[ft/s] = Q[gpm] * D^2[ft^2] * (0.104992 gpm/cfm)

# Reynolds Number
# gc = 32.174 lbm*ft/(lbf*s^2)
# (ft/s) * ft * (lbm/ft^3) / (lbf*s/ft^2)
# (ft/s) * ft * (lbm/ft^3) * (ft^2/(lbf*s)) / gc
# (ft^2/s) * (lbm/ft^3) * (ft^2/(lbf*s)) * (1/32.174) lbf*s^2/(lbm*ft)
# (1/32.174)

## pressure drop - major
# gc = 32.174 lbm*ft/(lbf*s^2)
# ΔP = f · (L/D) · (ρ V² / 2) · (1/144)
# ΔP (lbf/in^2) 
# = (lbm/ft^3)*(ft/s)^2 / gc / 144
# = (lbm/ft^3)*(ft/s)^2 * (1/32.174 (lbf*s^2)/(lbm*ft))*(1/144 1/ft^2))
# = 