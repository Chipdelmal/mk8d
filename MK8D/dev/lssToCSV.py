
import sys
from glob import glob
from os import path
import MK8D as mk


(PATH_I, PATH_O, FILE_O) = (sys.argv[1], sys.argv[2], sys.argv[3])
# (PATH_I, PATH_O, FILE_O) = ('./data/', './data/', 'MK8D.csv')
files = glob(path.join(PATH_I, '*.lss'))
data = mk.compileRunsDataframeFromFiles(files, prependID=True)
data.to_csv(path.join(PATH_O, FILE_O), index=False)