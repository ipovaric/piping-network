# Pipe Flow Pressure Loss Reference (U.S. Customary Units)

## Section 1 — Major Losses (Darcy-Weisbach)

### 1.1 Darcy-Weisbach Equation

**Head loss form:**

```
h_f = f · (L/D) · (V² / 2g)
```

| Symbol | Description | Units |
|---|---|---|
| h_f | Head loss (friction) | ft |
| f | Darcy friction factor (dimensionless) | — |
| L | Pipe length | ft |
| D | Pipe inside diameter | ft |
| V | Average flow velocity | ft/s |
| g | Gravitational acceleration | 32.2 ft/s² |

**Pressure drop form:**

```
ΔP = f · (L/D) · (ρ V² / 2) · (1/144)      [ΔP in psi]
```

or equivalently, using specific weight γ (lbf/ft³):

```
ΔP (psi) = γ · h_f / 144
```

where ρ is fluid density (lbm/ft³) and the 32.2 lbm·ft/(lbf·s²) conversion factor (g_c) is folded into the ρV² term if working in lbf.

### 1.2 Continuity / Velocity

```
Q = A · V        V = Q / A        A = π D² / 4
```

Common unit conversion for liquid flow:

```
V (ft/s) = 0.4085 · Q(gpm) / D²(in)
```

(derived from Q(cfs) = Q(gpm) / 448.831, A in ft²)

### 1.3 Reynolds Number

```
Re = V·D·ρ / μ = V·D / ν
```

| Regime | Criterion |
|---|---|
| Laminar | Re < 2,300 |
| Transitional | 2,300 < Re < 4,000 |
| Turbulent | Re > 4,000 |

### 1.4 Friction Factor

**Laminar flow (exact):**
```
f = 64 / Re
```

**Turbulent flow — Colebrook equation (implicit, iterative):**
```
1/√f = -2·log10[ (ε/D)/3.7 + 2.51/(Re·√f) ]
```

**Swamee-Jain explicit approximation** (±1% of Colebrook, no iteration, valid 5,000 < Re < 10⁸ and 10⁻⁶ < ε/D < 10⁻²):
```
f = 0.25 / { log10[ (ε/D)/3.7 + 5.74/Re^0.9 ] }²
```

### 1.5 Typical Absolute Roughness (ε)

| Pipe Material | ε (ft) | ε (in) |
|---|---|---|
| Drawn tubing / glass | 0.000005 | 0.00006 |
| Commercial/welded steel | 0.00015 | 0.0018 |
| Wrought iron | 0.00015 | 0.0018 |
| Asphalted cast iron | 0.0004 | 0.0048 |
| Galvanized iron | 0.0005 | 0.006 |
| Cast iron | 0.00085 | 0.0102 |
| Concrete | 0.001 – 0.01 | 0.012 – 0.12 |
| Riveted steel | 0.003 – 0.03 | 0.036 – 0.36 |
| PVC/plastic | 0.000005 | 0.00006 |

### 1.6 Velocity Head

```
h_v = V² / 2g
```

Used as the common multiplier for both major and minor losses.

---

## Section 2 — Minor Losses (Fittings, Valves, Entrances/Exits)

### 2.1 General Form

**K-value (resistance coefficient) method:**
```
h_m = K · (V² / 2g)
```

**Equivalent length method (alternative):**
```
h_m = f · (Le/D) · (V² / 2g)
```

Total system loss:
```
h_L,total = h_f + Σh_m = [f·(L/D) + ΣK] · (V² / 2g)
```

### 2.2 K-Values — Fittings

| Fitting | K (typical) |
|---|---|
| 90° elbow, standard (threaded) | 1.5 |
| 90° elbow, standard (flanged) | 0.3 |
| 90° elbow, long radius (flanged) | 0.2 |
| 45° elbow, standard | 0.4 |
| 45° elbow, long radius | 0.2 |
| 180° return bend (flanged) | 0.2 |
| Tee, flow through run (line flow) | 0.2 |
| Tee, flow through branch | 1.0 |
| Coupling / union | 0.08 |
| Pipe entrance, sharp-edged | 0.5 |
| Pipe entrance, rounded | 0.04 – 0.05 |
| Pipe entrance, re-entrant (Borda) | 0.8 – 1.0 |
| Pipe exit (into reservoir) | 1.0 |

### 2.3 K-Values — Reducers / Expanders

| Fitting | K (typical) |
|---|---|
| Gradual contraction (≤45° included angle) | 0.04 – 0.08 |
| Sudden contraction (based on D2/D1, small ratio) | 0.3 – 0.5 |
| Gradual expansion (7°–15° cone) | 0.2 – 0.3 |
| Sudden expansion | K = [1 − (D1/D2)²]² (based on V1, upstream velocity) |

### 2.4 K-Values — Valves (full open, unless noted)

| Valve Type | K (typical) |
|---|---|
| Gate valve, full open | 0.15 – 0.2 |
| Gate valve, ¾ open | 0.9 – 1.15 |
| Gate valve, ½ open | 4.5 – 5.6 |
| Globe valve, full open | 6.0 – 10.0 |
| Angle valve, full open | 2.0 – 3.0 |
| Ball valve, full bore, full open | 0.04 – 0.1 |
| Butterfly valve, full open | 0.3 – 0.5 |
| Plug valve, straightway | 0.3 – 0.5 |
| Swing check valve, full open | 2.0 – 2.5 |
| Lift check valve, full open | 10 – 12 |
| Diaphragm valve, full open | 2.0 – 2.3 |

*Note: valve K-values vary meaningfully by manufacturer, size, and internal geometry. For detailed engineering work, use the manufacturer's Cv data or Crane Technical Paper 410 (2÷K method) rather than generic table values.*

### 2.5 Notes on Application

- All K-values above assume fully turbulent flow and are referenced to the **velocity in the smaller/downstream pipe** unless otherwise noted.
- For a piping system with multiple fittings of different sizes, K-values must be adjusted (scaled by (D_small/D_large)⁴) before summing, since K is diameter-dependent when comparing across different pipe sizes.
- Cv-based valve sizing (`Q = Cv·√(ΔP/SG)` for liquids, gpm/psi) is generally preferred over generic K-tables for control valves and vendor-specific equipment.
