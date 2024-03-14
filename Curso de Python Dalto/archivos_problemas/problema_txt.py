#dos listas una con nombrwes otrta conm apeliidos
nombres = ["Lucas","Chris","Eric","Pedro","Roberto"]
apellidos = ["Huxx","Makin","Debris","lang","Aelo"]

#registrar esta informacion en un TXT de forma optima
with open("archivos_problemas_resueltos\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-------------\n") for n,a in zip(nombres,apellidos)]
    

#FORMA NO OPTIMA
#for n,a in zip(nombres,apellidos):
    #arch.writelines(f"Nombre: {n}\nApellido: {a}\n--------\n")
    