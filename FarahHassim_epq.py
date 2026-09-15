# Part 1 - Economic Production Quantity (EPQ) 

#1. EPQ is used when  you manufacture your own stock rather than ordering it from a supplier.
# the holding cost part of the calculation changes

# This model calculates the Economic Production Quantity (EPQ) - the optimal
# batch size to produce in-house when stock is manufactured gradually rather than
# ordered all at once. It also works out how many production runs are
# needed per year and the maximum inventory level reached during each run.

#2. EPQ Formula

#3. Step by step process
print("3. Step by step process")
#1) import math module
import math

#2) Define inputs
#units per year
annual_demand = 12000
#cost per production run, in Rand       
setup_cost = 50 
#cost per unit per year, in Rand            
holding_cost = 2  
#units produced/sold per day          
daily_demand_rate = 40    
#units your process can make per day  
daily_production_rate = 100

#3) EPQ Function
def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
    return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate)))

print("Results")
epq = calculate_epq(annual_demand, setup_cost, holding_cost, 
                    daily_demand_rate, daily_production_rate)

print("Optimal production quantity:", round(epq, 2))

#4) Calculate production runs per year and run length
runs_per_year = annual_demand / epq
run_length_days = epq / daily_production_rate

print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run (days):", round(run_length_days, 1))

#5) Calculate maximum inventory level 
max_inventory = epq * (1 - daily_demand_rate / daily_production_rate)
print("Maximum inventory level:", round(max_inventory, 2))

print("=====================================================================")
#4. Worked Example
print("4. Worked example")

annual_demand = 12000        
setup_cost = 50             
holding_cost = 2           
daily_demand_rate = 40      
daily_production_rate = 100 

def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
 return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate)))

epq = calculate_epq(annual_demand, setup_cost, holding_cost,
                   daily_demand_rate, daily_production_rate)
runs_per_year = annual_demand / epq
run_length_days = epq / daily_production_rate
max_inventory = epq * (1 - daily_demand_rate / daily_production_rate)

print("Results")
print("Optimal production quantity:", round(epq, 2))
print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run (days):", round(run_length_days, 1))
print("Maximum inventory level:", round(max_inventory, 2))

print("=====================================================================")
#5. Try it yourself
print("5.  ")
print("1) Try it yourself")
#1)
annual_demand = 12000       
setup_cost = 50             
holding_cost = 2           
daily_demand_rate = 40     
daily_production_rate = 150 #increaseed the value therfore indicates a faster machine

def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
 return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate)))

epq = calculate_epq(annual_demand, setup_cost, holding_cost,daily_demand_rate, 
                    daily_production_rate)
runs_per_year = annual_demand / epq
run_length_days = epq / daily_production_rate
max_inventory = epq * (1 - daily_demand_rate / daily_production_rate)

print("Results")
print("Optimal production quantity:", round(epq, 2))
print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run (days):", round(run_length_days, 1))
print("Maximum inventory level:", round(max_inventory, 2))

print("The EPQ decreases from 1000.0 in the worked example to 904.53 ")
print("When the p value increases,  the denominator, (1 - d_rate/p_rate) gets bigger resulting in a smaller EPQ value")

print("           ")
print("2) Try It Yourself ")

#2) 
def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
 return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate)))

annual_demand = 12000
setup_cost = 50
holding_cost = 2
daily_demand_rate = 40
daily_production_rate = 100000

epq = calculate_epq(annual_demand, setup_cost, holding_cost,
                   daily_demand_rate, daily_production_rate)
runs_per_year = annual_demand / epq
run_length_days = epq / daily_production_rate
max_inventory = epq * (1 - daily_demand_rate / daily_production_rate)

print("Results")
print("Optimal production quantity:", round(epq, 2))
print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run (days):", round(run_length_days, 1))
print("Maximum inventory level:", round(max_inventory, 2))

print("The p value is larger when compared to the d value.")
print("Therefore so gradual replenishment (EPQ) behaves the same as instant replenishment (EOQ).")
print("A very fast production rate means the whole batch is made almost instantly, like an EOQ order arriving all at once")

