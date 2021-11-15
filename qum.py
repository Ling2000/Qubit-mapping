import threading
import numpy.matlib
import math
import os
from pathlib import Path
import operator

def jianzhi(cir,cou,map,h):
    d=map[h]
    nb=[]
    for n in cir:
        if h in n:
            nb.append(n)
            pass
        pass
    mb=[]
    for n in cou:
        if d in n:
            mb.append(n)
            pass
        pass
    for n in nb:
        for m in nb:
            i,j=m
            if n==(j,i):
                nb.remove(m)
                pass
            pass
        pass
    #print(h)
    #print(d)
    #print(nb)
    #print(mb)
    if len(nb)<=len(mb):
        return True
        pass
    return False
    pass



def replace(nam, map,lisn):
    cirtr = open('./circuits/'+nam, 'r')
    my_file = Path('./results/'+lisn)
    if not my_file.is_dir():
        os.mkdir('./results/'+lisn)
    cirtw = open('./results/'+nam, 'w')
    line=cirtr.readline()
    a = list(line.split())
    while a[0]!="qreg":
        cirtw.write(line)
        line=cirtr.readline()
        a = list(line.split())
        if len(a)==0:
            line=cirtr.readline()
            a = list(line.split())
            pass
    cirtw.write(line)
    line=cirtr.readline()
    while True:
        if not line:
            break
        a = list(line.split())
        if len(a)==0:
            line=cirtr.readline()
            a = list(line.split())
            pass
        if a[0]=='creg':
            cirtw.write(line)
            line=cirtr.readline()
            a = list(line.split())
        if len(a)==3:
            c=a[1][0:len(a[1])-1].split(',',1)
            e=int(c[0][2:len(c[0])-1])
            f=int(a[2][2:len(a[2])-2])
            e=map[e]
            f=map[f]
            es="q[%d]" % e
            fs="q[%d]" % f
            lw=a[0]+" "+es+","+fs+";\n"
            cirtw.write(lw)
            pass
        else:
            c=a[1][0:len(a[1])-1].split(',')
            if len(c)==2:
                e=int(c[0][2:len(c[0])-1])
                f=int(c[1][2:len(c[1])-1])
                e=map[e]
                f=map[f]
                es="q[%d]" % e
                fs="q[%d]" % f
                lw=a[0]+" "+es+","+fs+";\n"
                cirtw.write(lw)
                pass
            else:
                e=int(a[1][2:len(a[1])-2])
                e=map[e]
                es="q[%d]" % e
                lw=a[0]+" "+es+";\n"
                cirtw.write(lw)
        line=cirtr.readline()
    cirtr.close()
    cirtw.close()


def match(cir,cou,map,qubit):
    if len(map)==0:
        i=0
        while i<qubit:
            h,z=cir[0]
            map[h]=i
            ci=cir.copy()
            ma=map.copy()
            if jianzhi(cir,cou,map,h):

                nu,ma=match(ci,cou,ma,qubit)

                if nu==1:
                    return (1,ma)
            i=i+1
            pass
        return (-1,ma)
    else:
        if len(cir)==0:
            return (1,map)
            pass
        hzb,zzb=cir[0]
        if(hzb in map):
            cir.pop(0)
            hzb=map.get(hzb)
            if(zzb in map):
                #print("yhyz")
                zzb=map.get(zzb)
                if((hzb,zzb) in cou) or ((zzb,hzb) in cou):
                    if len(cir)==0:
                        return (1,map)
                        pass
                    ci=cir.copy()
                    ma=map.copy()
                    return match(ci,cou,ma,qubit)
                #print(map)
                return (-1,map)
            else:
                #print("yhwz")
                n=0
                forZzb=[]
                while n<len(cou):
                    hczb,zczb=cou[n]
                    if hczb==hzb:
                        forZzb.append(zczb)
                    if zczb==hzb:
                        forZzb.append(hczb)
                    n=n+1
                    pass
                values=map.values()
                n=0
                while n<len(forZzb):
                    if(forZzb[n] in values):
                        forZzb.pop(n)
                        n=n-1
                    n=n+1
                    pass

                if len(forZzb)==0:
                    #print(map)
                    return (-1,map)
                n=0
                while n<len(forZzb):
                    map[zzb]=forZzb[n]
                    ci=cir.copy()
                    ma=map.copy()
                    if jianzhi(cir,cou,map,zzb):
                        nu,ma=match(ci,cou,ma,qubit)
                        if nu==1:
                            return (1,ma)
                    n=n+1
                    pass
                #print(ma)
                return (-1,ma)
        else:
            if(zzb in map):
                #print("whyz")
                cir.pop(0)
                zzb=map.get(zzb)
                n=0
                forHzb=[]
                while n<len(cou):
                    hczb,zczb=cou[n]
                    if hczb==zzb:
                        forHzb.append(zczb)
                    if zczb==zzb:
                        forHzb.append(hczb)
                    n=n+1
                    pass
                values=map.values()
                n=0
                while n<len(forHzb):
                    if(forHzb[n] in values):
                        forHzb.pop(n)
                        n=n-1
                    n=n+1
                    pass
                if len(forHzb)==0:
                    #print(map)
                    return (-1,map)
                n=0
                while n<len(forHzb):
                    map[hzb]=forHzb[n]
                    ci=cir.copy()
                    ma=map.copy()
                    if jianzhi(cir,cou,map,hzb):
                        nu,ma=match(ci,cou,ma,qubit)
                        if nu==1:
                            return (1,ma)
                    n=n+1
                    pass
                #print(ma)
                return (-1,ma)
            else:
                #print("whwz")
                values=map.values()
                n=0
                ma=map.copy()
                while n<qubit:
                    if n not in values:
                        map[hzb]=n
                        ci=cir.copy()
                        ma=map.copy()
                        if jianzhi(cir,cou,map,hzb):
                            nu,ma=match(ci,cou,ma,qubit)
                            if nu==1:
                                return (1,ma)
                    n=n+1
                #print(ma)
                return (-1,ma)








