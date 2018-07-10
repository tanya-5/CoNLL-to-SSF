import nltk, re,os
from nltk import word_tokenize
import time

x=1
y=10
f = open('input.txt', encoding="utf-8")
n = open('file1.txt','w+')
p = open('output.txt','w+')
nps=1
chunkidp=0
count=1
pcount=1
prel=""
nrel=""
store=[0]

for line in f:
    m=line.strip()
    if len(m)==0:
        n.write("\t))\t"+prel+"\n*<"+"/Sentence>"+"\n\n")
        l=len(store)
        x+=1
        nps=1
        count=1
        pcount=1
        y=10
        n.close()
        
        
        with open("file1.txt",encoding="utf-8") as file1:
            for block in file1.read().split("*"):
                pass
                b=block.split()
                if b[0]=='<Sentence' or b[0]=='</Sentence>':
                    b1 = ' '.join(b)
                    p.write(b1 + "\n")
                else:
                    i=int(b[-1])                    
                    b[-1]= re.sub("\d+",store[i],b[-1])
                    if i==0:
                        drel=b[-1]
                    else:    
                        drel="drel='"+ b[-2] + b[-1]+"'>"
                    b[3]="<fs "+b[3]+" "+drel
                    del b[-1]
                    del b[-1]
                    length=len(b)-4
                    start=b[0:4]
                    b1 = '\t'.join(start)
                    p.write(b1+"\n")
                    a=4
                    z=8
                    while length>1:
                        length=length-4  
                        b[z-1]=re.sub('-',' ',b[z-1])
                        start=b[a:z]
                        b1 = '\t'.join(start)
                        p.write(b1+"\n")
                        a=z
                        z=z+4      
                    p.write("\t))\n")
            p.write("\n")
            store=[0]
        os.remove('file1.txt')
        n = open('file1.txt','a')
    else:
        m= re.sub('chunkId',' ',m)
        m= re.sub('\|chunkType',' ',m)
        m= re.sub('\|stype',' ',m)
        m= re.sub('\|voicetype',' ',m)
        list= m.split()
        if list[11]=='main':
            list[8]= re.sub('-',"",list[8])
            list[9]= re.sub('-',"",list[9])
            stype="stype='"+ list[8]+"'"
            voicetype="voicetype='"+ list[9]+"'>"
            store[0]=stype+" "+voicetype
        indexes = [2, 4, 8,9,12,13]
        for index in sorted(indexes, reverse=True):
            del list[index]
        if list[2]=='SYM':
            if list[1]!='।':
                list[1]= ','
        list[3]= re.sub('lex-',"<fs-af='",list[3])
        list[3]= re.sub('cat-|gen-|num-|pers-|case-|vib-|tam-','',list[3])
        list[3]= re.sub('\|',',',list[3])
        list[3]=list[3][:-1]
        list[3]=list[3]+"'-"+"name='"+list[1]+"'-posn='"+str(y)+"'>"
        chunkidn=list[4]
        list[4]= re.sub('-',"",list[4])
        store.append(list[4])
##        print(store)
        if chunkidn=='-':
            chunkidn='none'
        else:
            chunkidn= re.sub('-','',chunkidn)
        cid = chunkidn   
        if list[5]=='-head':
            nrel=list[7]+":\t"+list[6]
        if list[0]=='1':
            n.write("<Sentence id='"+str(x)+"'>\n")
            prel=nrel
        if chunkidp!=chunkidn:
             if list[0]!='1':
                 n.write("\t))\t"+ prel+"\n")
                 count+=1
                 pcount=1
                 cid = re.sub("\d+","", cid)
             n.write("*"+str(count)+"\t(("+"\t"+cid+ "\tname='"+chunkidn+"'\n")
        indexes = [0,4,5,6,7]
        for index in sorted(indexes, reverse=True):
            del list[index]
        m = '\t '.join(list)
        chunkidp=chunkidn
        n.write(str(count)+"."+str(pcount)+"\t" +m + '\n')
        y+=10
        pcount+=1
        prel=nrel  
f.close()
p.close() 



