#!/usr/bin/env python
import argparse
from Bio import SeqIO

#DNA GC content calculator 

#handle command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Input file")
parser.add_argument("-o", help="Output file")

args = parser.parse_args()

#Put the -i argument for InFile
InFile = args.i

#Open the InFile
try:
	IN=open(InFile, 'r')
except IOError:
	print ("Can't open file: %s." %(InFile))
	
#Old code for reading file one line at a time
#for Line in IN:
#	Line=Line.strip('\n')
#	DNAseq=Line

#New code to use BioPython to read a fasta file
#parse the file (IN) given that it is a fasta file
for Record in SeqIO.parse(IN, "fasta"):
	#.seq is the sequence of the file, whereas .id would be the ID
	DNAseq = Record.seq
	#Get length of sequence	
	SeqLength = len(DNAseq)
	
	GC_count = 0
	Gap_count = 0
#Go through each base
	for Base in ('A', 'G', 'T', 'C', 'N', '-'):
	#for next week -> need to handle gaps(-) for my group
#Count the number of times the base occurs
		NumBase = DNAseq.count(Base)
	#Count the gaps in the sequence		
		if Base == '-':
			Gap_count += NumBase 
			
	#Count the Gs & Cs
		elif Base == "G" or Base == "C":
			GC_count += NumBase
#End of 'for Base in loop'
	Total = GC_count - Gap_count
			
	print ("This sequence is %d nucleotides long." %(SeqLength))
	print ("GC content of %s is %.2f" %(Record.id, (GC_count/SeqLength) * 100))
	print ("There are %d gaps in this record." %(Gap_count))
	print ("This is the GC content of %s without gaps included: %.2f" %(Record.id, (Total/SeqLength) * 100))