import textwrap

codigo = "int x;x=0;x=x+1;"
codigo = "int main() {int x;x=0;     x=x+1;}"
codigo= "int main(){ if (x==2){ x+=1;} else{x+=2;}}"

def indenta(codigo):
    newStr=""
    numOfSpaces

def formata(codigo):
    newStr = ""
    pos=0
    while(pos<len(codigo)-1):
        if codigo[pos]=="{":
           newStr+=indenta(codigo[pos:])
        if codigo[pos]==";":
            newStr+=";\n  "
        else:
            newStr+=codigo[pos]
        pos+=1
    print(newStr)

formata(codigo)