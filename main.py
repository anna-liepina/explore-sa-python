from fastapi import FastAPI
from strawberry.asgi import GraphQL

from api import schema

app = FastAPI()

@app.get("/")
def index():
    return {"message": "index"}

app.add_route("/graphql", GraphQL(schema, debug=True))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)