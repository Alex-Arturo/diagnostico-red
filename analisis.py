from datetime import datetime as dt
from typing import List
from ping_subprocess import ping_subprocess, ejecutar_traceroute
from registro_log import registro_log


def leer_ping(ruta_archivos: str, archivo_ping : str, host : str = "google.com", cantidad_pings : int = 4)->List[float]:
    latencias : List[float] = []
    with open(f"{ruta_archivos}/{archivo_ping}", "r") as f:
        texto = f.read()
        lista_analisis= texto.split("\n")[:cantidad_pings+1]
        for t in lista_analisis:
            if "ms" in t:
                lista_ping = t.split()
                lista_ping[-2]
                datos = lista_ping[-2].split("=")
                latencia_actual = float(datos[-1])
                latencias.append(latencia_actual)      
    registro_log(f"Comando ejecutado: ping {host}", "diagnostico.log")
    registro_log(f"Archivo leído: {archivo_ping}", "diagnostico.log")
    registro_log(f"Latencias extraídas: {latencias}", "diagnostico.log")
    return latencias

def calcular_promedio(latencias : List[float]):
    total_latencias : float = 0
    for latencia_actual in latencias:
        total_latencias+= latencia_actual
    if len(latencias)==0:
        raise ValueError("No se encontraron latencias válidas.")
    promedio = total_latencias / len(latencias)
    registro_log(f"Promedio de latencias: {promedio} ms","diagnostico.log")
    return promedio

def extraer_ip( ruta_archivos : str, archivo_ip_publica : str )-> str:
    with open(f"{ruta_archivos}/{archivo_ip_publica}", "r")as f:
        contenido = f.read().strip()
        registro_log(f"IP pública extraída: {contenido}","diagnostico.log")
        return contenido


def generar_reporte(promedio : float, ip_publica : str, cantidad_respuestas : int, ruta_salida : str, host :str = "google.com" )->None:
    with open(ruta_salida, "w") as f:
        fecha =dt.now().strftime("%Y/%m/%d")
        f.write(f"Analisis de resultados de red\nFecha: {fecha}\nHost: {host}\n")
        f.write(f"Promedio de lactencia: {promedio}ms ({cantidad_respuestas} respuestas)\n")
        f.write(f"IP pública: {ip_publica}\n")
        if promedio > 0:
            f.write("Conexión estable. No se detectaron errores en la ejecución de los comandos.")
        else:
            f.write(f"Problemas en la conexión.")


def analisis(ruta_archivos : str, archivo_ping : str, archivo_ip_publica : str, archivo_salida: str = "analisis_resultados.txt", host: str = "google.com", cantidad : int = 4)->None:
    try:
        if cantidad == 0:
            cantidad = 1
            registro_log("Cantidad de paquetes ajustado a 1 (no se permiten 0)", "diagnostico.log")
        ping_subprocess("resultados_red", host, cantidad)
        registro_log(f"Inicio del diagnóstico para {host}", "diagnostico.log")
        latencias = leer_ping(ruta_archivos, archivo_ping, host, cantidad)
        print("\n--- Traceroute ---")
        print(ejecutar_traceroute(host))
        promedio = calcular_promedio(latencias)
        ip = extraer_ip(ruta_archivos, archivo_ip_publica)
        generar_reporte(promedio, ip, len(latencias), archivo_salida, host)
        registro_log("Reporte generado correctamente.", "diagnostico.log")
        registro_log(f"Diagnóstico finalizado para {host}.", "diagnostico.log")
        print("Reporte generado con éxito.")
    except Exception as e:
        print(f"Problemas al generar reporte - ERROR : {e}")



print("Ejecutando diagnóstico desde rama dev")
