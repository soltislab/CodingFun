#!/usr/bin/env python3
from Bio import SeqIO
import sys

#DNA GC content calculator



def countItems(Item,Seq):
  ItemCount=Seq.count(Item)
  return(ItemCount)
  

def GC(DNAseq):
  GC_count=0
  SeqLength=len(DNAseq)
  for Base in ('A','G','T','C', 'S', 'N'):
    #Count the number of times the base occurs
    NumBase=countItems(Base, DNAseq)

    if Base == "G" or Base == "C" or Base == "S":
      GC_count+=NumBase
   #End of for Base in loop.        
 
  return(GC_count/SeqLength*100)
 
def main():
  InFile=sys.argv[1]
  try:
    IN=open(InFile, 'r')
  except IOError:
    print ("Can't open file: %s." %(InFile))

  for Record in SeqIO.parse(IN, "fasta") :
    DNAseq=Record.seq
    MyGC=GC(DNAseq)
    print ("GC content of %s is %.2f" %(Record.id, MyGC))



if __name__ == "__main__":
  main()