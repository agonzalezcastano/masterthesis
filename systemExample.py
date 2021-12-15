import pandapower as pn
import pandapower.estimation as estimation
import pandapower.networks as pnetwork
import pandas as pd

def setGBSystemExample(time_step):
    net = pnetwork.GBnetwork()
    success = estimation.estimate(net, init="flat")
    print("NET: " + success)
    return success
    
def set30BusSystemExample():
    net = pnetwork.case_ieee30()
    success = estimation.estimate(net, init="flat")
    print("NET: " + success)
    return success

def simpleSystemExample():
    net = pnetwork.simple_plot()
    success = estimation.estimate(net, init="flat")
    print("NET: " + success)
    return success