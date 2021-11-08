import csv
num_attributes = 6
print('in data set  attributes are',num_attributes)

a = []
print('\n the train data set is\n')

with open('trainingdataa.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        a.append(row)
        print(row)
        
print('\n the initital value of hypothesis is ')
hypothesis =['0']*num_attributes
print(hypothesis)

for j in range(0,num_attributes):
    hypothesis[j] = a[0][j]

print("\n find S : finding maximaly psecific hypothesis is :\n")

for i in range(0,len(a)):
    if a[i][num_attributes]=='yes':
        for j in range(0,num_attributes):
            if a[i][j]!=hypothesis[j]:
                hypothesis[j]='?'
            else:
                hypothesis[j]=a[i][j]
print("for training data set example no :(0)hypothesis is ",format(i),hypothesis)

print("max hypothesis is :\n")
print(hypothesis)