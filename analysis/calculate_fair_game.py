# -*- coding: utf-8 -*-
"""
Created on Mon May  9 08:42:27 2022

@author: Kyle Stanley
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gameplay_calculation = \
    pd.read_csv(r"data\ConfigurationCalculations.csv")

#This is small enough that I don't really have to optimize, but it would be
#the paper cutting problem in optimization at its core.

#Total Real Estate
#Possible configurations
####At least 1 4x4
# 1 4x4, 5 2x2
# 1 4x4, 4 2x2, 4 1x1
#...
# 1 4x4, 20 1x1

#####No 4x4, at least 1 2x2
# 9 2x2
# 8 2x2, 4 1x1
#...
# 36 1x1

#What is the inducement to choose a certain machine

#start from end game to find best configurations

#set beginning of game to not be able to afford this and take steps towards

#1 Cost per load
#F1 = -Cost-(Unit Cost)*Capacity
#2 Gain per load
#F2 = (Unit Cost of Processed Material)*Capacity
#Peak Efficiency Calculation of Machine
#F3 = -Cost-(Unit Cost)*Capacity*(%TTP==0)+\
#    (Unit Cost of Processed Material)*Capacity*((%TTP==0) - (TTP==0))

#Machine
machine = "T1"

def peak_efficiency_time_series_of_machine_get_vars(
        machine, gameplay_calculation):
    machine_variables = \
        gameplay_calculation[gameplay_calculation["Machine Index"] == machine]\
            .copy()
    cost = machine_variables["Cost"].values[0]
    capacity = machine_variables["Capacity"].values[0]
    unit_cost = machine_variables["Unit Cost of Material"].values[0]
    unit_cost_processed =\
        machine_variables["Unit Cost of Processed Material"].values[0]
    turns_to_produce =  machine_variables["Turns To Produce"].values[0]
    return (cost, capacity, unit_cost, unit_cost_processed, turns_to_produce)

def peak_efficiency_time_series_function(turns, cost, capacity, unit_cost,
                                         unit_cost_processed,
                                         turns_to_produce):
    """Function which calculates $$ over time for a machine"""
    initial_cost = -cost
    turn_based_cost = -(unit_cost)*capacity*(int(turns/turns_to_produce)+1)
    turn_based_income = (unit_cost_processed)*capacity*\
        int(turns/turns_to_produce)
    #print(initial_cost)
    #print(turn_based_cost)
    #print(turn_based_income)
    return initial_cost + turn_based_cost + turn_based_income

def peak_efficiency_time_series_step_0(cost, capacity, unit_cost,
                                         unit_cost_processed,
                                         turns_to_produce):
    initial_cost = -cost
    turn_based_cost = -(unit_cost)*capacity
    return initial_cost + turn_based_cost

def peak_efficiency_time_series_array(amount_of_time_steps, machine,
                                      gameplay_calculation):
    machine_vars = peak_efficiency_time_series_of_machine_get_vars(
        machine, gameplay_calculation)
    purchase_cost = peak_efficiency_time_series_step_0(*machine_vars)
    return [purchase_cost] +\
        [peak_efficiency_time_series_function(a, *machine_vars)\
            for a in range(1, 1 + amount_of_time_steps)]

def add_multiple_small_machines(dense_df):
    
    dense_df["T1x4"] = dense_df["T1"]*4
    dense_df["E1x4"] = dense_df["E1"]*4
    dense_df["P1x4"] = dense_df["P1"]*4
    
    dense_df["T1x16"] = dense_df["T1"]*16
    dense_df["E1x16"] = dense_df["E1"]*16
    dense_df["P1x16"] = dense_df["P1"]*16

    dense_df["T2x4"] = dense_df["T2"]*4
    dense_df["E2x4"] = dense_df["E2"]*4
    dense_df["P2x4"] = dense_df["P2"]*4
    
    return dense_df
def create_peak_efficiency_analysis_df(amount_of_time_steps, machine,
                                    gameplay_calculation):
    all_machine_peak_efficiencies = {}
    for machine in gameplay_calculation["Machine Index"]:
        all_machine_peak_efficiencies[machine] = \
            peak_efficiency_time_series_array(amount_of_time_steps, machine,
                                          gameplay_calculation)
    
    all_machine_peak_efficiencies["Timestep"] =\
        list(range(1+amount_of_time_steps))
    dense_df = pd.DataFrame.from_dict(all_machine_peak_efficiencies)
    dense_df = add_multiple_small_machines(dense_df)
    peak_efficiency_df = dense_df.melt(id_vars = "Timestep")
    return peak_efficiency_df



peak_efficiency_df = create_peak_efficiency_analysis_df(40, machine,
                                    gameplay_calculation)
sns.lineplot(x = "Timestep",y = "value",hue = "variable",data = peak_efficiency_df)
plt.show()