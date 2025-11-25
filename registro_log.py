from datetime import datetime as dt

def registro_log(mensaje : str, nombre_archivo : str)->None:
    with open(nombre_archivo, "a") as t:
        timestap = dt.now().strftime("[%Y/%m/%d %H:%M:%S]")
        t.write(f"{timestap}  {mensaje}\n")