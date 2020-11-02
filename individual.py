import numpy as np
from math import pi

class Individual():
    def __init__(self,id,features,ranking_parameters):
        self.i = id
        self.f = features
        self.w = ranking_parameters
    def G(self,features):
        return np.dot(self.w,features)
        
class Individual_2DSimu(Individual):
    def __init__(self,widget,pop_size,id,features,ranking_parameters):
        super().__init__(id,features,ranking_parameters)
        self.widget = widget
        self.N = pop_size
        self.x = 400 + 200*np.cos(id*(2*pi/self.N))
        self.y = 250 + 200*np.sin(id*(2*pi/self.N))

    def show(self,i):
        self.widget.fill(255)
        self.widget.noStroke()
        self.widget.ellipse(self.x,self.y,50,50)
        
        for i in range(len(self.f)):
            if self.f[i] <= 0:
                self.widget.fill(255,int(255*(self.f[i]+1)),0)
            else:
                self.widget.fill(int(255*(self.f[i])),255,0)
            self.widget.noStroke()
            self.widget.arc(self.x,self.y,40,40,(i*2*pi/len(self.f)),((i+1)*2*pi/len(self.f)))