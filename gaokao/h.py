import os
import math
import json
li2017={}
li2018={}
li2019={}
li2020={}
li2020zx={}
li2021zx={}
li2021fs={}
li2021={}
li2021ex={}
li2021zxex={}
li2021zxfs={}
rdata={}
with open("2017li.txt", "r") as f:  # 打开文件
     data = f.read()  # 读取文件
     h=data.split("|")
     for i in h:
         ll=i.split('#')
         li2017[ll[0]]=ll[1]
with open("2018li.txt", "r") as f:  # 打开文件
     data = f.read()  # 读取文件
     h=data.split("|")
     for i in h:
         ll=i.split('#')
         li2018[ll[0]]=ll[1]
with open("2019li.txt", "r") as f:  # 打开文件
     data = f.read()  # 读取文件
     h=data.split("|")
     for i in h:
         ll=i.split('#')
         li2019[ll[0]]=ll[1]
with open("2020li.txt", "r") as f:  # 打开文件
     data = f.read()  # 读取文件
     h=data.split("|")
     for i in h:
         ll=i.split('#')
         li2020[ll[0]]=ll[1]
with open("2021li.txt", "r") as f:  # 打开文件
     data = f.read()  # 读取文件
     h=data.split("|")
     for i in h:
         ll=i.split('#')
         li2021[ll[0]]=ll[1]
with open("2021li.txt", "r") as f:  # 打开文件
     data = f.read()  # 读取文件
     h=data.split("|")
     for i in h:
         ll=i.split('#')
         li2021fs[ll[1]]=ll[0]
with open("2020zxjh.txt", "r") as f:  # 打开文件
     data = f.read()  # 读取文件
     h=data.split("|")
     for i in h:
         ll=i.split('#')
         li2020zx[ll[0]]=ll[1]   
with open("2021zxjh.txt", "r") as f:  # 打开文件
     data = f.read()  # 读取文件
     h=data.split("|")
     for i in h:
         ll=i.split('#')
         li2021zx[ll[0]]=ll[1]   
with open("2021zxjh.txt", "r") as f:  # 打开文件
     data = f.read()  # 读取文件
     h=data.split("|")
     for i in h:
         ll=i.split('#')
         li2021zxfs[ll[1]]=ll[0]   
for i in range(0,8000):
    if(str(i) in li2021zxfs.keys()):
        li2021zxex[str(i)]=li2021zxfs[str(i)]
    else:
        j=i
        while(str(j) not in li2021zxfs.keys()):
            j=j+1
        li2021zxex[str(i)]=li2021zxfs[str(j)]

for i in range(0,80000):
    if(str(i) in li2021fs.keys()):
        li2021ex[str(i)]=li2021fs[str(i)]
    else:
        j=i
        while(str(j) not in li2021fs.keys()):
            j=j+1
        li2021ex[str(i)]=li2021fs[str(j)]
print(li2021zxex)
with open("2020.txt", "r",encoding='utf-8') as f:  # 打开文件
     data = f.read()  # 读取文件
     h=data.split("|")
     for i in h:
         ll=i.split('#')
         if len(ll)==4 and ll[3] != '':
             rdata[ll[0]]={}
             rdata[ll[0]]['code']=ll[0]
             rdata[ll[0]]['school']=ll[1]
             rdata[ll[0]]['pm2020']=li2020[ll[3]]
             rdata[ll[0]]['fs2020']=ll[3]
             rdata[ll[0]]['zxpm2020']=li2020zx[ll[3]]
with open("2019.txt", "r") as f:  # 打开文件
     data = f.read()  # 读取文件
     h=data.split("|")
     for i in h:
         ll=i.split('#')
         if len(ll)==4 and ll[3] != '' and (ll[0] in rdata.keys()):
             rdata[ll[0]]['pm2019']=li2019[ll[3]]
             rdata[ll[0]]['fs2019']=ll[3]
with open("2018.txt", "r") as f:  # 打开文件
     data = f.read()  # 读取文件
     h=data.split("|")
     for i in h:
         ll=i.split('#')
         if len(ll)==4 and ll[3] != '' and ll[3]!='0' and (ll[0] in rdata.keys()):
             rdata[ll[0]]['pm2018']=li2018[ll[3]]
             rdata[ll[0]]['fs2018']=ll[3]
with open("2017.txt", "r") as f:  # 打开文件
     data = f.read()  # 读取文件
     h=data.split("|")
     for i in h:
         ll=i.split('#')
         if len(ll)==4 and ll[3] != '' and ll[3]!='0' and (ll[0] in rdata.keys()):
             rdata[ll[0]]['pm2017']=li2017[ll[3]]
             rdata[ll[0]]['fs2017']=ll[3]
with open("gx2.txt", "r",encoding='utf-8-sig') as f:  # 打开文件
     data = f.read()  # 读取文件
     h=data.split("|")
     for i in h:
         
         ll=i.split('#')
         lll=ll[1].split("&")
         print(ll)
         rdata[ll[0]]['name']=lll[0]
         rdata[ll[0]]['position']=lll[1]
for key in rdata.keys():
    ldata=rdata[key]
    if('pm2018' not in ldata.keys()):
        ldata['pm2018']=str(int((int((ldata['pm2019']))*1.05)))
    if('pm2017' not in ldata.keys()):
        ldata['pm2017']=str(int((int((ldata['pm2018']))*1.05)))    
    lsa=(int(ldata['pm2020'])-int(ldata['pm2019']))*0.3+(int(ldata['pm2019'])-int(ldata['pm2018']))*0.6
    lsa=lsa+(int(ldata['pm2018'])-int(ldata['pm2017']))*0.1
    rdata[key]['lsa']=lsa
    ygpm=int(ldata['pm2020'])+int(ldata['pm2019'])+int(lsa*2)
    ygpm=int(ygpm/2)
    rdata[key]['expm1']=ygpm
    dlsa=lsa/int(ldata['pm2020'])
    rdata[key]['a']=str(int(lsa*10000/int(ldata['pm2020']))/100)
    zxygpm=int(ldata['zxpm2020'])
    zxygfs=int(li2021zxex[str(zxygpm)])
    ygfs=math.floor(zxygfs*0.5+int(li2021ex[str(ygpm)])*0.5)+1
    rdata[key]['ygfs']=str(ygfs)
data2 = json.dumps(rdata)
print(len(rdata.keys()))
with open('h.json','w') as f:
    f.write(data2)

    

