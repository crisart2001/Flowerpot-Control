import time
import requests
import RPi.GPIO as GPIO
from datetime import datetime
from si1145 import SI1145
from bme280 import BME280
from bh1750 import readLight
from RFM9X import RFM9X
rfm9x1 = RFM9X(node=50)
rfm9x2 = RFM9X(node=23)
while True:
    try:
        request = requests.get("http://www.google.com", timeout = 5)
    except (requests.ConnectionError, requests.Timeout):
        print("Sin conexion a internet")
    else:
        print("Con conexion a internet")
        break
url   = "http://201.207.53.225:3030/api/cosecha/AtmosphericReport"
url_1 = "http://201.207.53.225:3030/api/cosecha/QualityReport"
def main():
    '''try:
        sensor_bme280 = BME280(configured_measurements=["Temperature", "Pressure", "Humidity"])
    except:
        print('Sensor BME280 no conectado/funcional')
    try:
        sensor_si1145 = SI1145(configured_measurements=["UV_Radiation"])
    except:
        print('Sensor SI1145 no conectado/funcional')
    for _ in range(1):
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        #Sensor de luminosidad
        try:
            sensor_bh1750 = readLight()
            print("Light Level : " + format(sensor_bh1750,'.2f') + " lx")
        except:
            sensor_bh1750=0
            print('Sensor BH1750 no conectado/funcional')  
            
            
        try:
            measurements1 = sensor_si1145.read_sensor_values()
        except:
            print('Sensor SI1145 no conectado/funcional')
            
            
        try:
            measurements2 = sensor_bme280.read_sensor_values()
        except:
            print('Sensor BME280 no conectado/funcional')*/
            
            
        a=['','','']
        i=0
        try:
            for meas in measurements1:
                print("{} : {}".format(meas.name, meas.value))
                b=meas.value
        except: 
            b=0
        print(b)
        
        
        try:
            for meas in measurements2:
                print("{} : {}".format(meas.name, meas.value))
                a[i]= meas.value
                i=i+1
        except:
             a=[0,0,0]
        print(a)
        print("") '''
        
        #Subida sensores Estacion
        rec = [str(1),str(b),str(sensor_bh1750),str(a[1]),str(a[0]),str(a[2])]
        recibidos = send = {"id_device": rec[0], "created_at": dt_string, "UV_Radiation": rec[1], "Luminosity":rec[2], "Pressure": rec[3], "Temperature": rec[4], "Humidity": rec[5]}
        print(recibidos)
        x = requests.post(url,data = recibidos)
        
        
        #Feather Flujo
        pedir =rfm9x2.send("Data!16",16,with_ack = True) 
        recibidos2 = rfm9x2.receive(with_ack = True)
        try:
            if recibidos2 != None and recibidos2 != "1,":
                now = datetime.now()
                dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
                rec_2 = recibidos2.split("/")
                recibidos2 = send = {rec_2[0]+rec_2[1]}
                rec2=rec_2[1]
                #x = requests.post(url,data = recibidos2)
                #print(recibidos2)
                print("Volumen totalizado=",rec2[0]+rec2[1]+rec2[2]+rec2[3]+rec2[4])
                #print(rec)
                #print(x)
        except:
            print("Mensaje Desconocido del feather de flujo")
        
        #Estacion de calidad
        recibidos1 = rfm9x1.receive(with_ack = True)
        try:
            if recibidos1 != None and recibidos1 != "1,":
                rec1 = recibidos1.split(",")
                print( recibidos1 )
                recibidos1 = send = {"id_device": rec1[0], "created_at": dt_string, "Turbidity": rec1[2], "DissolvedSolids":rec1[3], "WaterLevel": rec1[4], "pH": rec1[5], "Temperature": rec1[6], "Flow": rec2[0]+rec2[1]+rec2[2]+rec2[3]+rec2[4] , "Conductivity": rec1[8], "Salinity": rec1[9]}
                x = requests.post(url_1,data = recibidos1)
                print(recibidos1)
                print(x)
        except:
            print("Mensaje Desconocido de la estacion de calidad")
        
        
        
        
        
        
        time.sleep(20.0)
    main()

if __name__ == "__main__":
    main()
main()