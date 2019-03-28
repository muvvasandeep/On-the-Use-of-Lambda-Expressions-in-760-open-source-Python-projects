import os
def find_lambda(path2):
    
    try:
        f=open(path2)
        data=f.read()
        if "lambda" in data:
            print("lambda is there in file",path2)
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