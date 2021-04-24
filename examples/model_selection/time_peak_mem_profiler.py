# Import the file to be used by the cProfiler
#import plot_dict_face_patches

# Import needed libraries --Do not change
import os
import cProfile, pstats
import io
from prettytable import PrettyTable
import csv

filename = "plot_validation_curve.py"
################# Memory profiling #################

print ("...Memory Profiling...")
os.system('mprof run --python --interval 0.01 --output memory_profiling.txt plot_validation_curve.py')
profiling_text = open(r"memory_profiling.txt", "r")
max_memory = 0    
for line in profiling_text:
    for part in line.split():
        x = line.split()
        if x[1] != '/usr/bin/python3':              # At the first line in x[1] is always the "/usr/bin/python3"
            if float(x[1]) > max_memory:
                max_memory = float(x[1])
#print ("************** Peak Memory (MB): ", max_memory, " **************")
# Delete the output txt file 
os.system('rm memory_profiling.txt')
#print ("memory_profiling.txt Deleted Succesfully")


################# Time Profiling #################

print ("...Time Profiling...")
profiler = cProfile.Profile()
profiler.enable()
exec(open(filename).read())
profiler.disable()
s=io.StringIO()

# Output the results at the CLI:
#stats = pstats.Stats(profiler).sort_stats('ncalls')
#stats.print_stats()

# Write the results in a txt file 
with open('time_profiling.txt', 'w+') as f:
    ps = pstats.Stats(profiler, stream=f)
    ps.sort_stats('ncalls')
    ps.print_stats()

# Open the txt file and read only the total time in first line
time_profiler = open(r'time_profiling.txt', "r")
time = 0
for i,line in enumerate(time_profiler):
    if i==0:                                #first line
        x=line.split()
        j=0
        while True:
            if x[j] == "in":
                break
            else: j += 1

        time = x[j+1]

#print ("************** Total Time (s): ", x[4]," **************")

# Delete the output txt file 
os.system('rm time_profiling.txt')
#print ("time_profiling.txt Deleted Succesfully")

t = PrettyTable(['Function', 'Peak Memory (MB)', 'Time (s)'])
t.add_row([filename, max_memory, time])
print(t)

# Edit the csv file
creator = open('/home/giannos/Desktop/Energy_Profiling_Details_CSV.csv', 'a+')            # Create it if it does not exist

with open('/home/giannos/Desktop/Energy_Profiling_Details_CSV.csv', 'r', newline='')as f: # Count the number of lines
    lines_count = len(f.readlines())
    #print (lines_count)
  
with open('/home/giannos/Desktop/Energy_Profiling_Details_CSV.csv', 'a+', newline='' )as f:
        thewriter=csv.writer(f)  
        thereader=csv.reader(f)
        if lines_count < 1:                                                         # if the first line is null
            thewriter.writerow(['PyScript', 'Total Memory(MB)','Total Time(s)'])
            thewriter.writerow([filename, max_memory,time])
        else:
            thewriter.writerow([filename, max_memory,time])

            

