#Q3
def is CollisionDetected(rect1, rect2):
    if rect1."bottomLeft"[0] > rect2."bottomLeft"[0]:
        if rect1."bottomLeft"[0] > rect2."topRight"[0]:
            if rect1."bottomLeft"[1] > rect2."bottomLeft"[1]:
                if rect1."bottomLeft"[1] > rect2."topRight"[1]:
                    return True
        
