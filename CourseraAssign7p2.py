# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
cont=0
ac=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    posnumb=line.find("0")
    nonumb=line[posnumb:]
    number=float(nonumb)
    cont=cont+1
    ac=ac+number
    
totalprom=ac/cont
print("Average spam confidence:",totalprom)