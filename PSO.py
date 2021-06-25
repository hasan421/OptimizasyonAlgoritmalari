import random
from random import randrange, uniform

class PSO:
    def __init__(self,c1,c2,k,esik_degeri):
        self.c1=c1
        self.c2=c2
        self.k=k
        self.temp=0
        self.t=0
        self.x1=[]
        self.x2=[]
        self.p_best=[]
        self.g_best=[]
        self.uygunluk=[]
        self.vi=[]
        self.esik_degeri=esik_degeri
    def first_throw(self):
        for i in range(self.k):
            self.x1.append(randrange(-5,5))
            self.x2.append(randrange(-5,5))
            Fx=4*pow(self.x1[i],2)-2.1*pow(self.x1[i],4)+1/3*pow(self.x1[i],6)+self.x1[i]*self.x2[i]-4*pow(self.x2[i],2)+4*pow(self.x2[i],4)
            self.p_best.append([self.x1[i],self.x2[i],Fx])
            self.uygunluk.append(Fx)
        
        temp=min(self.uygunluk)
        for i in range(self.k):
            if(self.p_best[i][2]==temp):
                self.g_best.append(self.p_best[i])


    def throw(self,vi):
        for i in range(self.k):
            self.x1[i]=self.x1[i]+self.vi[i][0]
            self.x2[i]=self.x2[i]+vi[i][1]
            Fx=4*pow(self.x1[i],2)-2.1*pow(self.x1[i],4)+1/3*pow(self.x1[i],6)+self.x1[i]*self.x2[i]-4*pow(self.x2[i],2)+4*pow(self.x2[i],4)
            if(self.uygunluk[i]>=Fx):
                self.p_best[i]=[self.x1[i],self.x2[i],Fx]
                self.uygunluk[i]=Fx
        temp=min(self.uygunluk)

        for i in range(self.k):
            if(self.p_best[i][2]==temp):

               self.g_best[0]=self.p_best[i]

    def iteration(self):

        while(self.g_best[0][2]>=self.esik_degeri):
    
            for j in range(self.k):
       
                rnd1=random.random()
                rnd2=random.random()
                if(self.t<=0):
                    v1=0+self.c1*rnd1*(self.p_best[j][0]-self.x1[j])+self.c2*rnd2*(self.g_best[0][0]-self.x1[j])
                    v2=0+self.c1*rnd1*(self.p_best[j][1]-self.x2[j])+self.c2*rnd2*(self.g_best[0][1]-self.x2[j])
                    self.vi.append([v1,v2])
           
                else:
                    v1=self.vi[j][0]+self.c1*rnd1*(self.p_best[j][0]-self.x1[j])+self.c2*rnd2*(self.g_best[0][0]-self.x1[j])
                    v2=self.vi[j][1]+self.c1*rnd1*(self.p_best[j][1]-self.x2[j])+self.c2*rnd2*(self.g_best[0][1]-self.x2[j])
                    self.vi[j]=[v1,v2]


        
            self.throw(self.vi)
            self.t+=1
        print('İstenilen Değer',self.g_best[0])

        
optimizasyon=PSO(2,2,10,2)
optimizasyon.first_throw()
optimizasyon.iteration()       




    
    

    



