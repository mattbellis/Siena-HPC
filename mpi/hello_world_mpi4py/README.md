# Test on head node

First do

```
module load Python3 OHPC/openmpi-3.1.4
```

Then do 

```
bash run.sh hello_world.py
```

# Test on cluster

```
sbatch slurm_script.sh
```

It should run quickly and produce an output file which you can check to see the rank and size for the processes.
