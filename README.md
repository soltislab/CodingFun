#Coding Fun

This has directions and some sample code for the Soltis Lab coding group.

##For Oct. 5:

1. Last week we wrote some code to calculate GC content. My Version of this is in the DNAcalc.py file.
2. This doesn't quite do what we want...Modify it to print out the %GC (ie. DNAseq.count(Base) when Base=G plus when Base=C divided by sequence length)
3. Currently this script uses a sequence hard coded on line 3 of the script. Let's modify this to read from a file and calculate %GC for each sequence in the file. For now, we will assume that the file has one sequence per line.
  Here's an example:
  ```
  try:
	IN=open('MySequenceFile.txt, 'r')
  except IOError:
	print "Can't open file."
  ```
4. Let's use argparse to take the filename from the command line.
	Here's an example:
  ```	
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", help="input file")
  parser.add_argument("-o", help="output file")
  
  args = parser.parse_args()
  
  InFile = args.i
  OutFile = args.o
  ```
5. Let's use BioPython to read a fasta file and calculate %GC.

    Here's an example:
  ```
  IN=open(InFile, 'r')
  for record in SeqIO.parse(IN, "fasta") :
  	for Base in ('A','G','T','C', 'N'):
    		NumBase=record.seq.count(Base)
  ```

