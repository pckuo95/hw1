# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107012045.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)

#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
# Retrive ten data points from the beginning.


# Return sum of all of HUMD value in input data
# If no data input, return value '-1' for error 
def sumHUMD(target_data):
    totalHUMD = 0.0
    i = 0
    if (len(target_data) == 0):
        totalHUMD = -1.0
    while i < len(target_data):
        HUMD = target_data[i].get('HUMD')
        totalHUMD += float(HUMD)
        i = i + 1
    return totalHUMD

#remove useless data and cal HUMD sum 
target_data = list(filter(lambda item: item['station_id'] == 'C0A880' and \
     item['HUMD'] != '-99.000' and item['HUMD'] != '-999.000', data))
C0A880 = sumHUMD(target_data)

target_data = list(filter(lambda item: item['station_id'] == 'C0F9A0' and \
     item['HUMD'] != '-99.000' and item['HUMD'] != '-999.000', data))
C0F9A0 = sumHUMD(target_data)

target_data = list(filter(lambda item: item['station_id'] == 'C0G640' and \
     item['HUMD'] != '-99.000' and item['HUMD'] != '-999.000', data))
C0G640 = sumHUMD(target_data)

target_data = list(filter(lambda item: item['station_id'] == 'C0R190' and \
     item['HUMD'] != '-99.000' and item['HUMD'] != '-999.000', data))
C0R190 = sumHUMD(target_data)

target_data = list(filter(lambda item: item['station_id'] == 'C0X260' and \
     item['HUMD'] != '-99.000' and item['HUMD'] != '-999.000', data))
C0X260 = sumHUMD(target_data)
#=======================================
# Part. 4
#=======================================
# Print result
if (C0A880 >= 0):
    print("[['C0A880',",C0A880,"],")
else:
    print("[['C0A880','None'],")

if (C0F9A0 >= 0):
    print("['C0F9A0',",C0F9A0,"],")
else:
    print("['C0F9A0','None'],")

if (C0G640 >= 0):
    print("['C0G640',",C0G640,"],")
else:
    print("['C0G640','None'],")

if (C0R190 >= 0):
    print("['C0R190',",C0R190,"],")
else:
    print("['C0R190','None'],")

if (C0X260 >= 0):
    print("['C0X260',",C0X260,"]],\n")
else:
    print("['C0X260','None']],\n")            
#========================================