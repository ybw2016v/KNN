#python3
import re
def zjl(namedog):
    hulldog=namedog
    lindogv=[]
    lindog1=[]
    pudog=[]
    eedog=[]
    pptdog=re.compile(r"([0-9]{0,}\.{0,}[0-9]{0,})(\([^)]*\))(([A-Z][a-z]{0,2}[0-9]{0,}\.{0,}[0-9]{0,}){0,})")
    hhdog=pptdog.findall(namedog)
    ppxdog=re.compile(r'([A-Z][a-z]{0,2})([0-9]{0,}\.{0,}[0-9]{0,})')
    if hhdog==[]:
        hhdog=namedog
        pptcdog=re.compile(r'([A-Z][a-z]{0,2})([0-9]{0,}\.{0,}[0-9]{0,})')
        hhdog=pptcdog.findall(hhdog)
        #print(hhdog)
        return hhdog


    else:
        pass
    for idog in hhdog:
        lindog1=[]

        havedog=ppxdog.findall(idog[1])
        idog=list(idog)
        if idog[0]=='':
            idog[0]='1'
        else:
            pass

        numdog=float(idog[0])
        havedog2=[]
        for jdog in havedog:
            jdog=list(jdog)
            if jdog[1]=='':
                jdog[1]='1'
            else:
                pass

            jdog[1]=numdog*float(jdog[1])
            pudog.append(jdog)
            havedog2.append(jdog)
        lindog1.append(havedog2)
        #print(lindog1)
        havedog3=ppxdog.findall(idog[2])
        havedog4=[]
        for kdog in havedog3:
            kdog=list(kdog)
            if kdog[1]=='':
                kdog[1]='1'
            else:
                pass
            kdog[1]=numdog*float(kdog[1])


            havedog4.append(kdog)
            pudog.append(kdog)
        lindog1.append(havedog4)
    #print(pudog)

    for oodog in pudog:
        bidog=oodog[0]
        #tiao=pudog.index(oodog)
        for zzdog in pudog:
            if zzdog[0]==bidog and pudog.index(oodog)!=pudog.index(zzdog):
                oodog[1]=oodog[1]+zzdog[1]
                pudog.remove(zzdog)
            else:
                pass
        eedog.append(oodog)
    #print(eedog)


    return eedog




#print(zjl('0.96(K0.48Na0.52Nb0.96Sb0.04)O3+0.04(Bi0.5Na0.5)ZrO3'))
#print(zjl('Na0.25K0.75'))

