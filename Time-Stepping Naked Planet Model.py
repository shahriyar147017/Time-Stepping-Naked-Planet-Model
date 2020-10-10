#Time-stepping naked planet model
#Written by Mohammad Shahiyar Parvez
#email : mohammadshahriyarparvez@yahoo.co.uk
while True:
    import matplotlib.pyplot as plt
    import numpy as np
    waterDepth = int (input ("Input ocean depth\n"))
    timeSteps = float (input("Input the number of time steps:\n")) #incremental value of time in years
    #waterDepth = 4000 # in meters
    L = 1350 #Sunlight factor in watts/m2 
    albedo = 0.3 #reflection factor, symbolized as alpha
    epsilon = 1 #quality of blackbody radiation
    sigma = 5.67E-8 #Boltzmann Const in (W/m2)*K4
    heatCapacity = waterDepth * 4.2E6 #J/(m2 - K)
    timeYears = [0] #in years
    T = [400] #Temperature (Kelvin) of ground as simulation progresses
    heatContent = heatCapacity * T[0] 
    energyInflux = (L*(1-albedo))/4   # Energy received by planet
    energyOutflux = 0  #Energy emitted by planet while initializing 

    for time in range(0,100):
        timeYears.append(timeSteps + timeYears[-1])
        energyOutflux = epsilon * sigma * (T[-1]**4)
        print ('After {0} years, the heat content is {1} J/m2 and the outgoing heat flux is {2} TEMPERATURE {3}'.format(timeYears[-1], heatContent, energyOutflux, T[-1]))
        heatContent += (energyInflux - energyOutflux)* timeSteps * 3.14e7    # 3.14e7 is to convert sec to years
        T.append (heatContent / heatCapacity)

    print("Ground Temperaure is {} K, and\nThe heat flux is {} W/m2\n" .format(T[-1], energyOutflux))

    plt.plot(timeYears, T)
    plt.show()