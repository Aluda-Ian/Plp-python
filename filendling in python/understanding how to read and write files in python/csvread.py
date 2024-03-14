import csv

# with open('filendling in python/understanding how to read and write files in python/ian.csv', 'r') as file:
#     read = csv.reader(file)
#     for row in read:
#         print(row)

with open('filendling in python/understanding how to read and write files in python/ian.csv', 'w' , newline='') as file:
    write = csv.writer(file)
    write.writerow(['name', 'skills','country'])
    write.writerow(['Ian', 'php','Kenya'])
    write.writerow(['name', 'skills','country'])
    