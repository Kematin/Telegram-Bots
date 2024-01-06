from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from loguru import logger
from pydantic import BaseModel

from auth import authenticate, create_access_token
from config import config
from database import AsyncSessionLocal, Database, Files, Project

admin_router = APIRouter(tags=["Admin"])


# dependency
async def get_db():
    try:
        db = AsyncSessionLocal()
        yield db
    finally:
        await db.close()


class AuthAdmin(BaseModel):
    username: str
    password: str

    class Config:
        json_schema_extra = {"example": {"username": "admin", "password": "password"}}


class ProjectChange(BaseModel):
    name: str
    summary: str
    price: int
    have_presentation: bool
    have_product: bool
    have_unique: bool
    is_blocked: bool | None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "name",
                "summary": "summary",
                "price": 799,
                "have_presentation": True,
                "have_product": True,
                "have_unique": True,
                "is_blocked": False,
            }
        }


class FilesChange(BaseModel):
    pass


@admin_router.post("/auth", status_code=status.HTTP_202_ACCEPTED)
async def auth_admin(data: AuthAdmin) -> dict:
    username, password = data.username, data.password
    if username != config.ADMIN_USERNAME or password != config.ADMIN_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Wrong credentials."
        )
    access_token = create_access_token(username)
    logger.info("Admin user sign in")
    return {"access_token": access_token, "token_type": "Bearer"}


@admin_router.get("/projects")
async def retrieve_projects(db=Depends(get_db), admin: str = Depends(authenticate)):
    project_database = Database(Project, db)
    projects = await project_database.get_all()
    logger.info("Get all projects.")
    return {"projects": projects}


@admin_router.get("/project/{project_id}")
async def retrieve_single_project(
    project_id: int, db=Depends(get_db), admin: str = Depends(authenticate)
):
    project_database = Database(Project, db)
    project = await project_database.get(project_id)
    if project:
        logger.info(f"Get project {project_id}.")
        return {"project": project}
    else:
        logger.warning(f"Project with id {project_id} not found.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with id {project_id} not found.",
        )


@admin_router.post("/project")
async def create_project(
    data: ProjectChange, db=Depends(get_db), admin: str = Depends(authenticate)
):
    project_database = Database(Project, db)
    await project_database.create(data.model_dump())
    logger.info(f"Create new project with data {data}")
    return {"message": "succesfull"}
