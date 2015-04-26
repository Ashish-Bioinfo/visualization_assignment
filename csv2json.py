#!/usr/bin/python
from optparse import OptionParser
import csv
import json

class CSV2JSON(object):

  def __init__(self):
   
    (self.csv_file , self.json_file) = self.getOpt()
    if  self.json_file == None:
         self.json_file = self.csv_file.replace('.csv','.json')

  def getOpt(self):

    parser = OptionParser(usage="usage: %prog -i <csv filename> -o <json filename>")

    parser.add_option('-i','--input', dest="in_file" , metavar="FILE",
		   help="input file in csv format")
    parser.add_option('-o', '--output', dest="out_file", metavar="FILE",
                  help="output file name json format")

    (options, args) = parser.parse_args()
   
    if len(args) < 0 :
        parser.error("wrong number of arguments")
    
    #returning passed options to calling function
    return (options.in_file, options.out_file)

    #Function to get json format from csv format

  def getJSON(self):
    
      csvfile = open(self.csv_file, 'r')
      jsonfile = open(self.json_file, 'w')

      fieldnames = csvfile.readline().strip().split(",")
      print fieldnames

      read_csv = csv.DictReader(csvfile, fieldnames)
      json_out = json.dumps( [ row for row in read_csv ])
      jsonfile.write(json_out) 
     
if __name__ == "__main__":
  obj = CSV2JSON()
  obj.getJSON()
