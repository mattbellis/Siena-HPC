import pandas as pd
import shutil
import sys
import os

################################################################################
# Define where you want the output file to go
outdir = '/qnap/mbellis/GAIA/cdn.gea.esac.esa.int/Gaia/gedr3/BATCH_TEST'

# Create the directory if it does not exist
does_exist = os.path.exists(outdir)

if not does_exist:

  # Create a new directory because it does not exist
  os.makedirs(outdir)
  print(f"The new directory {outdir} is created!")

################################################################################

infilename = sys.argv[1]
outfilename = f"{infilename.split('/')[-1].split('.csv.gz')[0]}_SKIMMED.h5"

df = pd.read_csv(infilename, compression='gzip')

dfskim = df[['ra','dec']]

dfskim.to_hdf(outfilename,key='skimmed')

del dfskim
del df

# Need to specify full path name for destination file otherwise
# it does not get overwritten
# 
# We copy things over in *this* script because the script knows the output name
# of the file
print(f"Moving {outfilename} {outdir}/{outfilename}")
shutil.move(outfilename, f"{outdir}/{outfilename}")

