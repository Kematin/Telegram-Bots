from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, UploadFile, status
from fastapi.responses import FileResponse
from loguru import logger
from pydantic import UUID4, BaseModel

from admin.auth import authenticate, create_access_token
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


class ProjectCreate(BaseModel):
    name: str
    summary: str
    price: int
    have_presentation: bool
    have_product: bool
    have_unique: bool
    category: str

    class Config:
        json_schema_extra = {
            "example": {
                "name": "name",
                "summary": "summary",
                "price": 799,
                "have_presentation": False,
                "have_product": False,
                "have_unique": False,
                "category": "minimum",
            }
        }


class ProjectChange(BaseModel):
    name: Optional[str] = None
    summary: Optional[str] = None
    price: Optional[int] = None
    have_presentation: Optional[bool] = None
    have_product: Optional[bool] = None
    have_unique: Optional[bool] = None
    is_blocked: Optional[bool] = None
    category: Optional[str] = None

    class Config:
        json_schema_extra = {"example": {"price": 899, "is_blocked": True}}


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
    project_id: UUID4,
    db=Depends(get_db),
    admin: str = Depends(authenticate),
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
    data: ProjectCreate,
    db=Depends(get_db),
    admin: str = Depends(authenticate),
):
    project_database = Database(Project, db)
    if data.category not in config.CATEGORIES:
        logger.warning(f"Invalid category for new project with data {data}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid category."
        )
    await project_database.create(data.model_dump())
    logger.info(f"Create new project with data {data}")
    return {"message": "succesfull"}


@admin_router.put("/project/{project_id}")
async def update_project(
    project_id: UUID4,
    data: ProjectChange,
    db=Depends(get_db),
    admin: str = Depends(authenticate),
):
    project_database = Database(Project, db)
    res = await project_database.update(project_id, data.model_dump())
    if not res:
        logger.warning(f"Project with id {project_id} not found.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with id {project_id} not found.",
        )
    logger.info(f"Update project with id {project_id}")
    return {"message": "succesffull"}


@admin_router.delete("/project/{project_id}")
async def delete_project(
    project_id: UUID4, db=Depends(get_db), admin: str = Depends(authenticate)
):
    project_database = Database(Project, db)
    res = await project_database.delete(project_id)
    if res:
        logger.info(f"Delete project {project_id}.")
        return {"message": "succesfull"}
    else:
        logger.warning(f"Project with id {project_id} not found.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with id {project_id} not found.",
        )


@admin_router.delete("/project")
async def delete_projects(db=Depends(get_db), admin: str = Depends(authenticate)):
    project_database = Database(Project, db)
    await project_database.delete_all()
    logger.info("Delete all projects")
    return {"message": "succeffull"}


@admin_router.get("/logs")
async def get_logs(admin: str = Depends(authenticate)):
    log_file = "./logs/debug.log"
    return FileResponse(path=log_file, filename="logs.log")
