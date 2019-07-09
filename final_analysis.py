import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
% matplotlib inline

E = np.linspace(-20,20,1000)

def func(E, Gamma, Z, delta):
    u0 = np.sqrt(0.5*(1+np.sqrt(((E+1j*Gamma)**2-delta**2)/(E+1j*Gamma)**2)))
    v0 = np.sqrt(1-u0**2)
    y = u0**2+(u0**2-v0**2)*Z**2
    a = u0*v0/y
    b = -((u0**2-v0**2)*(Z**2+1j*Z))/y
    A = a*np.conj(a)
    B = b*np.conj(b)
    G = np.real(1+A-B)
    return G/G[-1]
    
plt.plot(E, func(E,Gamma=0.55,Z=0.453,delta=1.25))
plt.grid()
plt.show()

# TRIAL 6 DATA

# in V:
inputDC6 = np.array([-3.30,-3.23,-3.16,-3.09,-3.02,-2.95,-2.88,-2.81,-2.74,-2.67,
                                          -2.60,-2.53,-2.46,-2.39,-2.32,-2.25,-2.18,-2.11,-2.04,-1.97,
                                          -1.90,-1.83,-1.76,-1.69,-1.62,-1.55,-1.48,-1.41,-1.34,-1.27,
                                          -1.20,-1.13,-1.06,-0.99,-0.92,-0.85,-0.78,-0.71,-0.64,-0.57,-0.50,-0.43,-0.36,
                                          -0.29,-0.22,-0.15,-0.08,0,0.08,0.16,0.24,0.30,0.40,0.48,0.56,0.64,0.72,-0.80,-0.88,
                                          -0.96,1.04,1.12,1.20,1.28,1.36,1.44,1.52,1.60,1.68,1.76,1.84,1.92,1.98,2.08,2.16,
                                          2.24,2.32,2.40,2.48,2.56,2.64,2.72,2.80,2.88,2.96,3.04,3.12,3.20,3.30])
# in uV:
outputAC6 = np.array([368.8,368.8,371.8,375.5,377.7,380.1,379.5,380.3,382.5,383.0,385.0,387.1,389.9,391.2,
                                     391.5,394.0,396.2,400.4,404.6,408.5,412.4,413.2,415.6,416.0,417.1,416.4,418.5,425.6,
                                     430.1,437.2,437.8,434.4,436.1,440.2,444.0,440.8,438.6,435.1,430.7,429.1,428.6,421.5,
                                     417.9,415.5,413.3,413.3,415.8,408.9,427.1,427.7,433.6,436.9,447.3,456.7,462.8,471.7,
                                     476.1,487.3,488.7,494.4,496.3,505.7,507.0,511.4,514.9,515.2,516.6,514.8,516.3,517.0,
                                     516.6,517.1,517.9,519.9,518.8,520.0,520.5,519.5,519.5,519.5,520.3,517.1,517.4,516.2,
                                     518.7,519.8,518.5,518.0,518.8])
# in mV:
outputDC6 = -1*np.array([5.8974,5.7416,5.6362,5.5902,5.4831,5.3880,5.2571,5.1265,5.0315,4.9134,4.7666,
                                            4.6703,4.5696,4.4358,4.3043,4.1719,4.0441,4.0446,3.8585,3.7929,3.6727,3.5576,
                                            3.4249,3.2859,3.1508,2.9999,2.8572,2.7526,2.6349,2.5087,2.4134,2.2651,2.1118,
                                            2.0035,1.8835,1.7191,1.5858,1.4427,1.3032,1.1879,1.1051,0.8796,0.7286,0.5969,
                                            0.4518,0.2975,0.1543,0.0024,-0.1719,-0.3365,-0.5180,-0.6667,-0.8777,-1.0607,
                                            -1.2799,-1.4472,-1.6468,-1.8292,-2.0531,-2.2588,-2.4778,-2.6747,-2.8713,-3.0914,
                                            -3.3159,-3.5260,-3.7327,-3.9784,-4.1721,-4.3933,-4.5787,-4.7240,-4.9671,-5.2432,
                                            -5.4360,-5.6835,-5.9012,-6.1380,-6.3294,-6.5568,-6.7338,-6.9114,-7.1135,-7.3352,
                                            -7.5002,-7.8032,-8.0179,-8.1675,-8.5134])

# ERROR
# in uV:
outputAC6_err = 5
# in mV:
outputDC6_err = 0.005

plt.errorbar(outputDC6, outputAC6, xerr=outputDC6_err, yerr=outputAC6_err, fmt='o', markersize=2, capsize=2)
plt.xlabel('$V_{DC}$ [mV]')
plt.ylabel('$V_{AC}$ [$\mu$V]')
plt.title('Trial 6 $V_{AC}$ vs $V_{DC}$')
plt.grid()
plt.show()

G6 = 1/outputAC6
G6_err = -outputAC6_err/outputAC6**2

