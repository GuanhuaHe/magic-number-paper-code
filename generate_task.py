from numpy import arange
f = open("tasklist.txt", 'w')

thestring = []

for beta in arange(0.4,10.4,0.4):
    thestring.append(str(beta)+"\t"+str(0)+"\t"+str(0.1)+"\t"+str(45000)+"\t"+str(45000)+"\t"+str(0)+"\n")

#both keep moving  
for idx in range(200):
    thestring.append(str(10)+"\t"+str(0)+"\t"+str(0.1)+"\t"+str(45000)+"\t"+str(45000)+"\t"+str(0)+"\n")


    


for idx, ss in enumerate(thestring):
    f.write(str(idx)+"\t"+ss)
f.close()
