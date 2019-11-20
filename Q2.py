#Q2
def inverte_matriz2x2(matriz):
    deter=(matriz[0][0]*matriz[1][1]) - (matriz[0][1]*matriz[1][0])

    if deter == 0
        return None

    na = matriz[1][1] * deter                           #should be (1/deter)
    nb = -(matriz[0][1] * deter)
    nc = -(matriz[1][0] * deter)
    nd = matriz [0][0] * deter

    inverted = [[na,nb],[nc,nd]]

    return inverted

def main()
    mtz = [[0,0],[0,0]]
    print("insira o : \n")
    mtz[0][0] = float(input("\'a\' de sua matriz"))         #missing \n
    mtz[0][1] = float(input("\'b\' de sua matriz"))
    mtz[1][0] = float(input("\'c\' de sua matriz"))
    mtz[1][1] = float(input("\'d\' de sua matriz"))

    print("matriz antes da inversão: \n")
    print(str(mtz[0][0]) + "\t" + str(mtz[0][1]) + "\n")        #check formatation
    print(str(mtz[1][0]) + "\t" + str(mtz[1][1]) + "\n")

    print("matriz invertida: \n")
    ivtd = inverte_matriz2x2(mtz)
    if ivtd == None:
        print("a determinante é igual à 0")                     #fix error msg
    else:
        print(str(ivtd[0][0]) + "\t" + str(ivtd[0][1]) + "\n")
        print(str(ivtd[1][0]) + "\t" + str(ivtd[1][1]) + "\n")

main()
