#!/usr/bin/env python3
import argparse
from Bio import SeqIO
import GCcalc

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
  GC=GCcalc.GC(DNAseq)
 
  print ("GC content of %s is %.2f" %(Record.id, GC))
#End for Record in loop.
