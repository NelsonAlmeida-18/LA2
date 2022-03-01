codigo = "int x;x=0;x=x+1;"
codigo = "int main() {int x;x=0;     x=x+1;}"
codigo= "int main(){ if (x==2){ x+=1;} else{x+=2;}}"

def indenta(codigo):
    newStr =""
    codigo= codigo.split(";")
    linhaInit =0
    for linha in codigo:
        pos=0
        while(linha[pos]==" "):
            pos+=1
        if linhaInit==0:
            newStr+="\n  "+linha+";\n"
            linhaInit+=1
        elif "}" in linha:
            newStr+="}"
        else:
            newStr+="  "+linha[pos:]+";\n"
    #print(newStr)
    return newStr

def formata(codigo):
    newStr = ""
    pos=0
    numOcorr = codigo.count(";")
    num=0
    for char in codigo:
        if char=="{":
            newStr+="{"
            newStr+=indenta(codigo[pos+1:])
            print(newStr)
            return newStr
        else:
            if char ==";" and num<numOcorr-1:
                newStr+=";\n"
                num+=1
            elif char==";" and num==numOcorr:
                newStr+=";"
                num+=1
            else:
                newStr+=char
        pos+=1
    print(newStr)
formata(codigo)