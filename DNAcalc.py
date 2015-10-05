#!/usr/bin/env python3

DNAseq='ATGTACGACGTACGNATNANTATTAC'

print("Sequence is: %s" %(DNAseq))


#print("There are %d As, %d Gs, %d Ts and %d Cs" %(NumA, NumG, NumT, NumC))

SeqLength=len(DNAseq)

for Base in ('A','G','T','C', 'N'):
  NumBase=DNAseq.count(Base)
  
  print("Percent %s: %.2f" %(Base,NumBase/SeqLength*100))
print ("Sequence is %d bp long" %(SeqLength))
