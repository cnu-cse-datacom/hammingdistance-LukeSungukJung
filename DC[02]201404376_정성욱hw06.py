import numpy as np
import random
import pandas as pd
from hamming_practice import hamming

df = pd.read_csv('sample.csv',names =['word','bin'])

def generate_random_ascii():
    for i in range(0,100):
        make_str = list()
        make_ascii = list ()
        make_hex = list()
        
        for j in range(0,4):
           num =  random.randint(97,122)
           make_str.append(str(chr(num)))
        string = ''.join(make_str)
        binary = bin(int.from_bytes(string.encode(),'big'))
    return string, binary


#for k in range(0,100):
#    string,binary =  generate_random_ascii()
#    df.iloc[k,0] = string
#    df.iloc[k,1] = "0"+binary[2:]

#df.to_csv('sample.csv',header=False,index=False)


min_ = 9999
count =0
prev_count =0
for i in range(len(df)):
    
    now_count = 9999
    for j  in range(i+1,len(df)):
        hd = (df.iloc[i,1],df.iloc[j,1])
        print(count,"(",df.iloc[i,0], df.iloc[j,0],")", ) 
        count =count+1
        now_count =0
        for sf in range(len(hd[0])):
                if(int(hd[0][sf])!=int(hd[1][sf])): 
                    now_count =now_count+1
                
    if(i==0):
        min_= now_count
        continue;
    else:
        if(now_count<min_):
            min_= now_count
        
        
print("min haming distance",min_)