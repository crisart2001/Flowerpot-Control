#Captura de datos
import statistics
from statistics import mean
import time
import requests
import json


url = "http://201.207.53.225:3031/api/biocarbon/"
valores=['','','']
valores1=['','','']


baja_humedad=15.00
alta_humedad=20.00
sleep_time=900 #15 minutos

def activar_linea(numero_linea):
    #numero_linea
    try:
        #y = requests.get(url+"Relay/"+numero_linea) #Estado de linea de agua
        #if( y == 'OFF'):
        command = "Relays/ON/"+numero_linea
        requests.get(url+command)
        print('Se activo la linea '+numero_linea)
        time.sleep(20)
        return
        #else :
            #print('La linea '+numero_linea+' ya estaba activa se mantiene asi')
            #return
    except:
        print('No se pudo activar la linea'+numero_linea)
        return

def desactivar_linea(numero_linea):
    try:
        #numero_linea
        #y = requests.get(url+"Relay/"+numero_linea) #Estado de linea de agua
        #if( y == 'ON'):
        command = "Relays/OFF/"+numero_linea
        requests.get(url+command)
        print('Se desactivo la linea '+numero_linea)
        time.sleep(20)
        return
        #else :
            #print('La linea '+numero_linea+' ya estaba desactivada se mantiene asi')
            #return
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
            if((valores[0]!=None) and (valores[1]!=None) and (valores[2]!=None)):
                if(((valores[0]-valores[1])>10) or ((valores[0]-valores[1])<-10)):
                    if((valores[0]-valores[2]>10) or (valores[0]-valores[2]<-10)):
                        valores1[0]=None
                        print('La maseta 23 se comporta de forma no esperada.')
                elif(valores[1]-valores[0]>10 or valores[1]-valores[0]<-10):
                    if(valores[1]-valores[2]>10 or valores[1]-valores[2]<-10):
                        valores1[1]=None
                        print('La maseta 24 se comporta de forma no esperada.')
                elif(valores[2]-valores[0]>10 or valores[2]-valores[0]<-10):
                    if(valores[2]-valores[1]>10 or valores[2]-valores[1]<-10):
                        valores[2]=None
                        print('La maseta 25 se comporta de forma no esperada.')
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
            if((valores[0]!=None) and (valores[1]!=None) and (valores[2]!=None)):
                if(valores[0]-valores[1]>10 or valores[0]-valores[1]<-10):
                    if(valores[0]-valores[2]>10 or valores[0]-valores[2]<-10):
                        valores[0]=None
                        print('La maseta 33 se comporta de forma no esperada.')
                if(valores[1]-valores[0]>10 or valores[1]-valores[0]<-10):
                    if(valores[1]-valores[2]>10 or valores[1]-valores[2]<-10):
                        valores[1]=None
                        print('La maseta 34 se comporta de forma no esperada.')
                if(valores[2]-valores[0]>10 or valores[2]-valores[0]<-10):
                    if(valores[2]-valores[1]>10 or valores[2]-valores[1]<-10):
                        valores[2]=None
                        print('La maseta 35 se comporta de forma no esperada.')
            prom_2=mean(d for d in valores if d is not None)
            print(prom_2)
        except:
            prom_2=None
            
        #Masetas 45, 46, 47
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
            if((valores[0]!=None) and (valores[1]!=None) and (valores[2]!=None)):
                if(valores[0]-valores[1]>10 or valores[0]-valores[1]<-10):
                    if(valores[0]-valores[2]>10 or valores[0]-valores[2]<-10):
                        valores[0]=None
                        print('La maseta 45 se comporta de forma no esperada.')
                if(valores[1]-valores[0]>10 or valores[1]-valores[0]<-10):
                    if(valores[1]-valores[2]>10 or valores[1]-valores[2]<-10):
                        valores[1]=None
                        print('La maseta 46 se comporta de forma no esperada.')
                if(valores[2]-valores[0]>10 or valores[2]-valores[0]<-10):
                    if(valores[2]-valores[1]>10 or valores[2]-valores[1]<-10):
                        valores[2]=None
                        print('La maseta 47 se comporta de forma no esperada.')
            prom_3=mean(d for d in valores if d is not None)
            print(prom_3)
        except:
            prom_3=None


        #Promedio de promedios y condiciones
        try:
            valores=[prom_1,prom_2,prom_3]
            print(valores)
            if((valores[0]!=None) and (valores[1]!=None) and (valores[2]!=None)):
                if(valores[0]-valores[1]>10 or valores[0]-valores[1]<-10):
                    if(valores[0]-valores[2]>10 or valores[0]-valores[2]<-10):
                        valores[0]=None
                        print('Las masetas 23, 24 y 25 estan mostrando datos inesperados por lo tanto no serán tomadas en cuenta.')
                if(valores[1]-valores[0]>10 or valores[1]-valores[0]<-10):
                    if(valores[1]-valores[2]>10 or valores[1]-valores[2]<-10):
                        valores[1]=None
                        print('Las masetas 33, 34 y 35 estan mostrando datos inesperados por lo tanto no serán tomadas en cuenta.')
                if(valores[2]-valores[0]>10 or valores[2]-valores[0]<-10):
                    if(valores[2]-valores[1]>10 or valores[2]-valores[1]<-10):
                        valores[2]=None
                        print('Las masetas 45, 46 y 47 estan mostrando datos inesperados por lo tanto no serán tomadas en cuenta.')
            prom_prom=mean(d for d in valores if d is not None)
            print('Promedio de promedios',prom_prom)
            return prom_prom
        except:
            return 'No funcional'

