import shutil
import sys
import os
import subprocess

# Define the path to the input files
path = "/qnap/mbellis/GAIA/cdn.gea.esac.esa.int/Gaia/gedr3/gaia_source/"

# Get current path
cwd = os.getcwd()

########################################################################################
# Write out a single slurm batch file for each job
########################################################################################
def write_file(filename, submit=False):
        output = ""
        output += "#!/bin/bash\n"
        output += "#\n"
        output += "# Set Job Name\n"
        output += "#SBATCH -J job\n"
        output += "\n"
        output += "# Set file to capture standard out and standard error and append the jobID (%j)\n"
        output += "#SBATCH -o job.out.%j\n"
        output += "\n"
        output += "#Set the total number of cores to use for the job\n"
        output += "#SBATCH -n 1\n"
        output += "\n"
        output += "#Set the time limit for the job - one hour is specified here\n"
        output += "#SBATCH --time=0:60:00\n"
        output += "\n"
        output += "#Load any necessary environmental modules here\n"
        output += "module load Python3\n"
        output += "\n"
        output += "# Move to the directory needed - defaults to the submission directory\n"
        output += "cd $SLURM_SUBMIT_DIR\n"
        output += "\n"
        output += "# perform calculation\n"
        output += f"python {cwd}/process_one_file.py {path}/{filename}\n"

        jobfilename = f"JOB_{filename}.sh"
        jobfile = open(jobfilename,'w')
        jobfile.write(output)
        jobfile.close()

        cmds = ['sbatch', jobfilename]

        # Submit the jobs if the submit job is set to True
        if submit is True:
            print(f"Submitting job to process {filename}")
            process = subprocess.Popen(cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout,stderr = process.communicate()
            print(stdout.decode())
            print(stderr.decode())


########################################################################################

# This looks in the path and filds all the files that meet the criteria, in this
# case that they have 'GaiaSource' in the name.
files = (filename for filename in os.listdir(path)
   if os.path.isfile(os.path.join(path,filename)) and filename.find('GaiaSource')>=0)

# Turn the generator into a list because I like working with lists better.
inputfiles = []
for f in files:
    #print(f)
    inputfiles.append(f)

#print(inputfiles)

#'''
# This writes and submits the files
#for f in inputfiles[:]: # Submit all the jobs 
for f in inputfiles[0:10]: # Submit 10 jobs for 10 files
    write_file(f,submit=True)
#'''

################################################################################
# Run these if you just want to generate some individual batch scripts
################################################################################
#write_file(inputfiles[0],submit=False)
#print()
#print(inputfiles[3])
#write_file(inputfiles[3],submit=False)

