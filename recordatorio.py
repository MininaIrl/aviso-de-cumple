import traceback
import datetime
import os 

try:
    import json
    from plyer import notification

    # Detectamos la ruta de forma automática y anónima
    DIRECTORIO = os.path.dirname(os.path.abspath(__file__))
    RUTA_JSON = os.path.join(DIRECTORIO, 'cumpleanos.json')
    
    # Añadimos encoding='utf-8' para evitar errores con tildes o la Ñ
    with open(RUTA_JSON, 'r', encoding='utf-8') as archivo:
        cumpleanos = json.load(archivo)

    hoy = datetime.datetime.now()
    proximos_cumpleaneros = []

    # Revisar los próximos 7 días
    for i in range(7):
        dia_revision = hoy + datetime.timedelta(days=i)
        fecha_str = dia_revision.strftime("%m-%d")
        
        for nombre, fecha in cumpleanos.items():
            if fecha == fecha_str:
                proximos_cumpleaneros.append(f"{nombre} ({fecha_str})")

    if proximos_cumpleaneros:
        nombres_texto = "\n".join(proximos_cumpleaneros)
        mensaje = f"Cumpleaños de esta semana:\n{nombres_texto}"
        
        notification.notify(
            title='🎂 Cumpleaños de la semana',
            message=mensaje,
            app_name='Recordatorio',
            timeout=15
        )

except Exception as e:
    # Si algo falla, el error se guarda en la misma carpeta del script
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_log = os.path.join(directorio_actual, 'registro_error.txt')
    
    with open(ruta_log, 'w', encoding='utf-8') as f:
        f.write("ERROR DETECTADO:\n")
        f.write(traceback.format_exc())