def lectura_1F_con_promedios():
    #Tratamiento 1F biocarbono 
        #Masetas 26,27,28 Caja I sensor(es) E(5) y Caja J sensor(es) ED(5,4)
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
            if((valores[0]!=None) and (valores[1]!=None) and (valores[2]!=None)):
                if((valores[0]!=None) and (valores[1]!=None) and (valores[2]!=None)):
                    if(valores[0]-valores[1]>10 or valores[0]-valores[1]<-10):
                        if(valores[0]-valores[2]>10 or valores[0]-valores[2]<-10):
                            valores[0]=None
                            print('La maseta 26 se comporta de forma no esperada.')
                    if(valores[1]-valores[0]>10 or valores[1]-valores[0]<-10):
                        if(valores[1]-valores[2]>10 or valores[1]-valores[2]<-10):
                            valores[1]=None
                            print('La maseta 27 se comporta de forma no esperada.')
                    if(valores[2]-valores[0]>10 or valores[2]-valores[0]<-10):
                        if(valores[2]-valores[1]>10 or valores[2]-valores[1]<-10):
                            valores[2]=None
                            print('La maseta 28 se comporta de forma no esperada.')
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
            if((valores[0]!=None) and (valores[1]!=None) and (valores[2]!=None)):
                if((valores[0]!=None) and (valores[1]!=None) and (valores[2]!=None)):
                    if(valores[0]-valores[1]>10 or valores[0]-valores[1]<-10):
                        if(valores[0]-valores[2]>10 or valores[0]-valores[2]<-10):
                            valores[0]=None
                            print('La maseta 41 se comporta de forma no esperada.')
                    if(valores[1]-valores[0]>10 or valores[1]-valores[0]<-10):
                        if(valores[1]-valores[2]>10 or valores[1]-valores[2]<-10):
                            valores[1]=None
                            print('La maseta 42 se comporta de forma no esperada.')
                    if(valores[2]-valores[0]>10 or valores[2]-valores[0]<-10):
                        if(valores[2]-valores[1]>10 or valores[2]-valores[1]<-10):
                            valores[2]=None
                            print('La maseta 43 se comporta de forma no esperada.')
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
            if((valores[0]!=None) and (valores[1]!=None) and (valores[2]!=None)):
                if((valores[0]!=None) and (valores[1]!=None) and (valores[2]!=None)):
                    if(valores[0]-valores[1]>10 or valores[0]-valores[1]<-10):
                        if(valores[0]-valores[2]>10 or valores[0]-valores[2]<-10):
                            valores[0]=None
                            print('La maseta 53 se comporta de forma no esperada.')
                    if(valores[1]-valores[0]>10 or valores[1]-valores[0]<-10):
                        if(valores[1]-valores[2]>10 or valores[1]-valores[2]<-10):
                            valores[1]=None
                            print('La maseta 54 se comporta de forma no esperada.')
                    if(valores[2]-valores[0]>10 or valores[2]-valores[0]<-10):
                        if(valores[2]-valores[1]>10 or valores[2]-valores[1]<-10):
                            valores[2]=None
                            print('La maseta 55 se comporta de forma no esperada.')
            prom_3=mean(d for d in valores if d is not None)
            print(prom_3)
        except:
            prom_3=None

        #Promedio de promedios y condiciones
        try:    
            valores=[prom_1,prom_2,prom_3]
            if((valores[0]!=None) and (valores[1]!=None) and (valores[2]!=None)):
                if(valores[0]-valores[1]>10 or valores[0]-valores[1]<-10):
                    if(valores[0]-valores[2]>10 or valores[0]-valores[2]<-10):
                        valores[0]=None
                        print('Las masetas 26, 27 y 28 estan mostrando datos inesperados por lo tanto no serán tomadas en cuenta.')
                if(valores[1]-valores[0]>10 or valores[1]-valores[0]<-10):
                    if(valores[1]-valores[2]>10 or valores[1]-valores[2]<-10):
                        valores[1]=None
                        print('Las masetas 41, 42 y 43 estan mostrando datos inesperados por lo tanto no serán tomadas en cuenta.')
                if(valores[2]-valores[0]>10 or valores[2]-valores[0]<-10):
                    if(valores[2]-valores[1]>10 or valores[2]-valores[1]<-10):
                        valores[2]=None
                        print('Las masetas 53, 54 y 55 estan mostrando datos inesperados por lo tanto no serán tomadas en cuenta.')
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
            if((valores[0]!=None) and (valores[1]!=None) and (valores[2]!=None)):
                if(valores[0]-valores[1]>10 or valores[0]-valores[1]<-10):
                    if(valores[0]-valores[2]>10 or valores[0]-valores[2]<-10):
                        valores[0]=None
                        print('La maseta 37 se comporta de forma no esperada.')
                if(valores[1]-valores[0]>10 or valores[1]-valores[0]<-10):
                    if(valores[1]-valores[2]>10 or valores[1]-valores[2]<-10):
                        valores[1]=None
                        print('La maseta 38 se comporta de forma no esperada.')
                if(valores[2]-valores[0]>10 or valores[2]-valores[0]<-10):
                    if(valores[2]-valores[1]>10 or valores[2]-valores[1]<-10):
                        valores[2]=None
                        print('La maseta 39 se comporta de forma no esperada.')
            prom_1=mean(d for d in valores if d is not None)
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
            if((valores[0]!=None) and (valores[1]!=None) and (valores[2]!=None)):
                if(valores[0]-valores[1]>10 or valores[0]-valores[1]<-10):
                    if(valores[0]-valores[2]>10 or valores[0]-valores[2]<-10):
                        valores[0]=None
                        print('La maseta 50 se comporta de forma no esperada.')
                if(valores[1]-valores[0]>10 or valores[1]-valores[0]<-10):
                    if(valores[1]-valores[2]>10 or valores[1]-valores[2]<-10):
                        valores[1]=None
                        print('La maseta 51 se comporta de forma no esperada.')
                if(valores[2]-valores[0]>10 or valores[2]-valores[0]<-10):
                    if(valores[2]-valores[1]>10 or valores[2]-valores[1]<-10):
                        valores[2]=None
                        print('La maseta 52 se comporta de forma no esperada.')
            prom_2=mean(d for d in valores if d is not None)
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
            print("2F")
            print(valores)
            if(valores[0]-valores[1]>10 or valores[0]-valores[1]<-10):
                print('Las masetas 37, 38 y 39 y las masetas 50, 51 y 52 están mostrando datos muy diferentes.')
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
            if((valores[0]!=None) and (valores[1]!=None) and (valores[2]!=None)):
                if(valores[0]-valores[1]>10 or valores[0]-valores[1]<-10):
                    if(valores[0]-valores[2]>10 or valores[0]-valores[2]<-10):
                        valores[0]=None
                        print('La maseta 17 se comporta de forma no esperada.')
                if(valores[1]-valores[0]>10 or valores[1]-valores[0]<-10):
                    if(valores[1]-valores[2]>10 or valores[1]-valores[2]<-10):
                        valores[1]=None
                        print('La maseta 22 se comporta de forma no esperada.')
                if(valores[2]-valores[0]>10 or valores[2]-valores[0]<-10):
                    if(valores[2]-valores[1]>10 or valores[2]-valores[1]<-10):
                        valores[2]=None
                        print('La maseta 36 se comporta de forma no esperada.')
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
            if((valores[0]!=None) and (valores[1]!=None)):
                if(valores[0]-valores[1]>10 or valores[0]-valores[1]<-10):
                    print('Las maseta 40 y 49 se comporta de forma no esperada.')
            prom_2=mean(d for d in valores if d is not None)
            print(prom_2)
        except:
            prom_2=None
            
        #Promedio de promedios y condiciones
        try: 
            valores=[prom_1,prom_2]
            if((valores[0]!=None) and (valores[1]!=None)):
                if(valores[0]-valores[1]>10 or valores[0]-valores[1]<-10):
                    print('Las masetas 17, 22 y 36 y las masetas 40 y 49 están mostrando datos muy diferentes.')
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
        #Masetas 32,44,48
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
            if((valores[0]!=None) and (valores[1]!=None) and (valores[2]!=None)):
                if(valores[0]-valores[1]>10 or valores[0]-valores[1]<-10):
                    if(valores[0]-valores[2]>10 or valores[0]-valores[2]<-10):
                        valores[0]=None
                        print('La maseta 32 se comporta de forma no esperada.')
                if(valores[1]-valores[0]>10 or valores[1]-valores[0]<-10):
                    if(valores[1]-valores[2]>10 or valores[1]-valores[2]<-10):
                        valores[1]=None
                        print('La maseta 44 se comporta de forma no esperada.')
                if(valores[2]-valores[0]>10 or valores[2]-valores[0]<-10):
                    if(valores[2]-valores[1]>10 or valores[2]-valores[1]<-10):
                        valores[2]=None
                        print('La maseta 48 se comporta de forma no esperada.')
            print("BCCOM")
            print(valores)
            prom_1=mean(d for d in valores if d is not None)
            print('Promedio de promedios',prom_1)
            return prom_1
        except:
            return 'No funcional'
        
