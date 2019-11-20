#Q3
def isCollisionDetected(rect1, rect2):   
    if rect1["bottomLeft"][0] > rect2["bottomLeft"][0]:             #corrigi a sintaxe da chamada de dicionário
        if rect1["bottomLeft"][0] < rect2["topRight"][0]:
            if rect1["bottomLeft"][1] > rect2["bottomLeft"][1]:
                if rect1["bottomLeft"][1] < rect2["topRight"][1]:
                    return True
    
    if rect2["bottomLeft"][0] > rect1["bottomLeft"][0]:                     #adicionei lógica
        if rect2["bottomLeft"][0] < rect1["topRight"][0]:
            if rect2["bottomLeft"][1] > rect1["bottomLeft"][1]:
                if rect2["bottomLeft"][1] < rect1["topRight"][1]:
                    return True
    
    if rect1["bottomLeft"][0] > rect2["bottomLeft"][0]:             
        if rect1["bottomLeft"][0] < rect2["topRight"][0]:
            if rect2["bottomLeft"][1] > rect1["bottomLeft"][1]:
                if rect2["bottomLeft"][1] < rect1["topRight"][1]:
                    return True
    
    if rect2["bottomLeft"][0] > rect1["bottomLeft"][0]:             
        if rect2["bottomLeft"][0] < rect1["topRight"][0]:
            if rect1["bottomLeft"][1] > rect2["bottomLeft"][1]:
                if rect1["bottomLeft"][1] < rect2["topRight"][1]:
                    return True
    
    return False
        
def main():         #adicionei a main e terminei a lógica que estava faltando
    BLx = float(input('digite a cordenada x do canto inferior esquerdo do primeiro retangulo: \n'))
    BLy = float(input('digite a cordenada y do canto inferior esquerdo do primeiro retangulo: \n'))
    TRx = float(input('digite a cordenada x do canto superior direito primeiro retangulo: \n'))
    TRy = float(input('digite a cordenada y do canto superior direito do primeiro retangulo: \n'))

    rect1 = {'bottomLeft': (BLx,BLy), 'topRight': (TRx,TRy) }

    BLx = float(input('digite a cordenada x do canto inferior esquerdo do segundo retangulo: \n'))
    BLy = float(input('digite a cordenada y do canto inferior esquerdo do segundo retangulo: \n'))
    TRx = float(input('digite a cordenada x do canto superior direito segundo retangulo: \n'))
    TRy = float(input('digite a cordenada y do canto superior direito do segundo retangulo: \n'))

    rect2 = {'bottomLeft': (BLx,BLy), 'topRight': (TRx,TRy) }

    collision = isCollisionDetected(rect1,rect2)
    
    if collision:
        print('Colisão detectada')
    else:
        print('colisão não detectada')
main()