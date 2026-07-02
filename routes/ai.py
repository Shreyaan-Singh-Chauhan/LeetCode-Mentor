from fastapi import APIRouter
from services.ollama_service import ask_llm

router = APIRouter()


@router.get("/test-ai")
def test_ai():

    reply = ask_llm("How do I solve Two Sum?")

    return {
        "response": reply
    }