"""
Boss AI - main application entry point
central hub for fast api applications

- creates the fast api instances
- connects to the databse
- mounts static files (html)
includes routers for authentic, profile managment.
- includes dashboard
- defines settigns

- add ai endpoints
        - goals
        - task
        -journal
        -boss chat
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api import auth, profile, dashboard

#fast api app
app = FastAPI(
    title="Boss AI",
    description="Ai- driven boss who gets you to do your work."
)

#static files
app.mount("/static", statsicFiles(directory="static"), name="static")


#routers (APi Endpoints)

#auth.py:login, register
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

#profile.py: creates / updates profile
app.include_router(profile.router, prefix="/profile", tags=["profile"])

#dashboard.py: user dashboard after login
app.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])

#root route

@app.get("/")

def read_root():
    """
    landing endpoint
    in production, Homepage
    :return: welcome to boss ai
    """
    return {"message": "Welcome, my name is shenny your boss. login to start.  "}



