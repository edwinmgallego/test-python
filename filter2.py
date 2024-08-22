palabras =["gato","perro","vaca","caballo","raton"]

palabras_largas= filter(lambda palabra: len(palabra)>4,palabras)
print(list(palabras_largas))