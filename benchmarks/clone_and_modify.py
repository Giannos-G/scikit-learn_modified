# Script to clone a specific python script and rename it 
from shutil import copyfile
import sys
import os

def manipulate_the_new_script(newscript,destination,n1,n2):
    list_of_lines = newscript.readlines()
    list_of_lines[69] = "    n = " + n1 + "\n"
    list_of_lines[97] = "    n = " + n2 + "\n"
    newscript = open(destination, "w")
    newscript.writelines(list_of_lines)
    newscript.close()


def main(argv):
    n1 = sys.argv[1]
    n2 = sys.argv[2]
    source = "/home/giannos/Desktop/scikit-learn/benchmarks/bench_tree.py"
    destination = "/home/giannos/Desktop/scikit-learn/benchmarks/bench_tree_n1_"+ n1 + "_n2_"+ n2 + ".py"
    copyfile(source, destination)

    # Manipulate the new script - Open it and send it
    new_script = open(destination, "r")
    manipulate_the_new_script(new_script, destination,n1,n2)
    new_script.close()
    os.system("python3 bench_tree_n1_"+ n1 + "_n2_"+ n2 + ".py")
    print ("################### bench_tree_n1_"+ n1 + "_n2_"+ n2 + ".py ###################"  )


if __name__ == "__main__":
   main(sys.argv[2:])
   
