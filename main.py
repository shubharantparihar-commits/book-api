from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hellow_world():
    return {"hello-world": "Hello World"}

@app.get("/health")
def health_status():
    return {"status": "Good"}

@app.get("/items")
def get_items(skip: int = 0, limit: int = 10, q: str | None = None ):
    results = [
        {"item_id": 1,"name": "Laptop"},
        {"item_id": 2,"name": "Charger"}
    ]
    if q is not None:
        results = [item for item in results if q.lower() in item["name"].lower()]
    return results[skip : skip + limit]


@app.get("/items/{item_id}")
def get_itemid(item_id: int):
    if item_id == 2:
        return {
            "item_id": 2,
            "name": "Charger"
        }


@app.get("/users/me")
def get_user_me():
    return {
        "user_id": 0,
        "name": "Me"
    }

@app.get("/users/{user_id}")
def get_userid(user_id: int):
    if user_id == 1:
        return {
            "user_id": 1,
            "user_name": "Lorence"
        }
