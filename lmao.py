a=10
b=5
c=8
valores=[a,b,c]
valores1=["","",""]
while True:
    if(valores[0]-valores[1]>10 or valores[0]-valores[1]<-10):
        if(valores[0]-valores[2]>10 or valores[0]-valores[2]<-10):
            valores1[0]=None
            print('La maseta 32 se comporta de forma no esperada.')
    elif(valores[1]-valores[0]>10 or valores[1]-valores[0]<-10):
        if(valores[1]-valores[2]>10 or valores[1]-valores[2]<-10):
            valores1[1]=None
            print('La maseta 44 se comporta de forma no esperada.')
    elif(valores[2]-valores[0]>10 or valores[2]-valores[0]<-10):
        if(valores[2]-valores[1]>10 or valores[2]-valores[1]<-10):
            valores1[2]=None
            print('La maseta 48 se comporta de forma no esperada.')
prom_1=mean(d for d in valores if d is not None)
print(prom_1)