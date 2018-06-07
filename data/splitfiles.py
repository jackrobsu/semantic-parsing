import sys

qf = open(sys.argv[1].split(".")[0]+"_question",'w')
af = open(sys.argv[1].split(".")[0]+"_answer",'w')


with open(sys.argv[1],'r') as f :

    for line in f :
        line = line.strip()
        arr = line.split("\t")
        qf.write(arr[0]+"\n")
        af.write(arr[1]+"\n")

    qf.close()
    af.close()
        

