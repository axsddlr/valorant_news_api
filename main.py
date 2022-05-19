import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from api.scrape import Valo

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="Unofficial Valorant News API",
    description="An Unofficial News REST API for [Valorant](https://playvalorant.com/), Made by [Andre "
                "Saddler]( "
                "https://github.com/axsddlr)",
    version="1.0.0",
    docs_url="/",
    redoc_url=None,
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# init limiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# init classes
vlrnt = Valo()


@app.get("/valorant/{locale}/patch-notes", tags=["Valorant"])
@limiter.limit("250/minute")
def valorant_patch_notes(request: Request, locale):
    return vlrnt.patch_notes(locale)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000)