def coup(nam):
    coup = open('./couplings/'+nam, 'r')
    line1=coup.readline()
    a = list(map(int,line1.split()))
    b=[(a[0],a[1])]
    line=coup.readline()
    while line!='\n':
        a = list(map(int,line.split()))
        b.append((a[0],a[1]))
        line=coup.readline()
    coup.close()
    return b



    pass

def cirt(nam):
    cirt = open('./circuits/'+nam, 'r')
    a=""
    line=cirt.readline()
    a = list(line.split())
    while a[0]!="qreg":
        line=cirt.readline()
        a = list(line.split())
        if len(a)==0:
            line=cirt.readline()
            a = list(line.split())
            pass
    b=[int(a[1][2:len(a[1])-2])]
    line=cirt.readline()
    while True:
        if not line:
            break
        a = list(line.split())
        if len(a)==0:
            line=cirt.readline()
            a = list(line.split())
            pass
        if a[0]=='creg':
            line=cirt.readline()
            a = list(line.split())

        if len(a)==3:
            c=a[1][0:len(a[1])-1].split(',')
            e=int(c[0][2:len(c[0])-1])
            f=int(a[2][2:len(a[2])-2])
            b.append((e,f))
        else:
            c=a[1][0:len(a[1])-1].split(',')
            if len(c)==2:
                c=a[1][0:len(a[1])-1].split(',')
                e=int(c[0][2:len(c[0])-1])
                f=int(c[1][2:len(c[1])-1])
                b.append((e,f))
                pass
        line=cirt.readline()
    cirt.close()
    nb = list(set(b))
    nb.sort(key=b.index)
    return  nb

    pass
def wenjian(lis,lisn):
    for nam in lis:
        b=cirt(a[0]+"/"+nam)
        c=coup(a[1])
        print(nam)
        h,z=c[0]
        reg=b[0]
        qubit=h
        b.pop(0)
        c.pop(0)
        #print(b)
        #print(c)
        d={}
        nu,ma=match(b,c,d,h)
        if nu==-1:
            print("no")
            pass
        else:
            print("reg|qubit")
            print(ma)
            replace(lisn+"/"+nam,ma,lisn)
        pass

def dange(cr,cp):
    b=cirt(cr)
    c=coup(cp)
    h,z=c[0]
    reg=b[0]
    qubit=h
    b.pop(0)
    c.pop(0)
    #print(b)
    #print(c)
    d={}
    print(b)
    nu,ma=match(b,c,d,h)
    if nu==-1:
        print("no")
        pass
    else:
        print("reg|qubit")
        print(ma)
        replace(a[0],ma,"")


if __name__ == "__main__":
    fio=input("Please choose mode: folder or file(If you want to test folder, please input fo. If you want to test file, please input fi):")
    if fio=="fo":
        print("Please input in that form: dic coup")
        a = list(input(' ').split())
        lis=os.listdir('./circuits/'+a[0])
        wenjian(lis,a[0])
    else:
        print("Please input in that form: dic/cirt coup")
        a = list(input(' ').split())
        dange(a[0],a[1])
    print("Done.")
