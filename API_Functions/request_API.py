import json
import datetime
import requests

def set_Register(chamber, partNum, serie, leak, state=0, user=7172):
    try:
        url = 'http://10.1.0.187:8086/registros'
        data = {"proveedor": "ZAR", "cabina": chamber, "codigo": f"{partNum}", "serie": f"{serie}", "fuga": leak,
                "operador": user, "estado": state}

        # Encabezados (headers) de la solicitud
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        # Envío de la solicitud POST
        response = requests.post(url, headers=headers, data=json.dumps(data))

        # Verifica la respuesta
        if response.status_code == 201:
            print("Solicitud exitosa:", response.json())
        else:
            print(f"Error {response.status_code}: {response.text}")

    except Exception as e:
        print("Error en la connexion con la API, Verificar WIFI")

def Get_totalCores(partNum):
    try:
        url = f"http://10.1.0.187:8086/registros/{partNum}/?consulta=total"

        # Encabezados de la solicitud
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Envío de la solicitud GET
        response = requests.get(url, headers=headers)

        # Verifica la respuesta
        if response.status_code == 201:  # Código 200 indica éxito en GET
            data = response.json()  # Convertir la respuesta a JSON
            # print(data.get("data"))
            return data.get("data")  # Devolver solo el contenido de "data"

        else:
            # print(f"Error {response.status_code}: {response.text}")
            return 0
    except Exception as e:
        print("Error en la connexion con la API, Verificar WIFI")