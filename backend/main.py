from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from scr.database.db import get_db
from scr.routes import auth, users

app = FastAPI(title="PoopOK", description="Welcome to PoopOK API",
              swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

app.include_router(auth.router, prefix='/api', tags=['Authentication'])
app.include_router(users.router, prefix='/api', tags=['Users'])


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
