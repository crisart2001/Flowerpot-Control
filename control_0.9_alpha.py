#Captura de datos
import statistics
from statistics import mean
import time
import requests
import json


url = "http://201.207.53.225:3031/api/biocarbon/"
valores=['','','']


baja_humedad=15.00
alta_humedad=20.00
sleep_time=900 #15 minutos



def activar_linea(numero_linea):
    #numero_linea
    try:
        y = requests.get(url+"Relay/"+numero_linea) #Estado de linea de agua
        if( y == 'OFF'):
            command = "Relays/ON/"+numero_linea
            requests.get(url+command)
            print('Se activo la linea '+numero_linea)
            return
        else :
            print('La linea '+numero_linea+' ya estaba activa se mantiene asi')
            return
    except:
        print('No se pudo activar la linea'+numero_linea)
        return

def desactivar_linea(numero_linea):
    try:
        #numero_linea
        y = requests.get(url+"Relay/"+numero_linea) #Estado de linea de agua
        if( y == 'ON'):
            command = "Relays/OFF/"+numero_linea
            requests.get(url+command)
            print('Se desactivo la linea '+numero_linea)
            return
        else :
            print('La linea '+numero_linea+' ya estaba desactivada se mantiene asi')
            return
    except:
        print('No se pudo desactivar la linea'+numero_linea)
        return
    



def lectura_0F_con_promedios():
    #Tratamiento 0F biocarbono 
        #Masetas 23,24,25 Caja I sensor(es) ABC(1,2,3)
        #Masetas 33,34,35 Caja K sensor(es) CBA(3,2,1)
        #Masetas 45,46,47 Caja M sensor(es) A(1) y Caja N sensor(es) ED(5,4)
    
    #########################################################################
        valores=['','','']
        #Masetas 23,24,25
        try:
            x = requests.get(url+"LastHumidity/I")
            x = json.loads(x.text)
            try:
                valores[0]=float(x["data"]["sensora"])
            except:
                valores[0]=None
            try:
                valores[1]=float(x["data"]["sensorb"])
            except:
                valores[1]=None
            try:
                valores[2]=float(x["data"]["sensorc"])
            except:
                valores[2]=None
        except:
            valores[0]=None
            valores[1]=None
            valores[2]=None
        try:
            prom_1=mean(d for d in valores if d is not None)
            print(prom_1)
        except:
            prom_1=None
        

        #Masetas 33,34,35
        try:
            x = requests.get(url+"LastHumidity/K")
            x = json.loads(x.text)
            try:
                valores[0]=float(x["data"]["sensorc"])
            except:
                valores[0]=None
            try:
                valores[1]=float(x["data"]["sensorb"])
            except:
                valores[1]=None
            try:        
                valores[2]=float(x["data"]["sensora"])
            except:
                valores[2]=None
        except:
            valores[0]=None
            valores[1]=None
            valores[2]=None
        try:
            prom_2=mean(d for d in valores if d is not None)
            print(prom_2)
        except:
            prom_2=None
            
        #Masetas 45,46,47
        try:
            x = requests.get(url+"LastHumidity/M")
            x = json.loads(x.text)
            try:
                valores[0]=float(x["data"]["sensora"])
            except:
                valores[0]=None
        except:
            valores[0]=None            
        try:
            x = requests.get(url+"LastHumidity/N")
            x = json.loads(x.text)
            try:
                valores[1]=float(x["data"]["sensore"])
            except:
                valores[1]=None
            try:
                valores[2]=float(x["data"]["sensord"])
            except:
                valores[2]=None
        except:
            valores[1]=None
            valores[2]=None
        try:
            prom_3=mean(d for d in valores if d is not None)
            print(prom_3)
        except:
            prom_3=None


        #Promedio de promedios y condiciones
        try:
            valores=[prom_1,prom_2,prom_3]
            prom_prom=mean(d for d in valores if d is not None)
            print('Promedio de promedios',prom_prom)
            return prom_prom
        except:
            return 'No funcional'