def analisis_de_condiciones():
    try:
        try:
            x = lectura_0F_con_promedios()
            if(   x < baja_humedad      ):
                     activar_linea('1')
            elif( x > alta_humedad      ):
                    desactivar_linea('1')
        except:
            print('Todas las cajas del tratamiento 0F no estan funcionando')
        try:
            x = lectura_1F_con_promedios()
            if(   x < baja_humedad       ):
                     activar_linea('2')
            elif( x > alta_humedad       ):
                    desactivar_linea('2')
        except:
            print('Todas las cajas del tratamiento 1F no estan funcionando')
        try:
            x = lectura_2F_con_promedios()
            print(x)
            if(  x < baja_humedad       ):
                     activar_linea('3')
            elif( x > alta_humedad      ):
                    desactivar_linea('3')
        except:
            print('Todas las cajas del tratamiento 2F no estan funcionando')
        try:
            x = lectura_bc_con_promedios()
            if( x < baja_humedad):
                     activar_linea('4')
            elif( x > alta_humedad ):
                    desactivar_linea('4')
        except:
            print('Todas las cajas del tratamiento BC no estan funcionando')
        try:
            x = lectura_bccom_con_promedios()
            if( x < baja_humedad):
                     activar_linea('5')
            elif( x > alta_humedad ):
                    desactivar_linea('5')
        except:
            print('Todas las cajas del tratamiento BC+COM no estan funcionando')
    except:
        print('Error en analisis')
    time.sleep(sleep_time) #15 minutos para muestrear
    analisis_de_condiciones()
    return

analisis_de_condiciones()
