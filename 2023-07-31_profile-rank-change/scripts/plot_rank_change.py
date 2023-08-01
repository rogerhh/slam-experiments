import sys
from optparse import OptionParser
import csv

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--input_file", dest="input_file", 
                      default="", help="The filename that contains rank change output in csv format")
    parser.add_option("--var_width", dest="var_width", 
                      default="", help="The width of the variables (assuming same for all)")

    (options, args) = parser.parse_args()

    filename = options.input_file
    var_width = int(options.var_width)

    with open(filename, "r") as fin:
        reader = csv.reader(fin, delimiter=",")
        for row in reader:
            print(row)
    
