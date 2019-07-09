import numpy as np
import matplotlib.pyplot as plt

#EXPERIMENTAL RESULTS (RUN 6) DONE WITH EVEN MORE CORRECTIONS AND FRESHLY ETCHED TIP, WEEK 11 WEDNESDAY

#TRIAL FAILED DUE TO BROKEN/OXIDIZIED NIOBIUM CONTACT

#RUN 6 RE-TRIED WEEK 11 THURSDAY

#RESISTANCE MEASUREMENT
resistance_6_ohms = (30,3)

inputDC6 = np.array([-3.30,-3.23,-3.16,-3.09,-3.02,-2.95,-2.88,-2.81,-2.74,-2.67,
                                          -2.60,-2.53,-2.46,-2.39,-2.32,-2.25,-2.18,-2.11,-2.04,-1.97,
                                          -1.90,-1.83,-1.76,-1.69,-1.62,-1.55,-1.48,-1.41,-1.34,-1.27,
                                          -1.20,-1.13,-1.06,-0.99,-0.92,-0.85,-0.78,-0.71,-0.64,-0.57,-0.50,-0.43,-0.36,
                                          -0.29,-0.22,-0.15,-0.08,0,0.08,0.16,0.24,0.30,0.40,0.48,0.56,0.64,0.72,-0.80,-0.88,
                                          -0.96,1.04,1.12,1.20,1.28,1.36,1.44,1.52,1.60,1.68,1.76,1.84,1.92,1.98,2.08,2.16,
                                          2.24,2.32,2.40,2.48,2.56,2.64,2.72,2.80,2.88,2.96,3.04,3.12,3.20,3.30])


outputAC6 = np.array([368.8,368.8,371.8,375.5,377.7,380.1,379.5,380.3,382.5,383.0,385.0,387.1,389.9,391.2,
                                     391.5,394.0,396.2,400.4,404.6,408.5,412.4,413.2,415.6,416.0,417.1,416.4,418.5,425.6,
                                     430.1,437.2,437.8,434.4,436.1,440.2,444.0,440.8,438.6,435.1,430.7,429.1,428.6,421.5,
                                     417.9,415.5,413.3,413.3,415.8,408.9,427.1,427.7,433.6,436.9,447.3,456.7,462.8,471.7,
                                     476.1,487.3,488.7,494.4,496.3,505.7,507.0,511.4,514.9,515.2,516.6,514.8,516.3,517.0,
                                     516.6,517.1,517.9,519.9,518.8,520.0,520.5,519.5,519.5,519.5,520.3,517.1,517.4,516.2,
                                     518.7,519.8,518.5,518.0,518.8])

outputDC6 = -1*np.array([5.8974,5.7416,5.6362,5.5902,5.4831,5.3880,5.2571,5.1265,5.0315,4.9134,4.7666,
                                            4.6703,4.5696,4.4358,4.3043,4.1719,4.0441,4.0446,3.8585,3.7929,3.6727,3.5576,
                                            3.4249,3.2859,3.1508,2.9999,2.8572,2.7526,2.6349,2.5087,2.4134,2.2651,2.1118,
                                            2.0035,1.8835,1.7191,1.5858,1.4427,1.3032,1.1879,1.1051,0.8796,0.7286,0.5969,
                                            0.4518,0.2975,0.1543,0.0024,-0.1719,-0.3365,-0.5180,-0.6667,-0.8777,-1.0607,
                                            -1.2799,-1.4472,-1.6468,-1.8292,-2.0531,-2.2588,-2.4778,-2.6747,-2.8713,-3.0914,
                                            -3.3159,-3.5260,-3.7327,-3.9784,-4.1721,-4.3933,-4.5787,-4.7240,-4.9671,-5.2432,
                                            -5.4360,-5.6835,-5.9012,-6.1380,-6.3294,-6.5568,-6.7338,-6.9114,-7.1135,-7.3352,
                                            -7.5002,-7.8032,-8.0179,-8.1675,-8.5134])
ACFractionalError = (2/outputAC6)
print(ACFractionalError)
#Graph Output AC vs Output DC
fig0, ax0 = plt.subplots(figsize=(8,5))
#ax0.scatter(outputDC6, outputAC6)
ax0.errorbar(outputDC6, outputAC6, xerr=0.005, yerr=2, fmt='o', markersize= 1, capsize=3)

