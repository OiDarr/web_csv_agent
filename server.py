from fastapi import FastAPI
from pydantic import BaseModel

from agent import get_csv_agent_response

app = FastAPI()


class RequestModel(BaseModel):
    text: str


@app.post("/api/get-agent-response")
async def generate_description_by_article(request: RequestModel):
    text = request.text
    response = get_csv_agent_response(text)
    return {"response": response}
