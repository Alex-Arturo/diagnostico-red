# Diagnóstico de Red

Este proyecto automatiza pruebas de conectividad y análisis de red, generando reportes individuales por host y manteniendo un log consolidado para seguimiento técnico.

## 📂 Archivos principales
- **ping_subprocess.py** → ejecuta comandos del sistema (`ping`, `curl`, `ipconfig/ifconfig`) y guarda resultados en archivos.
- **analisis.py** → procesa latencias, extrae la IP pública y genera reportes detallados.
- **diagnostico.log** → historial técnico con marcas de tiempo y eventos del diagnóstico.

## ⚙️ Funcionalidades
- Configuras la cantidad de paquetes de `ping`.
- Analiza múltiples hosts en una sola ejecución.
- Genera reportes `analisis_resultados_HOST.txt` con promedio de latencias e IP pública.
- Mantiene un log consolidado `diagnostico.log`.
- Ajusta automáticamente el mínimo de paquetes a 1 para evitar errores.

## 🚀 Cómo usar
1. Clona el repositorio:
   ```bash
   git clone git@github.com:Alex-Arturo/diagnostico-red.git
   cd diagnostico-red
   ```
2. Ejecuta el comando:
   - En  **Windows**: `python analisis.py` 
   - En **Linux/Mac**: `python3 analisis.py`

## 📊 Ejemplo de salida
```bash
Analisis de resultados de red
Fecha: 2025/11/26
Host: google.com
Promedio de latencia: 34.5 ms (4 respuestas)
IP pública: 189.xxx.xxx.xxx
Conexión estable. No se detectaron errores en la ejecución de los comandos.
```
## 👨‍💻 Autor
Proyecto desarrollado por Alex como parte de un proyecto personal de programación y ciberseguridad.




