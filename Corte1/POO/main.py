from clase import Square, Add_Sub1

object1 = Square(5)  
print(f"De la clase 'square': {object1.getval()}")  


object2 = Add_Sub1()  
object2.add(2, 3) 
object2.imprimirResultado()  

object2.sub(2, 3)  
object2.imprimirResultado()