def lectura_1F_con_promedios():
    #Tratamiento 1F biocarbono 
        #Masetas 26,27,28 Caja I sensor(es) E(5) y Caja J sensor(es) DE(5,4)
        #Masetas 41,42,43 Caja L sensor(es) CBA(3,2,1)
        #Masetas 53,54,55 Caja O sensor(es) CBA(3,2,1)

    #########################################################################
        valores=['','','']
        #Masetas 26,27,28
        try:
            x = requests.get(url+"LastHumidity/I")
            x = json.loads(x.text)
            try:
                valores[0]=float(x["data"]["sensore"])
            except:
                valores[0]=None
        except:
            valores[0]=None
        try:
            x = requests.get(url+"LastHumidity/J")
            x = json.loads(x.text)
            try:
                valores[1]=float(x["data"]["sensord"])
            except:
                valores[1]=None
            try:
                valores[2]=float(x["data"]["sensore"])
            except:
                valores[2]=None
        except:
            valores[1]=None
            valores[2]=None
        try:
            prom_1=mean(d for d in valores if d is not None)
            print(prom_1)
        except:
            prom_1=None

        #Masetas 41,42,43
        try:
            x = requests.get(url+"LastHumidity/L")
            x = json.loads(x.text)
            try:
                valores[0]=float(x["data"]["sensorc"])
            except:
                valores[0]=None
            try:
                valores[1]=float(x["data"]["sensorb"])
            except:
                valores[1]=None
            try:
                valores[2]=float(x["data"]["sensora"])
            except:
                valores[2]=None
        except:
            valores[0]=None
            valores[1]=None
            valores[2]=None
        try:
            prom_2=mean(d for d in valores if d is not None)
            print(prom_2)
        except:
            prom_2=None
            
        #Masetas 53,54,55
        try:
            x = requests.get(url+"LastHumidity/O")
            x = json.loads(x.text)
            try:
                valores[0]=float(x["data"]["sensorc"])
            except:
                valores[0]=None
            try:
                valores[1]=float(x["data"]["sensorb"])
            except:
                valores[1]=None
            try:
                valores[2]=float(x["data"]["sensora"])
            except:
                valores[2]=None
        except:
            valores[0]=None
            valores[1]=None
            valores[2]=None
        try:
            prom_3=mean(d for d in valores if d is not None)
            print(prom_3)
        except:
            prom_3=None

        #Promedio de promedios y condiciones
        try:    
            valores=[prom_1,prom_2,prom_3]
            prom_prom=mean(d for d in valores if d is not None)
            print('Promedio de promedios',prom_prom)
            return prom_prom
        except:
            return 'No funcional'

def lectura_2F_con_promedios():
    #Tratamiento 2F biocarbono 
        #Masetas 37,38,39 Caja M sensor(es) DE(4,5) y Caja J sensor(es) C(3)
        #Masetas 50,51,52 Caja N sensor(es) A(1) y Caja O sensor(es) ED(5,4)

    #########################################################################
        valores=['','','']
        #Masetas 37,38,39
        try:
            x = requests.get(url+"LastHumidity/M")
            x = json.loads(x.text)
            try:
                valores[0]=float(x["data"]["sensord"])  
            except:
                valores[0]=None
            try:
                valores[1]=float(x["data"]["sensore"])
            except:
                valores[1]=None
        except:
            valores[0]=None
            valores[1]=None
        try:
            x = requests.get(url+"LastHumidity/J")
            x = json.loads(x.text)
            try:
                valores[2]=float(x["data"]["sensorc"])
            except:
                valores[2]=None
        except:
            valores[2]=None
        
        try:
            prom_1=statistics.mean(valores)
            print(prom_1)
        except:
            prom_1=None

        #Masetas 50,51,52
        try:
            x = requests.get(url+"LastHumidity/N")
            x = json.loads(x.text)
            try:
                valores[0]=float(x["data"]["sensora"])
            except:
                valores[0]=None
        except:
            valores[0]=None
        try:
            x = requests.get(url+"LastHumidity/O")
            x = json.loads(x.text)
            try:
                valores[1]=float(x["data"]["sensore"])
            except:
                valores[1]=None
            try:
                valores[2]=float(x["data"]["sensord"])
            except:
                valores[2]=None
        except:
            valores[1]=None
            valores[2]=None
        try:
            prom_2=statistics.mean(valores)
            print(prom_2)
        except:
            prom_2=None
            
        #Masetas 53,54,55
        #x = requests.get(url+"LastHumidity/O")
        #x = json.loads(x.text)
        #valores[0]=float(x["data"]["sensorc"])
        #valores[1]=float(x["data"]["sensorb"])
        #valores[2]=float(x["data"]["sensora"])
        #prom_3=statistics.mean(valores)
        #print(prom_3)

        #Promedio de promedios y condiciones
        try: 
            valores=[prom_1,prom_2]
            prom_prom=mean(d for d in valores if d is not None)        #,prom_3])
            print('Promedio de promedios',prom_prom)
            return prom_prom
        except:
            return 'No funcional'

