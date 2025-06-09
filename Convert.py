import io
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import io
import re
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def leer_y_extraer_valores_vv_vh():
    """
    Abre un archivo .txt con datos hexadecimales, los convierte a ASCII y extrae los valores de Vv y Vh.

    Returns:
        tuple: (ascii_text:str, vv_valor:str|None, vh_valor:str|None)
    """
    try:
        # Oculta la ventana principal
        root = Tk()
        root.withdraw()

        # Diálogo de selección de archivo
        ruta_archivo = askopenfilename(
            title="Selecciona un archivo con datos hexadecimales",
            filetypes=[("Archivos de texto", "*.txt")]
        )

        if not ruta_archivo:
            print("No se seleccionó ningún archivo.")
            return None, None, None

        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()

            # Separa y limpia los hexadecimales
            hex_values = contenido.strip().split()
            bytes_data = bytes(int(h, 16) for h in hex_values)

            # Convierte a ASCII
            ascii_text = bytes_data.decode('ascii', errors='ignore')

            # Busca los valores con expresiones regulares
            vv_match = re.search(r'Vv:(\d+)', ascii_text)
            vh_match = re.search(r'Vh:(\d+)', ascii_text)

            vv_valor = vv_match.group(1) if vv_match else None
            vh_valor = vh_match.group(1) if vh_match else None

            return ascii_text, vv_valor, vh_valor

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None, None, None

ascii_texto, vv, vh = leer_y_extraer_valores_vv_vh()
if ascii_texto:
    #print("Texto ASCII completo:")
    #print(ascii_texto)
    print("Vv:", vv)
    print("Vh:", vh)