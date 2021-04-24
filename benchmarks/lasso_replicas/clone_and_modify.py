# Script to clone a specific python script and rename it 
from shutil import copyfile
import sys
import os

def manipulate_the_new_script(newscript,destination,samples,features):
    list_of_lines = newscript.readlines()
    samples2 = str(samples)
    features2 = str(features)
    list_of_lines[86] = "    samples_range = np.linspace(10, " + samples2 + ", 3).astype(int) \n"      
    list_of_lines[87] = "    features_range = np.linspace(10, " + features2 + " , 3).astype(int) \n"
    newscript = open(destination, "w")
    newscript.writelines(list_of_lines)
    newscript.close()


def main(argv):
    n1 = int(sys.argv[1])        # 500 -> start value 
    n2 = int(sys.argv[2])        # 30 -> step 
    samples = n1
    features = n1
    i = 0
    ii= 0
    source = "/home/giannos/Desktop/scikit-learn/benchmarks/lasso_replicas/bench_plot_lasso_path.py"
    while samples <= 2000:  # 50 samples from here - only manipulate samples 
        samples = n1 + i*n2
        i+=1
        ii = ii+1
        j = str(ii)
        destination = "/home/giannos/Desktop/scikit-learn/benchmarks/lasso_replicas/bench_plot_lasso_path_" + j + ".py"
        copyfile(source, destination)
        # Manipulate the new script - Open it and send it
        new_script = open(destination, "r")
        manipulate_the_new_script(new_script, destination,samples,features)
        new_script.close()
        print ("Successfully created replica: bench_plot_lasso_path_" + j + ".py")
    samples = n1        # Initialize to n1
    i=0

    while features <= 2000: # 50 samples from here - only manipulate features
        features = n1 + i*n2 
        i+=1
        ii = ii+1
        j = str(ii)
        destination = "/home/giannos/Desktop/scikit-learn/benchmarks/lasso_replicas/bench_plot_lasso_path_" + j + ".py"
        copyfile(source, destination)
        # Manipulate the new script - Open it and send it
        new_script = open(destination, "r")
        manipulate_the_new_script(new_script, destination,samples,features)
        new_script.close()
        print ("Successfully created replica: bench_plot_lasso_path_" + j + ".py")
    features = n1
    i=0

    while samples <= 2000:  # 50 samplesfrom here - manipulate both samples & features  
        samples = n1 + i*n2 
        features = n1 + i*n2
        i+=1
        ii = ii+1
        j = str(ii)
        destination = "/home/giannos/Desktop/scikit-learn/benchmarks/lasso_replicas/bench_plot_lasso_path_" + j + ".py"
        copyfile(source, destination)
        # Manipulate the new script - Open it and send it
        new_script = open(destination, "r")
        manipulate_the_new_script(new_script, destination,samples,features)
        new_script.close()
        print ("Successfully created replica: bench_plot_lasso_path_" + j + ".py")
   
    #os.system("python3 bench_tree_n1_"+ n1 + "_n2_"+ n2 + ".py")

if __name__ == "__main__":
   main(sys.argv[2:])
   
