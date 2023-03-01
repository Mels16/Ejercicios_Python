class Robot():
    def __init__(self,x,y) -> None:
        self.x = x 
        self.y=y
    
    def arriba(self,y):
        
        self.y = self.y+y


    def abajo(self,y):
        
        self.y = self.y-y
    
    def izquierda(self,x):
        self.x =self.x+x
        
    
    def derecha(self,x):
        
        self.x =self.x-x
    
    def vissualizar(self): 
        print(f"arriba{self.x} es: ")
    
        
Kimetsu = Robot()
Kimetsu.arriba(3)

