from society import Society_2DSimu
from processing_py import *
from heatmap import heatmap

widget = App(800,500)

S = Society_2DSimu(widget,8,3,50,25) #pop_size,n_features,variation_velocity,improvement_rate

def main():
    S.simulate(100) 
    heatmap(S.alpha)
main()


