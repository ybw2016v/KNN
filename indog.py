#python3
import re
from zjl import zjl
def shi(setdog):

    res=zjl(setdog)
    # pptdog=re.compile(r'([A-Z][a-z]{0,2})([0-9]{0,}\.{0,}[0-9]{0,})')
    # #setdog='Na2.5S1O4'#input('in:')
    # hhdog=pptdog.findall(setdog)
    #print(hhdog)
    return res

#print(shi("(Na0.25K)C3O2+0.75(Na0.25K0.75)C2S2O"))
