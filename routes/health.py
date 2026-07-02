from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {"message": "Leet Mentor Backend Running 🚀"}


@router.get("/health")
def health():
    return {"status": "running"}