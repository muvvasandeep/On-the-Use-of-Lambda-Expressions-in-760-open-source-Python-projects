import os
import json
f = open("final_lambda_occur.txt","r")
data = f.read()
all_lines = data.split('\n')
fp = open("comments.txt","w")
snippet = ""
count = 0
comments = {}
path = "C:\\Users\\muvva\\Desktop\\Dataset\\"
print(len(all_lines))
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
                            snippet+=all_lines[i-2]
                            snippet+='\n'
                            snippet+=all_lines[i-1]
                            snippet+='\n'
                            snippet+=all_lines[i]
                            snippet+='\n'
                            snippet+=all_lines[i+1]
                            snippet+='\n'
                            snippet+="#########################################################################################"
                            snippet+='\n'
                            #print(name)
                            if name in comments.keys():
                                comments[name]+=1
                            else:
                                comments[name]=1
        except:
            continue
fp.write(snippet)
print(comments)

with open('comments.json','w') as f1:
    json.dump(comments,f1)
                    
        
