
import rpy2.robjects as robjects

import logging

from rpy2.robjects.packages import importr

from rpy2.rinterface_lib.callbacks import logger as rpy2_logger
import os
from os.path import dirname, abspath



# Display errors in console
# Source: https://stackoverflow.com/questions/11992138/suppress-warnings-in-rpy2
rpy2_logger.setLevel(logging.ERROR) 

utils = importr('utils')
base = importr('base')

# parent_dir = dirname(dirname(abspath(__file__)))
# Path
# sourcepath = os.path.join(parent_dir, "PythonR/mainweb.R")
# robjects.r['source']('main.R') 

r = robjects.r
r['source']('Python/PythonR/mainweb.R') 
 
# Loading the function we have defined in R.
main_function_r = robjects.globalenv['main_function']
setup_function_r = robjects.globalenv['setup_function']


#Invoking the R function and getting the result
# count_separate_trees_function_r('files/CHM.tif')
