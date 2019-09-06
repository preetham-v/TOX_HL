#Import required directories: numpy and math required
import sys
import csv
import numpy
import math

#Take in required arguments
if len(sys.argv)!=7:
    print("Usage: "+sys.argv[0]+"python dosage.py <file_name> <number_died> <total_number> <time_period> <dosage_conc> <dosage_points>")
    sys.exit()
    
survival_file = sys.argv[1] #File which contains data on conc vs survival
crit_died = float(sys.argv[2]) #Number of mice which died during multi-dose experiment
crit_total = float(sys.argv[3]) #Total number of mice which were used during multi-dose experiment
conc_point = float(crit_died/crit_total) #Fraction of mice which died during multi-dose experiment
time_period = int(sys.argv[4]) #Time period of dosage
conc_dosage = float(sys.argv[5]) #Concentration of dosage
N_points = float(sys.argv[6]) #Number of dosages administered before witnessing first death


#Takes in input file
point_list=[] 

with open(survival_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        point_list.append(row)

for i in range(0,len(point_list)):
    point_list[i][0] = float(point_list[i][0])
    point_list[i][1] = float(point_list[i][1])

#Initializes variables
    
index_prev = 0 #Denotes the first index for linear interpolation
index_curr = 0 #Denotes the second index for linear interpolation
buff_curr = 0
buff_prev = 0
flag = 0 #Used to mark the first time when conc_point lies on linear graph
count_total = float(point_list[0][1]) #Total number of mice used in conc vs survival experiment

for j in range(0,len(point_list)):
    buff_curr = j
    if float(1-float(point_list[buff_curr][1]/count_total)) < float(1-float(point_list[buff_prev][1]/count_total)): #If graph dips and rises again, exit
        print("The number of mice survived is not decreasing with increasing concentration. Data not reliable")
        sys.exit(0)
        
    if float(1-float(point_list[buff_curr][1]/count_total)) >= float(1-float(point_list[buff_prev][1]/count_total)): #Keep searching the file
        buff_prev = j
        
    if float(1-float(point_list[buff_curr][1]/count_total)) >= conc_point and flag != 1: #Marks the points for linear interpolation
        index_curr = j
        index_prev = j-1
        flag = 1

linear_int = float((point_list[index_curr][1]-point_list[index_prev][1])/(point_list[index_curr][0]-point_list[index_prev][0])) #Slope of linear graph

N_toxic = float((((float((1-conc_point)*count_total)-point_list[index_prev][1]))/linear_int)+point_list[index_prev][0]) #Conc at which it becomes toxic

ratio = float(N_toxic/conc_dosage) #Ratio of toxic conc and administered dosage

coeff = [] #Coefficients of polynomial equation [a2,a1,a0] would denote the polynomial a2x^2 + a1x^1 + a0x^0

for i in range(0,int(N_points+1)):
    if i == 0:
        coeff.append(1)
    if i != 0 and i not in[N_points-1,N_points]:
        coeff.append(0)
    if i == N_points-1:
        coeff.append(float(-1*ratio))
    if i == N_points:
        coeff.append(float(ratio-1))

x = numpy.roots(coeff) #Magical function which returns approximate roots

real_valued = x.real[abs(x.imag)<1e-5] #This is used because choosing only those with imaginary part = 0 might make us lose roots; fault of numpy.roots approximations

proper_x = None #Variable which denotes an acceptable root

for i in real_valued:
    if i > 0 and i < 1:
        proper_x = i 

lambda_x = -1*math.log(proper_x)/time_period #Lambda in exp(-lambda*t)

t_half = math.log(2)/lambda_x #Half life

print('\n' + 'The half-life is ' str(round(t_half, 2))+ ' units of time') #Print half life
print('\n'+'Units are same as the time period input.')
            
