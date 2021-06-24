import random
from random import randrange, uniform
from typing import Text
p_best=[]
g_best=[]
x1=[]
x2=[]
vi=[]
uygunluk=[]
c1=c2=2
k=10
temp=0
t=0
def first_throw():

    for i in range(k):
        x1.append(randrange(-5,5))
        x2.append(randrange(-5,5))
        Fx=4*pow(x1[i],2)-2.1*pow(x1[i],4)+1/3*pow(x1[i],6)+x1[i]*x2[i]-4*pow(x2[i],2)+4*pow(x2[i],4)
        p_best.append([x1[i],x2[i],Fx])
        uygunluk.append(Fx)
        
first_throw()      
temp=min(uygunluk)
for i in range(k):
    if(p_best[i][2]==temp):
        g_best.append(p_best[i])


def throw(vi):
    for i in range(k):
        x1[i]=x1[i]+vi[i][0]
        x2[i]=x2[i]+vi[i][1]
        Fx=4*pow(x1[i],2)-2.1*pow(x1[i],4)+1/3*pow(x1[i],6)+x1[i]*x2[i]-4*pow(x2[i],2)+4*pow(x2[i],4)
        if(uygunluk[i]>=Fx):
            p_best[i]=[x1[i],x2[i],Fx]
            uygunluk[i]=Fx
    temp=min(uygunluk)

    for i in range(k):
        if(p_best[i][2]==temp):
            g_best[0]=p_best[i]


while(g_best[0][2]>=2):
    
    for j in range(k):
       
        rnd1=random.random()
        rnd2=random.random()
        if(t<=0):
            v1=0+c1*rnd1*(p_best[j][0]-x1[j])+c2*rnd2*(g_best[0][0]-x1[j])
            v2=0+c1*rnd1*(p_best[j][1]-x2[j])+c2*rnd2*(g_best[0][1]-x2[j])
            vi.append([v1,v2])
           
        else:
        
            v1=vi[j][0]+c1*rnd1*(p_best[j][0]-x1[j])+c2*rnd2*(g_best[0][0]-x1[j])
            v2=vi[j][1]+c1*rnd1*(p_best[j][1]-x2[j])+c2*rnd2*(g_best[0][1]-x2[j])
            vi[i]=[v1,v2]


        
    throw(vi)
    t+=1
print('İstenilen Değer',g_best[0])

        
        




    
    

    



