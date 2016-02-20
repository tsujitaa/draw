ten=[[x,y]for y in range(5) for x in range(5)]

def tenten(x,y):
    return ten [(5*y)+x]

def masu(x,y):
    returm tenten(x,y)
    
newten=[]

def right(x,y):
    if (tenten(x,y) in ten) and (tenten(x+1,y) in ten):
        newten.append(tenten(x+1,y))
def up(x,y):
    if (tenten(x,y) in ten) and (tenten(x,y+1) in ten):
        newten.append(tenten(x,y+1))
def left(x,y):
    if (tenten(x,y) in ten) and (tenten(x-1,y) in ten):
        newten.append(tenten(x-1,y))
def down(x,y):
    if (tenten(x,y) in ten) and (tenten(x,y-1) in ten):
        newten.append(tenten(x,y-1))



            
li=[right(x,y),up(x,y),left(x,y),down(x,y),right(x,y)]

def _draw(x,y):

def erase(x,y):



"""li=[right(x,y),up(x,y),left(x,y),down(x,y),right(x,y)]
def draw():
    for n in range(2):
        if x==0 and y==0 :
            li[n]
        if x==4 and y==0 :
            li[n+1]
        if x==0 and y==4 :
            li[n+3]
        if x==4 and y==4 :
            li[n+2]

    for m in range(1,4):
        if x==m and y==0:
            li[m-1]
        if x==0 and y==m:
            li[m+2]
        if x==m and y==4:
            li[m+1]
        if x==4 and y==m:
            li[m]

    for k in range(1,4):
        for l in range(1,4):
            if x==k and y==l:
                for j in range(4):
                    li[j]"""
                
    





