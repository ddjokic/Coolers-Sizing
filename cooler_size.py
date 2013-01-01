#!/usr/bin/env python
## Fresh Water Coolers Sizing Script
import math

def get_integer(message, default):
#get integer number - error check included
	try:
		f=input (message)
		st=type(f)
		if f==0:
			f=default
			return f
		elif f==" ":
			f=default
			return f
		else:
			return int(f)
	except:
		print("Wrong Input! Try again")
		return(get_integer(message, default))
        
def get_float(message, default):
#get float number - error check included
	try:
		f=input (message)
		st=type(f)
		if f==0:
			f=default
			return f
		elif f==" ":
			f=default
			return f
		else:
			return float(f)
	except:
		print("Wrong Input! Try again")
		return(get_float(message, default))
		
def get_tag ():
# get equipment tag info
	tag=raw_input("Enter Tag: ")
	return tag
	
def get_desc():
#get human description of equipment
	desc=raw_input("Enter Description: ")
	return desc
	
def get_temp_hot():
# hot fluid data
	temp_hot_in=get_float("Enter Hot Fluid Inlet Temperature or press '0' for default of 35 degC: ", 35.0)
	temp_hot_out=get_float("Enter Hot Fluid Outlet Temperature or press '0' for default of 60 degC: ", 60.0) 
	dtemp_hot=temp_hot_out-temp_hot_in
	return dtemp_hot
	
def get_flow_hot():
# flow of hot fluid
	flow_hot_fluid=get_float("Enter Hot Fluid Flow or press '0' for default of 20 cum/h: ", 20.0)
	return flow_hot_fluid
	
def sum_list(list_name):
# calculating summ of various lists
	return float(sum(list_name))
	
def write_file (file, message, var):
	fn.write ("\n")
	fn.write (str(message))
	fn.write ("\t")
	fn.write (str(var))

pname = raw_input("Project Name: ")       #project name
			
##Cooling Fluid data
        
print "Hot Fluid Data"
cp=get_float("Specific heat of hot fluid [kj/(kg degC)]- press '0' for 4.182 (fresh water)or input data: ", 4.182)
print cp

SW=get_float("Specific weight of hot fluid [kg/cum] - press '0' for 1000 (fresh water) or input data: ", 1000.0)
print SW
print "end of hot fluid data input"

print "cold fluid data input"
cc=get_float("Specific heat of cold fluid [kj/(kg degC)]- press '0' for 3.936 (sea water) or input data: ", 3.936)
print cc

SWc=get_float("Specific weight of cold fluid [kg/cum]- press '0' for 1025 (sea water) or input data: ", 1025.0)
print SWc

dTC=get_float("Estimated temperature rise in Cold fluid after cooler [degC] - press '0' for 5degC or input data:", 5.0)

print dTC
print "end of cold data input"

print ("Cooled Equipment Data")
eq_number=get_integer("Enter Number of Cooled Equipment - press '0' for default of 3: ", 3)
print eq_number

cooler_number=get_integer("Enter Number of Coolers - press '0' for default of 1: ", 1)

##forming empty lists to hold equipment data
tag=[]
desc=[]
dtemp_hot=[]
flow_hot=[]
cap_hot=[]

##populating lists with equipment data
for item in range (1, eq_number+1):
	print ("Input Equipment Nr %s") %item
	tag.append(get_tag())
	desc.append(get_desc())
	delta_temp_hot=get_temp_hot()
	dtemp_hot.append(delta_temp_hot)
	flow_hot_ins=get_flow_hot()
	flow_hot.append(flow_hot_ins)
	cap_hot_ins=flow_hot_ins*delta_temp_hot
	cap_hot.append(cap_hot_ins)

##calculating list sums
sum_dtemp_hot=sum_list(dtemp_hot)
sum_cap_hot=sum_list(cap_hot)
sum_flow_hot=sum_list(flow_hot)

##final calculation
##calculating average deltaTemp [degC]
avrg_delta_temp=float(sum_cap_hot/sum_flow_hot)    ##check formula!!!

##calculating heat load - Hot Fluid Data Used
sum_heat_load=float(SW*sum_flow_hot*cp*avrg_delta_temp)
heat_load=sum_heat_load/cooler_number

##calculating cold fluid flow in cum/h through each cooler
flow_cold=float(3600.0*heat_load/(SWc*cc*dTC))

##calculating logarithmic mean temperature LMTD
LMTD=(avrg_delta_temp-dTC)/math.log(avrg_delta_temp/dTC)

##calculating thermal length
termal_lenght=avrg_delta_temp/LMTD
heat_load_LMTD_ratio=heat_load/LMTD

#writing input and results
filename=pname+'.txt'
fn=open(filename, 'w')
fn.write(pname)
fn.close()
fn=open(filename, 'a')
fn.write("\nCooling Fluids Data")
write_file(fn, "Specific heat of hot fluid [kJ/(kg degC)]: ", cp)
write_file(fn, "Specific weight of hot fluid [kg/cum]: ", SW)
write_file(fn, "Specific heat of cold fluid [kj/(kg degC)]: ", cc)
write_file(fn, "Specific weight of cold fluid [kg/cum]: ", SWc)
write_file(fn, "Number of coolers in a loop: ", cooler_number)
fn.write("\n")
fn.write("\nCooled Equipment Data:")
fn.write("\nTag#")
fn.write('\t Description')
fn.write('\t Coolant delta [degC] ')
fn.write('\t Hot Fluid Flow [cum/h] ')
fn.write('\t Capacity of coolant [cum*degC/h] ')
fn.write('\n')
fn.close()
#writing input equipment data
fn=open(filename, 'a')
for item in range(0, eq_number):
	fn.write('\n')
	fn.write(str(tag[item]))
	fn.write('\t')
	fn.write(str(desc[item]))
	fn.write('\t')
	fn.write(str(dtemp_hot[item]))
	fn.write('\t')
	fn.write(str(flow_hot[item]))
	fn.write('\t')
	fn.write(str(cap_hot[item]))
# writing calculation results
write_file(fn, "Average difference temperature-hot fluid [degC]: ", avrg_delta_temp)
write_file(fn, "Heat load per cooler P[kW]: ", heat_load)
write_file (fn, "Cold Fluid Flow [cum/h]: ", flow_cold)
write_file(fn, "Logaritmic Mean Temperature -LMTD: ", LMTD)
write_file(fn, "Thermal Lenght - THL: ", termal_lenght)
write_file (fn, "Heat Load-Logaritmic Mean Temperature ratio -P/LMTD: ", heat_load_LMTD_ratio)
fn.close()	
print ("Calculation executed")