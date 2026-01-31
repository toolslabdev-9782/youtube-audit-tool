from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.youtube_api import router as youtube_router
from backend.facebook_api import router as facebook_router

app = FastAPI(
    title="Audit Platform API",
    description="YouTube & Facebook Audit APIs",
    version="1.0"
)

# -------------------------
# CORS
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# HOME
# -------------------------
@app.get("/")
def home():
    return {"message": "Audit API is running"}

# -------------------------
# ROUTERS
# -------------------------
app.include_router(youtube_router, prefix="/api/youtube", tags=["YouTube Audit"])
app.include_router(facebook_router, prefix="/api", tags=["Facebook Audit"])
