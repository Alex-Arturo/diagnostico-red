# Diagnóstico de Red

Este proyecto automatiza pruebas de conectividad usando `ping` y `curl`, 
genera reportes individuales por host y mantiene un log consolidado.

## Archivos principales
- `ping_subprocess.py` → ejecuta comandos y guarda resultados.
- `analisis.py` → procesa latencias, IP pública y genera reportes.
- `diagnostico.log` → historial técnico paso a paso.

## Cómo usar
```bash
python analisis.py

---

