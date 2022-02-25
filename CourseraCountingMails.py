# Finding and counting the most reapeated email from the "mbox-short.txt" file
fname = input("Enter file name: ")
document=open(fname)
count=0
histogram=dict()


for linea in document:
    if (linea.startswith('From ')):
        important=linea.split()
        for find in important:
            if "@" in find:
                histogram[find]=histogram.get(find,0)+1
            
freqmail=None
wie=None


for k,n in histogram.items():
    if freqmail is None or n>wie:
        freqmail=k
        wie=n

print(freqmail,wie)      

