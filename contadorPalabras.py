import re
class CuentaPalabrasArchivo:

    wordcount = {}

    def __init__(self):
        print("Inicia contador de palabras")

    def admin_file(self, archivo):
        #Inicia admin de archivo
        self.archivo = archivo
        print("Contando las palabras del archivo: "+self.archivo)
        with open(archivo) as file:
            for word in file.read().split():
                # Extrae caracteres
                partes = re.split(r'(\W+)|(?<!\d)[,.;]|[,.;](?!\d)', word)
                for i in partes:
                    print("Parte:" +i)
                    if (i != ''):
                        if i not in self.wordcount:
                            self.wordcount[i] = 1
                        else:
                            self.wordcount[i] += 1

        print(self.wordcount)

obj = CuentaPalabrasArchivo()
obj.admin_file("./ejemplo.txt")
