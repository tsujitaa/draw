"""ten=[[x,y]for y in range(5) for x in range(5)]

def tenten(x,y):
    return ten [(5*y)+x]

newten=[]

def right(x,y):
    a=tenten(x+1,y)
    newten.append(a)
def up(x,y):
    b=tenten(x,y+1)
    newten.append(b)
def left(x,y):
    c=tenten(x-1,y)
    newten.append(c)
def down(x,y):
    d=tenten(x,y-1)
    newten.append(d)



def draw1(x,y):
    if a in ten:
        right(x,y)
def draw2(x,y):
    if b in ten:
        up(x,y)        
def draw3(x,y):
    if c in ten:
        left(x,y)
def draw4(x,y):
    if d in ten:
        down(x,y)

li=[draw1(x,y),draw2(x,y),draw3(x,y),draw4(x,y)]

def _draw(x,y):"""
    



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
                    li[j]
                
def erase():"""
    





"""def draw():
    for n in range(2):
        if x==0 and y==0 :
            newten.append(tenten(x+(1-n),y+n))
        if x==4 and y==0 :
            newten.append(tenten(x-(1*n),y+(1-n)))
        if x==0 and y==4 :
            newten.append(tenten(x+(1-n),y-(1*n)))
        if x==4 and y==4 :
            newten.append(tenten(x-n,y+(n-1)))

    for m in range(1,3):
        if x==m and y==0:
            for k in range 
            newten.append(tenten)"""
