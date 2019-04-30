import os
from collections import defaultdict as dd
repo_count=dd(int)
f=open('final_lambda_occur.txt','r',encoding = "ISO-8859-1")

data=f.read()
def find_count(c):
    all_files=os.listdir(c)
    for file1 in all_files:
        repo_count[str(file1)]=data.count(file1)

c=input().strip()
find_count(c)
f.close()
import json
with open('repo_lambda_count.json', 'w') as fp:
    json.dump(repo_count, fp)                    
        
