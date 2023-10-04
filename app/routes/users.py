from ._imports import *

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/me")
async def my_data(token=Depends(get_token)):
    return token