ax0.set_xlabel('Output DC (mV)')
ax0.set_ylabel('Output AC (uV)')
ax0.set_title('Output AC vs Output DC Trial 6')
# ax0.set_xticks(np.arange(-3.0,1.5,0.25))
# ax0.set_xlim(-2.2,1.0)
plt.grid()
#plt.savefig('name.png')
plt.show()


#Transform AC to differential conductance 1/AC
diffCond6 = 1/outputAC6
diffCondError = diffCond6*ACFractionalError
print(diffCondError)
#print(diffCond6)

#Graph Differential Conductance 1/AC vs Output DC Trial 6
fig1, ax1 = plt.subplots(figsize=(8,5))
ax1.errorbar(outputDC6, diffCond6, xerr=0.005,  yerr=diffCondError, fmt='o', markersize= 1, capsize=3)

ax1.set_xlabel('Output DC (mV)')
ax1.set_ylabel('Differential Conductance')
ax1.set_title('Differential Conductance vs Output DC Trial 6')
#ax1.set_xticks(np.arange(-3.1,1.5,0.25))
ax1.set_ylim(0.0015,0.003)
plt.grid()
#plt.savefig('name.png')
plt.show()

#Normalize the Conductance and center at zero

#Find DC offset
minIndex = len(outputDC6)
for i in range(len(outputDC6)):
    if outputDC6[i] > -2.1 and outputDC6[i] < -1.8:
        if diffCond6[i] < minIndex:
            minIndex = i
print('Minimum Diff Conductance = ' + str(diffCond6[minIndex]))

#Find DC value at minimu
dcMin = outputDC6[minIndex]
print('DC Offset mV = ' + str(dcMin))
#Shift all DC malues by offset
outputDCShifted = outputDC6 + (-1*dcMin)

#Graph With offset
fig2, ax2 = plt.subplots(figsize=(8,5))
ax2.errorbar(outputDCShifted, diffCond6, xerr=0.005, yerr=diffCondError, fmt='o', markersize= 1, capsize=3)
ax2.set_xlabel('Output DC (mV)')
ax2.set_ylabel('Differential Conductance')
ax2.set_title('Differential Conductance vs Output DC Trial 6 With DC Offset')
#ax1.set_xticks(np.arange(-3.1,1.5,0.25))
ax1.set_ylim(0.0015,0.003)
plt.grid()
#plt.savefig('name.png')
plt.show()

#Normalize the Graph so tail conductance is 1
#Take sum of points greater than 6 mV
sum1 = 0
length = 0
for i in range(len(outputDCShifted)):
    if outputDCShifted[i] > 6:
        sum1 = sum1 + diffCond6[i]
        length = length + 1

print("Avergae conductance for tail is:" + str(sum1/length))
#Scaling Factor to normalize tail to 1
scaleFactor = sum1/length

condNormal = diffCond6/scaleFactor

#Graph With offset and Normalized
fig3, ax3 = plt.subplots(figsize=(8,5))
ax3.errorbar(outputDCShifted, condNormal, xerr=0.005, yerr=diffCondError*(1/scaleFactor), fmt='o', markersize= 1, capsize=3)
ax3.set_xlabel('Output DC (mV)')
ax3.set_ylabel('Differential Conductance')
ax3.set_title('Differential Conductance vs Output DC Trial 6 With DC Offset and Normalized')
#ax1.set_xticks(np.arange(-3.1,1.5,0.25))
#ax1.set_ylim(0.0015,0.003)
plt.grid()
#plt.savefig('name.png')
plt.show()

#Decide where to cut the bad data
#zoom in on -2 - -1 mV
fig4, ax4 = plt.subplots(figsize=(8,5))
ax4.scatter(outputDCShifted, condNormal)
ax4.set_xlabel('Output DC (mV)')
ax4.set_ylabel('Differential Conductance')
ax4.set_title('Differential Conductance vs Output DC Trial 6 With DC Offset and Normalized')
ax4.set_xlim(-3,-1.8)
ax4.set_ylim(1.2,1.35)
plt.grid()
#plt.savefig('name.png')
plt.show()

#something happened around between -2 and -2.2, discrpenacy in the points. Chop data there
finalDC = []
finalCond = []

for i in range(len(outputDCShifted)):
    if outputDCShifted[i] > -1.8:
        finalDC.append(outputDCShifted[i])
        finalCond.append(condNormal[i])
