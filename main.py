from fastapi import FastAPI
from file import fetch_tweets, get_trends
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/tweets")
def get_tweets_route(query: str = ""):
    tweets = fetch_tweets(query=query)
    if tweets is None:
        return {"error": "The entered query is not a place."}
    if not tweets:
        return {"error": "No tweets found"}
    return {"tweets": tweets}

@app.get("/trends")
def get_trends_route():
    trends = get_trends()
    return {"trends": trends}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about")
def read_about():
    return {"About": "This is a simple FastAPI application"}

users = [
    {"id": 1, "name": "sadaf"},
    {"id": 2, "name": "ramu"},
    {"id": 3, "name": "javeria"},
]

@app.get("/users")
def get_all_users():
    return users

@app.get("/users/{id}")
def get_user(id: int):
    for u in users:
        if u["id"] == id:
            return u
    return {"error": "user not found"}

@app.post("/users")
def create_user(user: dict):
    users.append(user)
    return user

@app.delete("/users/{id}")
def delete_user(id: int):
    for i, u in enumerate(users):
        if u["id"] == id:
            deleted_user = users.pop(i)
            return deleted_user
    return {"error": "user not found"}
