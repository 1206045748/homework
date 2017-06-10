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
while True:
    ten=None
    try:
        ten=input("输入:")
        data = {}
        with open('./case/case'+ten+'.txt', 'r') as df:
            ie=0
            for kv in [de.strip().replace(" ","").split(',') for de in df]:
      
                data[ie]=[int(kve) for kve in kv]
                ie=ie+1
        print (data)
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
                if(len(g[i])==0 or g[i][0]==-1):
                    l.append(d)
                else:
                    for t in g[i]:
                        fin(t,d,l,g)
    

        for key in data:
    #s=s+key
            a=[]
            fin(key,a,l,data)
             
        temp=[]
        tt=[]

        for i in l:
            if(i not in temp):
                temp.append(i)
        l2=[]
        for i in temp:
            l2.append(i)

        for p1 in temp:
            for p2 in l2:
                compare(p1,p2,tt)
#print(tt)
        for i in tt:
            temp.remove(i)
        print(len(temp))
        print (temp)
        files= open('./answer/answer'+ten+'.txt', 'w+') 
        files.write(str(len(temp))+"\n")
        temp=sorted(temp,key=lambda a:(len(a),a))
        for ti in temp:
  #  ki=' '.join([str(ji) for ji in ti])
   # files.write(ki+"\n")
             files.write(str(ti)+"\n")
        files.close()
    except:pass
    if(len(ten)>2):break