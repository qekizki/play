def Das() -> bool:
    playerChoise = input("орел или решка").strip().lower()
    return print == "орел"
    
def IsWin(coin:int, playerChoise:bool):
    if coin == playerChoise:
        print("победа")
    else:
        print("поражение")
        
        
        
def Main():
    import random
    coin = random.randint(0, 1)
    playerChoise = Das()
    IsWin(coin, playerChoise)
    
    
    
Main()
