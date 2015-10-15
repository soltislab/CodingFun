#!/usr/bin/env python3
import argparse
from Bio import SeqIO
#Adding comments
parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Input file")

args = parser.parse_args()

InFile = args.i

try:
  IN=open(InFile, 'r')
except IOError:
  print ("Can't open file.")

#for Line in IN:
#  Line=Line.strip('\n')
for Record in SeqIO.parse(IN, "fasta") :
  DNAseq=Record.seq
  SeqLength=len(DNAseq)
  GC_count=0
  
  for Base in ('A','G','T','C', 'S', 'N'):
  
    NumBase=DNAseq.count(Base)
    
    #print("Percent %s: %.2f" %(Base,NumBase/SeqLength*100))
    
    if Base == "G" or Base == "C" or Base == "S":
           GC_count+=NumBase
            
  #print ("Sequence is %d bp long" %(SeqLength))
  print ("GC content of %s is %.2f" %(Record.id, GC_count/SeqLength*100))
