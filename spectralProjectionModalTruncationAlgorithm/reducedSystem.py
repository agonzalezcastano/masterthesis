import numpy as np

def createReducedSystem(Ar, Br, Cr, Dr):
    Gr = [[Ar, Br], [Cr, Dr]]
    return Gr