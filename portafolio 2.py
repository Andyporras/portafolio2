"""
nombre:invertirLista
entrada: una lista
salida: lista invertida
restricciones: debe ser una lista el dato a ingresar
"""

def invertirLista(lista):
    if(isinstance(lista,list)):
        if(lista==[]):
            return 0
        else:
            return invetirLista_aux(lista,[])
    else:
        print(f"Error, el dato {lista} no es una lista")

def invetirLista_aux(lista,result):
    if(lista==[]):
        return result
    else:
        return invetirLista_aux(lista[:-1],result+[lista[-1]])
#--------------------------------------------------------------------------------------

"""
nombre: extremosLista
entrada: una lista
salida: el numero menor y mayor de la lista
restrincciones: debe ser una lista 
"""

def extremosLista(lista):
    if(isinstance(lista,list)):
        if(lista==[]):
            return f"Error,la lista esta vacio."
        else:
            menor=menor_aux(lista,lista[0])
            mayor=mayor_aux(lista,lista[0])
            return  extremosLista_aux(menor,mayor,[])
    else:
        return f"Error, el dato ingresado ({lista}) no es una lista."


def menor_aux(lista,result):
    if(lista==[]):
        return result
    elif(int(lista[0]))<result:
        return menor_aux(lista[1:],lista[0])
    else:
        return menor_aux(lista[1:],result)

def mayor_aux(lista,result):
    if(lista==[]):
        return result
    elif(int(lista[0]))>result:
        return mayor_aux(lista[1:],lista[0])
    else:
        return mayor_aux(lista[1:],result)

def extremosLista_aux(menor,mayor,result):
    if(menor==0)or mayor==0:
        return result
    elif(menor==mayor):
        return [mayor]
    else:
        return extremosLista_aux(0,0,result+[menor]+[mayor])


"""
nombre:eliminarDigito
entrada:num= un numero entero
sacar=un numero entero
salida: el numero pero sin el numero que se saca
restrincciones: los 2 parametros debe ser un entero positivo
"""

def eliminarDigito(num,sacar):
    if(isinstance(num,int)and isinstance(sacar,int)and sacar>=0)and num>=0:
       if(num==0):
           return 0
       else:
           return eliminarDigito_aux(str(num),str(sacar),"")
    else:
        return f"Error, el numero {num} no es un numero entero."
def eliminarDigito_aux(num,sacar,result):
    if(num==""):
        return int(result)
    elif(num[0]==sacar):
        return eliminarDigito_aux(num[1:],sacar,result)
    else:
        return eliminarDigito_aux(num[1:],sacar,result+num[0])

#-----------------------------------------------------------------------

"""
nombre: nivelesLista
entrada: una lista con sub lista
salida: cantidad de sublista que contiene la lista
restricciones: debe ser una lista el dato de entrada.
"""


def nivelesLista(lista):
    if(isinstance(lista,list)):
        return nivelesLista_aux(lista,[])
    else:
        return f"Error, el dato ingresado ({lista}), no es una lista."

def nivelesLista_aux(lista,result):
    if(lista==[]):
        return result
    else:
        
        if(isinstance(lista[0],list)):
            subLista=contar_aux(lista[0],1)
            return nivelesLista_aux(lista[1:],result+[subLista])
        else:
            return nivelesLista_aux(lista[1:],result+[0])

def contar_aux(lista,cont):
    if(lista==[]):
        return cont
    else:
        if(isinstance(lista[0],list)):
           return contar_aux(lista[0],cont+1)
        else:
            return 1

#----------------------------------------------------------------------------

"""
nombre:obtenerIndicesListaVectore
entrada:tres vectores 
salida:los indice de los numero que sea igual a cero o menor a cero en la lista
restricciones:debe ser lista los tres datos ingresados, solo debe tener un tipo de dato los vectores en la lista
solo debe haber entero,las 3 lista o vectores debe tener el mismo tamaño.

"""
def obtenerIndicesListaVectore(vector1,vector2,vector3):
    if(isinstance(vector1,list)and isinstance(vector2,list))and isinstance(vector3,list):
        if(verificar_aux(vector1)):
            if(verificar_aux(vector2)):
                if(verificar_aux(vector3)):
                    if(tamaño_aux(vector1,vector2,vector3)==1):
                        indice1=indices_aux(vector1,0,[])
                        indice2=indices_aux(vector2,0,[])
                        indice3=indices_aux(vector3,0,[])
                        return [indice1]+[indice2]+[indice3]
                    else:
                        return f"ERROR,tamaños distintos de los vectores"
                else:
                    return f"ERROR,el vector3 ({vector3}) no tiene todos los datos de tipo entero "
            else:
                return f"ERROR,el vector2 ({vector2}) no tiene todos los datos de tipo entero"
        else:
            return f"ERROR,el vector1 ({vector1}) no tiene todos los datos de tipo entero"
    else:
        return f"ERROR,debe ingresar tres vectores que sean lista. "



def verificar_aux(vector):
    if(vector==[]):
        return True
    else:
        if(isinstance(vector[0],int)):
            return verificar_aux(vector[1:])
        else:
            return False

def tamaño_aux(vector1,vector2,vector3):
    if(vector1==[])or vector2==[] or vector3==[]:
        if(vector1==[])and vector2==[] and vector3==[]:
            return True
        else:
            return False

    else:
        return tamaño_aux(vector1[1:],vector2[1:],vector3[1:])

def indices_aux(vector,cont,result):
    if(vector==[]):
        return result
    elif(vector[0]<=0):
        return indices_aux(vector[1:],cont+1,result+[cont])
    else:
        return indices_aux(vector[1:],cont+1,result)
            
        
        
                        




                        
