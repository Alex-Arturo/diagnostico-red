import subprocess
import os
from typing import Dict
import platform
from registro_log import registro_log

def obtener_comando_interfaces():
    sistema = platform.system().lower()
    if "linux" in sistema:
        return ["ip", "addr"]
    elif "windows" in sistema:
        return ["ipconfig"]
    elif "darwin" in sistema:
        return ["ifconfig"]
    else:
        return["echo", "Comando no soportado"]


def ping_subprocess(directorio : str = "resultados_red", host :str = "google.com", cantidad :int = 4)->None:
    try:
        comandos = {f"interfaces":obtener_comando_interfaces(), 
                    f"ping_{host}":["ping", "-c",f"{cantidad}" , host], 
                    f"ip_publica": ["curl","ifconfig.me"]
                    }
        for clave, lista_comandos in comandos.items():
            resultado = subprocess.run(
                lista_comandos,
                capture_output=True,
                text=True,
                check=True
            )
            if os.path.exists(f"{directorio}/"):
                with open(f"resultados_red/{clave}.txt", "w") as f:
                    f.write(resultado.stdout)
                print(f"El resultado fue guardado con exito en el archivo {clave}.txt.")
            else:
                print("El directorio no existe.")
                return

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        with open("error.txt", "w") as f:
            f.write(e.stderr)

def ejecutar_traceroute(host):
    try:
        # Windows usa 'tracert', Linux/Mac usan 'traceroute'
        comando = ["tracert", host] if subprocess.run(["uname"], capture_output=True).returncode != 0 else ["traceroute", host]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        return resultado.stdout
    except Exception as e:
        return f"Error ejecutando traceroute: {e}"



