from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from src.i18n.translations import I18nMiddleware, translator

from src.database.db import get_db
from src.routes import (
    auth,
    users,
    attacks,
    toilet_session,
    achievement,
    armor,
    curse, posts_comments
)

app = FastAPI(title="PoopOK", description="Welcome to PoopOK API",
              swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})
app.add_middleware(I18nMiddleware, default_language="uk")  # noqa

app.include_router(auth.router, prefix='/api', tags=['Authentication'])
app.include_router(users.router, prefix='/api', tags=['Users'])
app.include_router(posts_comments.router, prefix='/api', tags=['Comments and Posts'])
app.include_router(attacks.router, prefix='/api', tags=['Attacks'])
app.include_router(toilet_session.router, prefix='/api', tags=['Toilet Sessions'])
app.include_router(achievement.router_achievements, prefix='/api', tags=['Achievements'])
app.include_router(armor.router_armor, prefix='/api', tags=['Armor'])
app.include_router(curse.router_curse, prefix='/api', tags=['Curse'])


@app.get("/api/healthchecker", tags=['Health checker'])
async def healthchecker(db: AsyncSession = Depends(get_db), t: callable = Depends(translator)):
    try:
        result = await db.execute(text("SELECT 1"))
        result = result.fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail=t("health.db_config_error"))
        return {"message": t("health.welcome")}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=t("health.db_config_error"))
