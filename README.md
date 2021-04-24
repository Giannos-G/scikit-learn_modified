# scikit-learn_modified
### This is the repo of a modified version of scikit-learn which is used to benchmark every example and benchmark included in the original repo. 
1) I commented all of the *plt.show()* commands to every script of */examples* and */benchmarks* in order to minimize human intreaction with each script so that my energy, time and memory profiling will be more accurate. 
2) In every directory you will find the *time_peak_mem_profiler.py* which is used to do the profiling (time and max memory)
3) I made replicas of the files:
   - /benchmarks/bench_tree.py 
   - /benchmarks/bench_plot_lasso_path.py

in which I modified only some simple loops. This was done to increase my dataset entries. 

That's all the changes I made :) 
