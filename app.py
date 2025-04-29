# app.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
import time

app = FastAPI()

# Configuración de templates (usa la carpeta 'templates')
templates = Jinja2Templates(directory="templates")

# Configuración
AGENT_ID = "asst_HriembvdBALUOb4R31pVK0uL"
API_KEY = "1kJRofLM1rUsAaUY2vnKpJ3kpkZ2885iHD1aZgGZ9IcMvMAJDGQtJQQJ99BDACHYHv6XJ3w3AAAAACOG7Stx"

# Inicializar cliente del proyecto
try:
    project_client = AIProjectClient.from_connection_string(
        credential=DefaultAzureCredential(),
        conn_str="eastus.api.azureml.ms;91c10a2b-e8c8-4e07-82f1-35560d0bb7bc;ai-agents;re-estate-agents"
    )
except Exception as e:
    print("Error en la conexión:", e)

# Crear thread de conversación
thread = project_client.agents.create_thread()
print(f"Thread creado, ID: {thread.id}")

@app.get("/", response_class=HTMLResponse)
async def chat(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@app.post("/send_message")
async def send_message(request: Request):
    body = await request.json()
    user_input = body.get("user_input")

    if not user_input:
        return JSONResponse({"assistant_response": "No se recibió mensaje del usuario."})

    try:
        # Crear mensaje del usuario
        project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )

        # Ejecutar el agente
        run = project_client.agents.create_run(thread_id=thread.id, agent_id=AGENT_ID)

        # Esperar a que el run termine
        while True:
            run = project_client.agents.get_run(thread_id=thread.id, run_id=run.id)
            if run.status in ['completed', 'failed', 'cancelled']:
                break
            time.sleep(1)

        if run.status != "completed":
            return JSONResponse({"assistant_response": "Ocurrió un error al procesar tu solicitud."})

        # Obtener el mensaje del asistente
        messages = project_client.agents.list_messages(thread_id=thread.id)

        assistant_response = ""

        for msg in sorted(messages['data'], key=lambda x: x['created_at'], reverse=True):
            if msg['role'] == 'assistant':
                content_list = msg.get('content', [])
                for content in content_list:
                    if 'text' in content:
                        assistant_response = content['text'].get('value', 'Sin respuesta')
                break

        return JSONResponse({"assistant_response": assistant_response})

    except Exception as e:
        print("Error procesando mensaje:", e)
        return JSONResponse({"assistant_response": "Error interno del servidor."})
