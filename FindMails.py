fname = input("Enter file name: ")
document=open(fname)
count=0

for linea in document:
    if (linea.startswith('From ')):
        important=linea.split()
        print(important) #[1] To get just email
        count=count+1
        

print("There were", count, "lines in the file with From as the first word")