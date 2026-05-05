# API + BI
Este proyecto integra una arquitectura de datos utilizando Excel, Supabase, FastAPI y Power BI para el análisis de unidades económicas.

Flujo de datos:

Excel → Supabase (PostgreSQL) → API (FastAPI) → Power BI

Los datos se almacenan en Supabase, se consultan mediante una API desarrollada en FastAPI y se visualizan en un dashboard interactivo en Power BI.



# API (FastAPI)

Endpoints desarrollados:

- GET /api/unidades → listado general
- GET /api/unidades/{id} → consulta por ID
- GET /api/unidades/buscar → búsqueda por nombre
- GET /api/estadisticas/total_por_estado → KPI por estado
- GET /api/unidades/filtro → filtros dinámicos
- GET /api/unidades/perfil_completo → información completa
- GET /api/unidades/cercanas → búsqueda geoespacial

# Ejecución 

Para ejecutar la API:

uvicorn main:app --reload

Ejemplo:

http://127.0.0.1:8000/api/unidades


## Despliegue

Se intentó el despliegue en PythonAnywhere pero por la incompatibilidad entre WSGI y ASGI (FastAPI), no se pudo publicar la API en línea.

La API funciona en entorno local.

# Base de Datos

Se utilizó Supabase como base de datos PostgreSQL.

Se creó la tabla "unidades" con campos como:

- id
- nom_estab
- raz_social
- entidad
- nombre_act

---

# Dashboard

El dashboard fue desarrollado en Power BI.

Incluye:

- KPI: total de unidades económicas
- Gráfica de barras por estado
- Gráfica de pastel por actividad
- Filtros interactivos

Archivo dashboard.pbix


# Insights

Insight 1
Se identificó que ciertos estados concentran una mayor cantidad de unidades económicas, lo que indica mayor actividad económica en esas regiones.

Insight 2
Al analizar las actividades económicas, se observa que algunos sectores predominan, lo que puede indicar tendencias del mercado y oportunidades de negocio.

---

#Tecnologías utilizadas

- Python (FastAPI)
- Supabase (PostgreSQL)
- Power BI
- GitHub