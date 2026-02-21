# 🎂 Aviso de Cumple

Sistema sencillo en Python para gestionar y recibir notificaciones de cumpleaños directamente en el escritorio.

## ¿Qué hace?
* **Gestión de fechas:** Permite guardar y actualizar nombres con sus respectivos cumpleaños (formato MM-DD).
* **Alertas automáticas:** Escanea la lista y lanza una notificación de Windows si alguien cumple años en los próximos 7 días.
* **Almacenamiento local:** Guarda todo en un archivo `cumpleanos.json` dentro de la misma carpeta.

## ¿Cómo funciona?
1. **Interfaz (`interfaz.py`):** Ejecutas este archivo para abrir una ventana donde registras a tus amigos.
2. **Lógica (`recordatorio.py`):** Compara la fecha actual con los datos del JSON. Si hay coincidencias cercanas, activa la notificación de sistema.
3. **Lanzador (`lanzador.bat`):** Un archivo ejecutable que facilita la automatización para que el programa corra en segundo plano al encender la PC.

## Instalación rápida
1. Instala la librería necesaria:
   ```bash
   pip install plyer
