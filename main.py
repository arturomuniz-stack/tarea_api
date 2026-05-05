from fastapi import FastAPI
import requests

app = FastAPI()

SUPABASE_URL = "https://tsblrsuyugeonexdfnic.supabase.co"
API_KEY = "sb_publishable_Eb-fLuY733NREcFFQ4G_yQ_kVN1c3zN"

@app.get("/")
def read_root():
    return {"mensaje": "API funcionando correctamente"}

@app.get("/api/unidades")
def get_unidades():
    try:
        url = f"{SUPABASE_URL}/rest/v1/unidades?select=id,nom_estab,raz_social&limit=50"

        headers = {
            "apikey": API_KEY,
            "Authorization": f"Bearer {API_KEY}"
        }

        response = requests.get(url, headers=headers)
        return response.json()

    except Exception as e:
        return {"error": str(e)}
    
@app.get("/api/unidades/id/{id}")
def get_unidad_por_id(id: int):
    try:
        url = f"{SUPABASE_URL}/rest/v1/unidades?id=eq.{id}&select=*"

        headers = {
            "apikey": API_KEY,
            "Authorization": f"Bearer {API_KEY}"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        if len(data) == 0:
            return {"mensaje": "No encontrado"}

        return data[0]

    except Exception as e:
        return {"error": str(e)}
    
@app.get("/api/unidades/buscar")
def buscar_unidades(nombre: str):
    try:
        url = f"{SUPABASE_URL}/rest/v1/unidades?nom_estab=ilike.*{nombre}*&select=*&limit=50"

        headers = {
            "apikey": API_KEY,
            "Authorization": f"Bearer {API_KEY}"
        }

        response = requests.get(url, headers=headers)
        return response.json()

    except Exception as e:
        return {"error": str(e)}
    
@app.get("/api/estadisticas/total_por_estado")
def total_por_estado():
    try:
        url = f"{SUPABASE_URL}/rest/v1/unidades?select=entidad"

        headers = {
            "apikey": API_KEY,
            "Authorization": f"Bearer {API_KEY}"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        conteo = {}

        for item in data:
            estado = item.get("entidad")

            if estado in conteo:
                conteo[estado] += 1
            else:
                conteo[estado] = 1

        resultado = []
        for estado, total in conteo.items():
            resultado.append({
                "estado": estado,
                "total": total
            })

        return resultado

    except Exception as e:
        return {"error": str(e)}
    
@app.get("/api/unidades/filtro")
def filtrar_unidades(estado: str = None, actividad: str = None):
    try:
        filtros = []

        if estado:
            filtros.append(f"entidad=eq.{estado}")

        if actividad:
            filtros.append(f"nombre_act=ilike.*{actividad}*")

        query = "&".join(filtros)

        url = f"{SUPABASE_URL}/rest/v1/unidades?{query}&select=*&limit=50"

        headers = {
            "apikey": API_KEY,
            "Authorization": f"Bearer {API_KEY}"
        }

        response = requests.get(url, headers=headers)
        return response.json()

    except Exception as e:
        return {"error": str(e)}
    
@app.get("/api/unidades/perfil/{id}")
def perfil_completo(id: int):
    try:
        url = f"{SUPABASE_URL}/rest/v1/unidades?id=eq.{id}&select=*"

        headers = {
            "apikey": API_KEY,
            "Authorization": f"Bearer {API_KEY}"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        if len(data) == 0:
            return {"mensaje": "No encontrado"}

        u = data[0]

        resultado = {
            "id": u.get("id"),
            "nombre": u.get("nom_estab"),
            "razon_social": u.get("raz_social"),

            "ubicacion": {
                "estado": u.get("entidad"),
                "municipio": u.get("municipio"),
                "colonia": u.get("nomb_asent")
            },

            "actividad": {
                "nombre": u.get("nombre_act")
            }
        }

        return resultado

    except Exception as e:
        return {"error": str(e)}
    
@app.get("/api/unidades/cercanas")
def unidades_cercanas(lat: float, lon: float, radio: float):
    try:
        url = f"{SUPABASE_URL}/rest/v1/unidades?select=*"

        headers = {
            "apikey": API_KEY,
            "Authorization": f"Bearer {API_KEY}"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        resultado = []

        for u in data:
            lat_db = u.get("latitud")
            lon_db = u.get("longitud")

            # Si no hay coordenadas, se ignora
            if lat_db is None or lon_db is None:
                continue

            # Distancia simple (NO exacta, pero suficiente)
            distancia = ((lat - lat_db)**2 + (lon - lon_db)**2) ** 0.5

            if distancia <= radio:
                resultado.append(u)

        return resultado

    except Exception as e:
        return {"error": str(e)}