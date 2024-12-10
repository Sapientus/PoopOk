from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

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

app.include_router(auth.router, prefix='/api', tags=['Authentication'])
app.include_router(users.router, prefix='/api', tags=['Users'])
app.include_router(posts_comments.router, prefix='/api', tags=['Comments and Posts'])
app.include_router(attacks.router, prefix='/api', tags=['Attacks'])
app.include_router(toilet_session.router, prefix='/api', tags=['Toilet Sessions'])
app.include_router(achievement.router_achievements, prefix='/api', tags=['Achievements'])
app.include_router(armor.router_armor, prefix='/api', tags=['Armor'])
app.include_router(curse.router_curse, prefix='/api', tags=['Curse'])
# app.include_router(posts.post_router, prefix='/api', tags=['Posts'])
# app.include_router(comments.comment_router, prefix='/api', tags=['Comments'])


@app.get("/api/healthchecker", tags=['Health checker'])
async def healthchecker(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT 1"))
        result = result.fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to the database")
