class A:
    def B(self,arr):
        c,d=0,0
        for e in arr:
            if e:
                c+=1
            else:
                d=max(c,d)
                c=0
        d=max(c,d)
        return d

f=A()
arr_1=[1,1,0,1,1,1,0,0,1,1,1,1]
arr_2=[1,1,1]
arr_3=[]
arr_4=[0,0,0]
print(f.B(arr_1))