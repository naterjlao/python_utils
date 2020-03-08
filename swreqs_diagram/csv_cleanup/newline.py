#!/usr/bin/python3

# The csv's have a tendency to be corrupt and add newlines
# Usage:
#        newline.py <INPUT_FILE> <OUTPUT_FILE>


import sys
import os.path

# List of strings that every appropriate line should have
IDENTIFIERS = ["user_","fun_","nonfun_","sys_","sw_"]

if __name__ == "__main__":
	print("running csv newline checker")

	# Check the number of arguments
	if (len(sys.argv) != 3):
		raise Exception('invalid number of arguments. Usage: newline.py <INPUT_FILE> <OUTPUT_FILE>')

	inputFileName = sys.argv[1]
	outputFileName = sys.argv[2]

	# Check if the input argument is a valid filename
	if (not (os.path.isfile(inputFileName))):
		raise Exception("%s is not a file" % inputFileName)


	# Check if the output argument is a file that already exists
	# If it does, kill it
	if (os.path.isfile(outputFileName)):
		os.remove(outputFileName)

	inputFile = open(inputFileName,'r')
	outputFile = open(outputFileName,'x')

	# Create an empty result string
	result = ""
	current = ""

	# Go through each line
	for line in inputFile:
		
		# Strip each line from trailing and leading newlines and whitespace
		current = line
		current = current.strip()

		# Find the leading lines
		isLeading = False
		for identifier in IDENTIFIERS:
			if (current.find(identifier) == 0):
				isLeading = True

		# If the line starts with one of the identifiers, add a newline before it
		if (isLeading):
			result += "\n"

		result += current

	# Add additional newline at the end
	result += "\n"

	# Flush result string to the OUTPUT_FILE
	outputFile.write(result)

	# Cleanup
	inputFile.close()
	outputFile.close()

