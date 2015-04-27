#!/usr/bin/python
from optparse import OptionParser
import csv
import json
import itertools
class CSV2JSON(object):

  def __init__(self):

    self.header = ""   
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

  def nestedJSON(self, csv_list):

    nested_json = []

    data = sorted(csv_list, key=lambda r: r[1])
    
    for key, group in itertools.groupby(csv_list, key=lambda r: r[0]):
      group_rows = [row[1:] for row in group]
      
      if len(row[1:]) == 1:
        nested_json.append({"name": row[0],"size": int(row[1])})
      else:
        nested_json.append({"name": key,"children":self.nestedJSON(group_rows)})

    return nested_json 
   
  def getNestedJSON(self):

    csvfile = open(self.csv_file, 'r')
    jsonfile = open(self.json_file, 'w')

    self.header = csvfile.readline().strip().split(",")
    #reading csv as list of list
    csv_list = list(csv.reader(csvfile))
    
    json_out = json.dumps(self.nestedJSON(csv_list),indent = 2)
    jsonfile.write(json_out)

  def getJSON(self):
    
      csvfile = open(self.csv_file, 'r')
      jsonfile = open(self.json_file, 'w')

      self.header = csvfile.readline().strip().split(",")

      read_csv = csv.DictReader(csvfile, self.header)
      json_out = json.dumps( [ row for row in read_csv ])
      jsonfile.write(json_out) 
     
if __name__ == "__main__":
  obj = CSV2JSON()
  #obj.getJSON()
  obj.getNestedJSON()
