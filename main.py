from fastapi import FastAPI
from app.routes import router
from app.config import settings

"""
Aplicación FastAPI para Quiz de PSeInt con IA

Esta aplicación genera quizzes interactivos de PSeInt utilizando IA (Google Gemini).
Los usuarios pueden responder preguntas de análisis de código PSeInt secuencial
y recibir retroalimentación inmediata sobre sus respuestas.

Características principales:
- Generación automática de preguntas con IA
- Sistema de sesiones para seguimiento de progreso
- Cache de preguntas para mejor rendimiento
- Validación rigurosa de preguntas generadas

Autor: Sistema de Quiz PSeInt
Versión: 1.0.2
"""

app = FastAPI(
    title="PSeInt Quiz App",
    description="Generador de Quizzes Interactivas con IA",
    version="1.0.2"
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
