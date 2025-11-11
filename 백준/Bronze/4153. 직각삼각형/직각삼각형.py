while True:
    a,b,c = map(int, input().split())
    
    if a == 0 and b == 0 and c ==0:
        break
        
    sides = sorted([a,b,c])
    x,y,z = sides
    
    if x*x +y*y == z*z:
        print("right")
    else:
        print("wrong")