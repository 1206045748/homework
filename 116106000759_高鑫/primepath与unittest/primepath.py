graph1={0:[1,2],1:[3],2:[3],3:[0]}
graph3={0:[1,2],1:[2],2:[3,4],3:[6],4:[5,6],5:[4],6:[]}
graph2={1:[2],2:[3,13],3:[4],4:[5,7,9],5:[6],6:[2],7:[8],8:[2],9:[10],10:[11,12],11:[3],12:[2],13:[]}
l=[]
s=''
def fin(i,a,l,g):
    c=[]
    for y in a:
        c.append(y)
   
    if(i in c and i!=c[0]):
        l.append(c)
               
    elif(i in c and i==c[0]):
               # s=s+i
        c.append(i)
        l.append(c)
    else:
        d=c
        d.append(i)
        if(len(g[i])==0):
            l.append(d)
        else:
            for t in g[i]:
                fin(t,d,l,g)
    

for key in graph2:
    #s=s+key
    a=[]
    fin(key,a,l,graph2)
             
#print(l)
temp=[]
tt=[]

for i in l:
    if(i not in temp):
        temp.append(i)
l2=[]
for i in temp:
    l2.append(i)
def compare(p1,p2,tt):
    s1=""
    s2=""
    for i in p1:
        s1=s1+str(i)+","
    for j in p2:
        s2=s2+str(j)+","
    if(s1!=s2 and s1 in s2):
        if(p1 not in tt):
            tt.append(p1)
for p1 in temp:
    for p2 in l2:
        compare(p1,p2,tt)
#print(tt)
for i in tt:
    temp.remove(i)
print(str(len(temp)))
for p in temp:
    print (p)



           


       
