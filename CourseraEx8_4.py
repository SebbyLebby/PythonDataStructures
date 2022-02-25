#Entrenando
documento=open('Romeo.txt')
count=0
lst=[]
for leer in documento:
    lst=lst+leer.split()

print(lst)