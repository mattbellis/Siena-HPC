# Test on head node

First do

```
module load Python3 
```

Then do 

```
python process_one_file.py /qnap/mbellis/GAIA/cdn.gea.esac.esa.int/Gaia/gedr3/gaia_source/GaiaSource_636681-636777.csv.gz
```

You can then look in the output directory, as defined in `process_one_file.py` to see if the output file is there. 


# Test on cluster

You will want to edit `build_job_scripts.py` if you want to run over 1 file or 10 or all the files.
Then you can run

```
python build_job_scripts.py
```

This will run over the files and copy the output to whatever directory you specified in 
`process_one_file.py`.
