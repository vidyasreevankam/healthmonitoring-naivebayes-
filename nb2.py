from NaiveBayes import  Pool
import os
DClasses = ["acute","allergies","cancer","fever","heart disease","signs","ulcers"]
base = "learn/"
p = Pool()
for i in DClasses:
    print(i)
    p.learn(base + i, i)
base = "test/"
for i in DClasses:
    dir = os.listdir(base + i)
    for file in dir:
        res = p.Probability(base + i + "/" + file)
        print(i + ": " + file + ": " + str(res))
dir = os.listdir(base + f)
for file in dir:
   res = p.Probability(base + f + "/" + file)
   print(f + ": " + file + ": " +str(res))
