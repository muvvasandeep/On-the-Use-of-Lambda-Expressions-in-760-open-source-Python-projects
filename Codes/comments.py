import os
import json
f = open("final_lambda_occur.txt","r")
data = f.read()
all_lines = data.split('\n')
count = 0
comments = {}
path = "C:\\Users\\muvva\\Desktop\\testing\\"
for i in range(0,len(all_lines)):
    if i>1 and i<len(all_lines)-1:
        try:
            if "lambda" in all_lines[i]:
                if ('#' in all_lines[i-1] and all_lines[i-1].count('#')==1) or ('#' in all_lines[i-1] and all_lines[i+1].count('#')==1):
                    if path in all_lines[i-2]:
                        index = all_lines[i-2].find("-master")
                        if index>0:
                            name = all_lines[i-2][31:index]
                            name+="-master"
                            print(name)
                            if name in comments.keys():
                                comments[name]+=1
                            else:
                                comments[name]=1
        except:
            continue
print(comments)

with open('comments.json','w') as f:
    json.dump(comments,f)
                    
        
