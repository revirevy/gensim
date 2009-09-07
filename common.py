import os.path
import logging

try:
    import numpy
    import scipy.sparse
    import csc.divisi
except ImportError:
    msg = "This program requires numpy, scipy and divisi packages installed under python2.5"
    logging.critical(msg) # log first
    raise SystemExit(msg) # then abort

PRINT_LEVEL = logging.DEBUG

# INPUT_PATHS is a mapping from id -> file system path. 
# id will be used as article's 'source' attribute in the similar.xml file.
# file system path will be scanned for directories starting with '#' and articles 
# from these directories will be used for similarity computation
INPUT_PATHS = {
               'dmlcz-serial': '/data/dmlcz/data/share/serial',
               'dmlcz-monograph': '/data/dmlcz/data/share/monograph',
               'dmlcz-proceedings': '/data/dmlcz/data/share/proceedings',
               'numdam': '/data/dmlcz/data/share/numdam',
               }

# all intermediate files will be stored into this directory
OUTPUT_PATH = '/data/dmlcz/xrehurek/results'
#OUTPUT_PATH = '/Users/kofola/workspace/dml/data/results'
assert os.path.isdir(OUTPUT_PATH), "directory %s for storing intermediate files is invalid" % OUTPUT_PATH

# all intermediate matrices will be stored into this directory
MATRIX_PATH = OUTPUT_PATH
assert os.path.isdir(MATRIX_PATH), "directory %s for storing matrices is invalid" % MATRIX_PATH

# this prefix is used for files generated by gensim
PREFIX = 'gensim'

def dataFile(fname):
    return os.path.join(OUTPUT_PATH, fname)

def inputPath(id):
    return os.path.join(INPUT_PATHS[id], fname)

def dbFile(type, baseDir = None):
    if baseDir:
        return dataFile(type + '_' + baseDir.replace('/', '_').replace('\\', '_') + '.pdl')
    else:
        return dataFile(type + '.pdl')

def matrixFile(fname):
    return os.path.join(MATRIX_PATH, fname)
