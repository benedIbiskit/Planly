from fastapi import FastAPI

app = FastAPI(
    title="Planly",
    description="Приложение для управления подписками. Базовый API практики №1.",
    version="0.1.0",
)


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint."""
    return {"message": "Hello World"}


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}