def lectura_bc_con_promedios():
    #Tratamiento BC biocarbono
        #Masetas 17,22,36,40,49 Caja I sensor(es) D(4), Caja K sensor(es) E(5), Caja M sensor(es) C(3), Caja L sensor(es) D(4) y Caja N sensor(es) B(2)
    
    #########################################################################
        valores=['','','']
        #Masetas 17,22,36
        try:
            x = requests.get(url+"LastHumidity/I")
            x = json.loads(x.text)
            try:
                valores[0]=float(x["data"]["sensord"])
            except:
                valores[0]=None
        except:
                valores[0]=None
        try:        
            x = requests.get(url+"LastHumidity/K")
            x = json.loads(x.text)
            try:
                valores[1]=float(x["data"]["sensore"])
            except:
                valores[1]=None
        except:
            valores[1]=None
        try:
            x = requests.get(url+"LastHumidity/M")
            x = json.loads(x.text)
            try:
                valores[2]=float(x["data"]["sensorc"]) 
            except:
                valores[2]=None
        except:
            valores[2]=None
        try:    
            prom_1=mean(d for d in valores if d is not None)
            print(prom_1)
        except:
            prom_1=None

        #Masetas 40,49
        try:
            x = requests.get(url+"LastHumidity/L")
            x = json.loads(x.text)
            try:
                valores[0]=float(x["data"]["sensord"])
            except:
                valores[0]=None
        except:
            valores[0]=None
        try:
            x = requests.get(url+"LastHumidity/N")
            x = json.loads(x.text)
            try:
                valores[1]=float(x["data"]["sensorb"])
            except:
                valores[1]=None
        except:
            valores[1]=None
        try:
            valores[2]=None
            prom_2=mean(d for d in valores if d is not None)
            print(prom_2)
        except:
            prom_2=None
            
        #Promedio de promedios y condiciones
        try: 
            valores=[prom_1,prom_2]
            prom_prom=mean(d for d in valores if d is not None)        #,prom_3])
            print('Promedio de promedios',prom_prom)
            return prom_prom
        except:
            return 'No funcional'
def lectura_bccom_con_promedios():
    #Tratamiento BC+COM biocarbono
        #Masetas 32,44,48 Caja K sensor(es) D(4), Caja M sensor(es) B(2) y Caja N sensor(es) C(3)
    
    #########################################################################
        valores=['','','']
        #Masetas 17,22,36
        try:
            x = requests.get(url+"LastHumidity/K")
            x = json.loads(x.text)
            try:
                valores[0]=float(x["data"]["sensord"])
            except:
                valores[0]=None
        except:
            valores[0]=None
        try:
            x = requests.get(url+"LastHumidity/M")
            x = json.loads(x.text)
            valores[1]=float(x["data"]["sensorb"])
        except:
            valores[1]=None
        try:
            x = requests.get(url+"LastHumidity/N")
            x = json.loads(x.text)
            try:
                valores[2]=float(x["data"]["sensorc"]) 
            except:
                valores[2]=None
        except:
            valores[2]=None
        try:
            prom_1=mean(d for d in valores if d is not None)
            print('Promedio de promedios',prom_1)
            return prom_1
        except:
            return 'No funcional'
def analisis_de_condiciones():
    try:
        try:
            if( lectura_0F_con_promedios() < baja_humedad):
                     activar_linea('1')
            elif( lectura_0F_con_promedios() > alta_humedad ):
                    desactivar_linea('1')
        except:
            print('Todas las cajas del tratamiento 0F no estan funcionando')
        try:
            if( lectura_1F_con_promedios() < baja_humedad):
                     activar_linea('2')
            elif( lectura_1F_con_promedios() > alta_humedad ):
                    desactivar_linea('2')
        except:
            print('Todas las cajas del tratamiento 1F no estan funcionando')
        try:
            if( lectura_2F_con_promedios() < baja_humedad):
                     activar_linea('3')
            elif( lectura_2F_con_promedios() > alta_humedad ):
                    desactivar_linea('3')
        except:
            print('Todas las cajas del tratamiento 2F no estan funcionando')
        try:
            if( lectura_bc_con_promedios() < baja_humedad):
                     activar_linea('4')
            elif( lectura_bc_con_promedios() > alta_humedad ):
                    desactivar_linea('4')
        except:
            print('Todas las cajas del tratamiento BC no estan funcionando')
        try:
            if( lectura_bccom_con_promedios() < baja_humedad):
                     activar_linea('5')
            elif( lectura_bccom_con_promedios() > alta_humedad ):
                    desactivar_linea('5')
        except:
            print('Todas las cajas del tratamiento BC+COM no estan funcionando')
    except:
        print('Error en analisis')
    time.sleep(sleep_time) #15 minutos para muestrear
    analisis_de_condiciones()
    return

    

analisis_de_condiciones()


