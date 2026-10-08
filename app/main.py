from fastapi import FastAPI

app = FastAPI(title="CI/CD Demo")

@app.get("/")
def home():
    return {
        "message": "Hello Students hello docker!",
        "version": "1.0"
        
    }

@app.get("/about")
def about():
    return {
        "project": "FastAPI CI/CD Demo",
        "technology": "FastAPI + Docker + GitHub Actions"
    }
