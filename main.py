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
def get_tweets(query: str = ""):
    tweets = fetch_tweets(query=query)
    return {"tweets": tweets}

@app.get("/trends")
def trends_route():
    trends = get_trends()
    return {"trends": trends}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about")
def read_about():
    return {"About": "This is a simple FastAPI application"}

users=[
    {"id":1 , "name":"sadaf"},
    {"id":2 , "name":"ramu"},
    {"id":3 , "name":"javeria"},    
]

@app.get("/users")
def user():
    return users

@app.get("/users/{id}")
def user(id: int):
 for u in users:
  if u["id"] == id:
    return u
  return("error:user not found")

@app.post("/users")
def create_user(user:dict):
  users.append(user)
  return user


@app.get("/users/{id}")
def user(id: int):
  for u in users:
    if u["id"] == id:
        user.remove(u)
        return u
        return("error:user not found")








