# Lecturas de sensores
sensores = [120, 85, 210, 150]
umbral = 100

for i in range(len(sensores)):
    print(f"Sensor {i+1}: {sensores[i]} cm")
    if sensores[i] < umbral:
        print("Advertencia: Obstaculo muy cerca")
