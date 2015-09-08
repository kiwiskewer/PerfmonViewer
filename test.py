    #config = ConfigParser(dict_type=dict, delimiters=(' ', '=', ':'), allow_no_value=True)
    #config = ConfigParser(dict_type=dict, delimiters=(' ', '=', ':'), allow_no_value=True)
    #config = ConfigParser(dict_type=dict, delimiters=(' ', '=', ':'), allow_no_value=True)
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
        pfmon[name].append(int(value))
    return pfmon

def main(argv):
  outputFile=''
  configFile='pfmons.cfg'
  pfName=''
  batchNum=''
  pfFile=''
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
    else:
      pfFile=arg

  config = ConfigParser(dict_type=dict,allow_no_value=True)
  config.optionxform = lambda option: option
  config.read(configFile)

  if not pfFile:
    pfFile='perfmon.csv'

if __name__ == "__main__":
  main(sys.argv[1:])