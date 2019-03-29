import os
f1=open("lambda_occur.txt",'a')
def find_lambda(path2):
    try:
        f=open(path2)
        data=f.read()
        all_lines=data.split('\n')
        snippet=""
        n=len(all_lines)
        for i in range(0,n):
            if "lambda" in all_lines[i]:
                if i>0:
                    snippet+=all_lines[i-1]
                snippet+=all_lines[i]
                if i<n-1:
                    snippet+=all_lines[i+1]
                snippet+="\n\n"
        f1.write(snippet)
    except:
        return 0

def is_valid(p):
    i=len(p)-1
    while p[i]!='.' and i>=0:
        i-=1
    exten=p[i+1:]
    if exten!="py":
        return False
    return True

def visit(p):
    try:
        all_files=os.listdir(p)
    except:
        all_files=[]
        
    for k in all_files:
        if is_valid(k)==False:
            visit(p+'\\'+k)
        else:
            find_lambda(p+'\\'+k)
            #print(k)
        
def run(c):
    print("Path is :",c)            
    if is_valid(c)==False:   
        all_files=os.listdir(c)
        for file1 in all_files:
            if is_valid(file1)==False:   
                visit(c+'\\'+file1)
            else:
                find_lambda(c+'\\'+file1)
                #print(file1)
    else:
        find_lambda(c)
        #print(c)

path1=input()
run(path1)
f1.close()
