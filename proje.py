x = [9,2,5,4,12,7,8,11,9,3,7,4,12,5,4,10,9,6,9,4]
y = [1,1,1,2,2,2,3,3,5,8,9,9,9,15,15,14,13,12,12,15,15]


def ortalamaBul(vektor):
    veriAdedi = len(vektor)
    if veriAdedi <= 1:
        return vektor
    else:
        return sum(vektor) / veriAdedi
    

def medyanBul(vektor):
    vektor = sorted(vektor)
    veriAdedi = len(vektor)
    if veriAdedi % 2 == 1:
        return vektor[veriAdedi // 2]
    else:
        i = veriAdedi // 2
        return (vektor[i - 1] + vektor[i]) / 2
    
def standartSapmaBul(vektor):
    sd = 0.0 # standart sapma
    veriAdedi = len(vektor)
    if veriAdedi <= 1:
        return 0.0
    else:
        for _ in vektor:
            sd += (float(_) - ortalamaBul(vektor)) ** 2
        sd = (sd / float(veriAdedi)) ** 0.5
        return sd
    
print(standartSapmaBul(x))
print(standartSapmaBul(y))
print(medyanBul(x))
print(medyanBul(y))
print(ortalamaBul(x))
print(ortalamaBul(y))

    
def varyansBul(vektor):
     return standartSapmaBul(vektor) ** 2