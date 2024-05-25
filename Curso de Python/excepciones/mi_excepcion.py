#creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Impresionante, cometiste el siguiente error: {err}")

#lanzando mi propia excepcion
#raise MiExcepcion("jaaaajaaaaa, no podeeeeees")

#manejandola        
try:
    raise MiExcepcion("jaaaajaaaaa, no podeeeeees")
except:
    print("Como vas a cometer ese error?")