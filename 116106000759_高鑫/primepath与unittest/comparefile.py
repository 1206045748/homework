while True:
    ten=None
    try:
        ten=input("输入:")
        file1=[]
        file2=[]
        with open('./answer/answer'+ten+'.txt', 'r') as df:
            for  de in df:
                file1.append(de)
        with open('./hshanswer/answer'+ten+'.txt', 'r') as df2:
            for  de2 in df2:
                file2.append(de2)
        flag=0
        for i in range(len(file1)):
            if(file1[i]!=file2[i]):
                print("第"+str(i)+"条路径不匹配："+file1[i]+"vs"+file2[i])
                flag=1
        if(flag==0):
            print("比较成功！")
    except:pass
    if(len(ten)>2):break

   