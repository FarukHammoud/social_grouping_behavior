import numpy as np
from individual import Individual,Individual_2DSimu
import matplotlib.pyplot as plt

class Society():
    def __init__(self,pop_size,n_features,variation_velocity,improvement_rate):
        self.N = pop_size
        self.n = n_features
        self.S = []
        self.alpha = np.random.rand(self.N,self.N)
        for i in range(self.N):
            self.alpha[i] = self.alpha[i]/np.sum(self.alpha[i])
        self.gamma_1 = variation_velocity
        self.gamma_2 = improvement_rate
        for i in range(self.N):
            f = 2*np.random.rand(self.n)-1
            w = 2*np.random.rand(self.n)-1
            w /= np.linalg.norm(w)
            self.S.append(Individual(i,f,w))

    def __str__(self):
        print("Social Proximity:")
        print(self.alpha)
        print("Ranking Parameters:")
        for i in range(self.N):
            print(self.S[i].w)
        print("Grades:")
        for i in range(self.N):
            for j in range(self.N):
                print(self.S[i].G(self.S[j].f),end= ' | ')
            print()
        print("Features:")
        for i in range(self.N):
            print(self.S[j].f,end= ' | ')
        print() 
        return ''

    def communication(self,dt):
        for i in range(self.N):
            for k in range(self.n):
                dw = 0
                for j in range(self.N):
                    dw += self.alpha[i][j]*(self.S[i].f[k]-self.S[j].f[k])
                self.S[i].w += dt*self.gamma_1*dw
                self.S[i].w /= np.linalg.norm(self.S[i].w)
            
    def social_proximity(self,dt):
        for i in range(self.N):
            alpha_i = np.zeros(self.N)
            for j in range(self.N):
                # Direct
                direct = self.alpha[i][j]*self.S[i].G(self.S[j].f)
                # First-order Induzed
                induced = 0
                for k in range(self.N):
                    if not k == i and not k == j:
                        induced += self.alpha[i][k]*self.alpha[k][j]*self.S[i].G(self.S[j].f)

                alpha_i[j] = np.sqrt(np.amax([0.0,direct+induced]))
            self.alpha[i] = alpha_i/np.sum(alpha_i)

    def features_improvement(self,dt):
        for i in range(self.N):
            self.S[i].f = dt*self.gamma_2*self.S[i].w + (1-dt*self.gamma_2)*self.S[i].f
    def run(self,dt):
        self.communication(dt)
        self.social_proximity(dt)
        self.features_improvement(dt)
    def simulate(self,T=10,n=100):
        dt = T/n
        for step in range(n):
            self.run(dt)

class Society_2DSimu(Society):

    def __init__(self,widget,pop_size,n_features,variation_velocity,improvement_rate):
        super().__init__(pop_size,n_features,variation_velocity,improvement_rate)
        self.S = []
        for i in range(self.N):
            f = 2*np.random.rand(self.n)-1
            w = 2*np.random.rand(self.n)-1
            w /= np.linalg.norm(w)
            self.S.append(Individual_2DSimu(widget,self.N,i,f,w))
        self.widget = widget

    def draw_social_proximity(self):
        m = np.max(self.alpha)
        for i in range(self.N):
            for j in range(self.N):
                if self.alpha[i][j] != 0:
                    if self.alpha[i][j] <= 0.5*m:
                        self.widget.stroke(255,int(510*(self.alpha[i][j]/m)),0)
                    else:
                        self.widget.stroke(int(255*(self.alpha[i][j]/m-0.5)),255,0)
                    if i < j:
                        self.widget.line(self.S[i].x-3,self.S[i].y-3,self.S[j].x-3,self.S[j].y-3)
                    if i > j:
                        self.widget.line(self.S[i].x+3,self.S[i].y+3,self.S[j].x+3,self.S[j].y+3)
    def show(self,f):
        self.widget.background(0)
        self.draw_social_proximity()
        for i in range(self.N):
            self.S[i].show(f)
    
    def simulate(self,n=100):
        dt = 0.01
        for step in range(n):
            print(step)
            self.run(dt)
            self.show(0)
            self.widget.redraw()
