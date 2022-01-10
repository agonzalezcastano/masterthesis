import scipy.linalg as la
import numpy as np

def calculateRankRevealingQ(P):
    Q, R, perm = la.qr(P, pivoting = True)
    return Q