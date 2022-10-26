import statistics
from statistics import mean
def manejo (x,y,z,cm1,cm2,cm3):
    lista = [x,y,z]
    if((lista[0]!=None) and (lista[1]!=None) and (lista[2]!=None)):
        if(lista[0]>100):
            lista[0]=None
            print('La maseta '+cm1+' no tiene dato porcentual.')
            return lista
        if(lista[1]>100):
            lista[1]=None
            print('La maseta '+cm2+' no tiene dato porcentual.')
            return lista
        if(lista[2]>100):
            lista[2]=None
            print('La maseta '+cm3+' no tiene dato porcentual.')
            return lista
        if(lista[0]-lista[1]>10 or lista[0]-lista[1]<-10):
            if(lista[0]-lista[2]>10 or lista[0]-lista[2]<-10):
                lista[0]=None
                print('La maseta '+cm1+' se comporta de forma no esperada.')
                return lista
        elif(lista[1]-lista[0]>10 or lista[1]-lista[0]<-10):
            if(lista[1]-lista[2]>10 or lista[1]-lista[2]<-10):
                lista[1]=None
                print('La maseta '+cm2+' se comporta de forma no esperada.')
                return lista
        elif(lista[2]-lista[0]>10 or lista[2]-lista[0]<-10):
            if(lista[2]-lista[1]>10 or lista[2]-lista[1]<-10):
                lista[2]=None
                print('La maseta '+cm3+' se comporta de forma no esperada.')
                return lista
        else:
            return lista
    else:
        if(lista[0]==None):
            print('La maseta '+cm1+' no esta enviando datos válidos.')
            return lista
        if(lista[1]==None):
            print('La maseta '+cm2+' no esta enviando datos válidos.')
            return lista
        if(lista[2]==None):
            print('La maseta '+cm3+' no esta enviando datos válidos.')
            return lista
a=10    
b=5
c=None
listagg =manejo (a,b,c,'23','24','25')
print(listagg)
prom_1=mean(d for d in listagg if d is not None)
print(prom_1)