fig5, ax5 = plt.subplots(figsize=(8,5))
ax5.scatter(finalDC, finalCond)
ax5.set_xlabel('Output DC (mV)')
ax5.set_ylabel('Differential Conductance')
ax5.set_title('Differential Conductance vs Output DC Trial 6 With DC Offset and Normalized and Cut at -2.0')
#ax5.set_xlim(-3,-1.8)
#ax5.set_ylim(1.2,1.35)
plt.grid()
#plt.savefig('name.png')
plt.show()

#Curve fit to above graph
import scipy.optimize
def func(E, gammaRate, delta, Z, offset):
    uSquared = (1.0/2.0)*( 1 + np.sqrt( ((E+(1j)*gammaRate)**2-delta**2) / ((E+(1j)*gammaRate)**2) ) )  #eqn 15
    #print("u^2: " + str(uSquared))
    vSquared = 1 - uSquared #eqn 15
    #print("v^2: " + str(vSquared))
    u = np.sqrt(uSquared) #15
    #print("u: " + str(u))
    v = np.sqrt(vSquared) #15
    #print("v: " + str(v))
    gamma = uSquared + (uSquared - vSquared)*Z**2 #eqn 18
    #print("gamma: " + str(gamma))

    a = (u*v)/(gamma) #eqn 16
    #print("a: " + str(a))
    b = -1*( ((uSquared-vSquared)*(Z**2+1j*Z**2)) / gamma)
    #print("b: " + str(b))

    A = a*np.conj(a) #between 18/19
    #print("A: " + str(A))
    B = b*np.conj(b) #between 18/19
    #print("B: " + str(B))

    cond = 1 + A - B + offset#eqn 24
    #print("conductance: " + str(cond))
    return np.real(cond)

popt, pcov = scipy.optimize.curve_fit(func, finalDC, finalCond, p0=[0.98818298,2.69966382,0.42229179,1])

print('Optimal parameters:', popt)

fig3, ax3 = plt.subplots(figsize=(8,5))
ax3.plot(np.array(finalDC), func(np.array(finalDC), *popt), label='Fit', c='k')
ax3.errorbar(np.array(finalDC), np.array(finalCond), xerr=0.005, yerr=0, label='label', fmt='o', markersize=3, capsize=3)
perr = np.sqrt(np.diag(pcov))

ax1.set_ylim(0.0015,0.003)
#x1 = np.linspace(-20,20,num=1000)
#plt.plot(x1,func(x1,0.82,1.53,0.78,1))
plt.grid()
plt.show()

#Plot with data points and full curve
fig7, ax7 = plt.subplots(figsize=(8,5))
ax7.errorbar(np.array(finalDC), np.array(finalCond), xerr=0.005, yerr=0, label='label', fmt='o', markersize=3, capsize=3)
x1 = np.linspace(-10,10,num=10000)
plt.plot(x1,func(x1,popt[0],popt[1],popt[2],popt[3]), c = 'k')
perr = np.sqrt(np.diag(pcov))
ax7.set_xlabel('$V_D$$_C$ [mV]')
ax7.set_ylabel('$G_N$$_S$ (normalized)')
ax7.set_title('Trial 6: Differential conductance of superconducting niobium')
plt.grid()
plt.show()
print('')
print('Results:')
print('Gamma = '+str(popt[0])+" +/- " + str(perr[0]))
print('Delta (Energy Gap) = ' +str(popt[1])+" +/- " + str(perr[1]))
print('Z = '+str(popt[2])+" +/- " + str(perr[2]))
print('Extra Offset Parameter = '+str(popt[3])+" +/- " + str(perr[3]))

#Calculation of all the other constants
hbar = 6.5821195e-13 #meV
#Gamma = hbar/tau eqn 6
tau = hbar/popt[0]
#vfs minimum fermi velocity use eqn 18, vfn for gold is 1.4E6m/s ref 6
# vfs >= 523213 m/s
vfs = 523213
#BCS Coherence length
#coherence length = hbar*vfs/pi*delta
cohLength = (hbar*523213)/(np.pi*popt[2]) #m
cohLength = (cohLength)/(10e-9)
print('Quasi Particle Lifetime Tau (s) = ' + str(tau))
#Calculated using eqn 19 and wolfram
print('Minimum fermi velocity (m/s) = 5.23X10^5')
print('BCS Coherence Length (nm)= ' + str(cohLength))
