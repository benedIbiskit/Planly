from fastapi import FastAPI

app = FastAPI(
    title="Planly",
    description="Приложение для управления подписками. API учебного проекта Planly.",
    version="0.2.0",
)

TEAM_NAME = "Planly"


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint."""
    return {"message": "Hello World"}


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}


@app.get("/version")
async def version() -> dict[str, str]:
    """Версия приложения и команда-владелец."""
    return {"version": app.version, "team": TEAM_NAME}
