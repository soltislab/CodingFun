#!/usr/bin/env python3
import argparse
from Bio import SeqIO

#DNA GC content calculator

#Handle command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Input file")

args = parser.parse_args()
  
#Put the -i argument in InFile
InFile = args.i

#Open the InFile
try:
  IN=open(InFile, 'r')
except IOError:
  print ("Can't open file: %s." %(InFile))

#Old code for reading file one line at a time.
#for Line in IN:
#  Line=Line.strip('\n')


#New code to use BioPython to read a fasta file
for Record in SeqIO.parse(IN, "fasta") :
  DNAseq=Record.seq
  GC_count=0
  
  #Get Length of sequence
  SeqLength=len(DNAseq)
  
  #Go through each base
  for Base in ('A','G','T','C', 'S', 'N'):
    #Count the number of times the base occurs
    NumBase=DNAseq.count(Base)

    #print("Percent %s: %.2f" %(Base,NumBase/SeqLength*100))

    if Base == "G" or Base == "C" or Base == "S":
      GC_count+=NumBase
   #End of for Base in loop.        
 
  print ("GC content of %s is %.2f" %(Record.id, GC_count/SeqLength*100))
#End for Record in loop.