plt.errorbar(outputDC6, G6, xerr=outputDC6_err, yerr=G6_err, fmt='o', markersize=2, capsize=2)
plt.xlabel('$V_{DC}$ [mV]')
plt.ylabel('$G_{NS}$')
plt.title('Trial 6 Conductance')
plt.grid()
plt.show()

# SHIFT TO ZERO POINT CENTER
outputDC6_shifted = []

G6_in_zone = []
for i in range(0,len(outputDC6)):
    if -2.5<outputDC6[i]<-1.0:
        G6_in_zone.append(G6[i])
        minG = min(G6_in_zone)
        
for i in range(0,len(G6)):
    if G6[i] == minG:
        minIndex = i
SHIFT = outputDC6[minIndex]

print('Shift value:', -SHIFT, 'mV')

outputDC6_shifted = outputDC6-SHIFT

plt.errorbar(outputDC6_shifted, G6, xerr=outputDC6_err, yerr=G6_err, fmt='o', markersize=2, capsize=2)
plt.xlabel('$V_{DC}$ [mV]')
plt.ylabel('$G_{NS}$')
plt.title('Trial 6 Conductance shifted to center')
plt.grid()
plt.show()

# NORMALIZE AND CUT USELESS DATA
G6_normed = G6/G6[-1]
G6_normed_cut = []
outputDC6_cut = []
G6_err_normed = G6_err/G6[-1]
G6_err_cut = []

for i in range(0,len(outputDC6)):
    if outputDC6_shifted[i]>-1.8:
        G6_normed_cut.append(G6_normed[i])
        outputDC6_cut.append(outputDC6_shifted[i])
        G6_err_cut.append(G6_err_normed[i])
        
plt.errorbar(outputDC6_cut, G6_normed_cut, xerr=outputDC6_err, yerr=G6_err_cut, fmt='o', markersize=2, capsize=2)
plt.xlabel('$V_{DC}$ [mV]')
plt.ylabel('$G_{NS}$ (normalized)')
plt.title('Trial 6 Conductance normalized and cut at $V_{DC}=-1.8$ mV')
plt.grid()
plt.show()

guesses = [1,1,1]
E = np.linspace(-2,11,69)
popt, pcov = scipy.optimize.curve_fit(func, outputDC6_cut, G6_normed_cut, p0=guesses)

print('Optimal parameters:')
print('Gamma =', popt[0], '+/-', np.sqrt(np.diag(pcov)[0]), 'meV')
print('Zeff =', popt[1], '+/-', np.sqrt(np.diag(pcov)[1]))
print('Delta =', popt[2], '+/-', np.sqrt(np.diag(pcov)[2]), 'meV')

fit = func(np.array(outputDC6_cut), *popt)

plt.plot(outputDC6_cut, fit, c='k', label='Fit to BTK theory')
plt.errorbar(outputDC6_cut, G6_normed_cut, xerr=outputDC6_err, yerr=G6_err_cut, fmt='o', markersize=2, capsize=2)
plt.legend()
plt.grid()
plt.show()

E = np.linspace(-max(outputDC6_cut),max(outputDC6_cut),100)

fig1, (ax1,ax2) = plt.subplots(2, sharex=True, gridspec_kw={'height_ratios':[5,1]}, figsize=(8,5))
ax1.errorbar(outputDC6_cut, G6_normed_cut, xerr=outputDC6_err, yerr=G6_err_cut, fmt='o', markersize=3, capsize=3)
ax1.plot(E,func(E, *popt), c='k',label='Fit to BTK theory',color = 'r')
ax1.grid()
ax1.legend()
ax1.set_ylabel('$G_{NS}$ (normalized) [arbitrary units]')
ax1.set_title('Trial 6: Normalized differential conductance of superconducting 99% Nb-Ta')

residuals = G6_normed_cut-fit

ax2.errorbar(outputDC6_cut, residuals, xerr=outputDC6_err, yerr=G6_err_cut, fmt='o', markersize=3, capsize=3)
ax2.set_ylabel('Residuals')
ax2.set_xlabel('$V_{DC}$ [mV]')
ax2.grid()
fig1.subplots_adjust(hspace=0)
plt.show()

hbar = 6.582e-13 #meV/s
Gamma = popt[0]

T = hbar/Gamma
print('Quasiparticle lifetime  T =', T, 's')

Zeff = popt[1]
vfn = 1.4e6
func1 = lambda vfs : Zeff**2-(1-vfn/vfs)**2/(4*(vfn/vfs))

vfs = np.linspace(-1e7,1e7,10000)
plt.scatter(vfs, func1(vfs), s=1)
plt.xlim(0,1e7)
plt.ylim(-1,1)
plt.grid()
#plt.show()

vfs_soln = scipy.optimize.fsolve(func1, 5e5)
print('Fermi velocity lower bound v_Fs =', vfs_soln)

Delta = popt[2]

zeta = hbar*vfs_soln/(np.pi*Delta)
print('Coherence length zeta =', zeta*10**9, 'nm')
