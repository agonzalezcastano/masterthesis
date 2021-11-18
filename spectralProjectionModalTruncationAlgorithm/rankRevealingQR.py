import numpy as np
import scipy.linalg as la

def calculateRankRevealingQ(P):
    Q, R, perm = la.qr(P, pivoting = True)
    return Q