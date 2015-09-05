#!/pkg/qct/software/python/3.4.0/bin/python
import os,getopt
import re
import sys
#from ConfigParser import SafeConfigParser
from configparser import ConfigParser
import csv
from collections import defaultdict
def pfReader(fn):
  pfmon=defaultdict(list)
  with open (fn) as f:
    reader = csv.DictReader(f)
    for row in reader:
      for name,value in row.items():
        try:
          v=int(value)
        except ValueError:
          pass
        pfmon[name].append(int(v))
    return pfmon

def main(argv):
  outputFile='sel_perfmons.csv'
  configFile='pfmons.cfg'
  pfName=''
  batchNum=''
  try:
    opts, args = getopt.getopt(argv,"o::c::p::b::")
  except getopt.GetoptError:
    print ('getPerfmon.py -c config -o output.csv -p pfmon_name -b batch# pfmon.csv')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-c':
      configFile = arg
    elif opt in ('-o'):
      outputFile = arg
    elif opt in ('-p'):
      pfName = arg
    elif opt in ('-b'):
      batchNum = arg
  if args:
    pfFiles=args
  else:
    pfFiles.append('perfmon.csv')

  config = ConfigParser(dict_type=dict,allow_no_value=True)
  config.optionxform = lambda option: option
  config.read(configFile)
  batches=[]

  if 'batches' in config.sections():
    if 'start' in config['batches']:
      start_batch=config.item('batches','start')
    if 'end' in config['batches']:
      start_batch=config.item('batches','end')
    for i in config['batches']:
      batches.append(i)
  counters=[]
  for i in config['counters']:
    counters.append(i)
  
  pfcounters=defaultdict(list)
  for fn in pfFiles:
    pfcounters[fn]=pfReader(fn)
    

  

if __name__ == "__main__":
  main(sys.argv[1:])
