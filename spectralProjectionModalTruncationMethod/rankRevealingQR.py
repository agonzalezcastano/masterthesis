import scipy.linalg as la
import numpy as np

def calculateRankRevealingQ(P):
    Q, R, P = la.qr(P, pivoting = True)
    return Q