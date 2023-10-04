from fastapi import APIRouter, Depends
from ..dependencies.get_token import get_token

APIRouter(), Depends(), get_token()
