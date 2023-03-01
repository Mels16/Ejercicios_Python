#Realizar un progrma que conste de un clase llmada alumno que tebga como atributo el nombre.
#definir los metodos para definir sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y 
#si ha aprobado o no .


class Alumno (): 
    #nota minima para pasar
    
    nota_minima = 3.5
    
    def __init__(self,nombre,nota): 
        #definir el nombre y la nota del alumno
        self.nombre= nombre
        self.nota = nota
            
        
    def aprobado(self): 
        #definir si el estudiante paso  la materia
        if self.nota >=3.5: 
            print("la nota ha sido aprobada")
        
M=Alumno("Lisay",4.0)
M.aprobado()






