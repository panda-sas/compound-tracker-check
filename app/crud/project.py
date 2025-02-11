from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate

def create_project(db: Session, project_data: ProjectCreate):
    db_project = Project(**project_data.model_dump(exclude_unset=True))
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.ProjectId == project_id).first()

def update_project(db: Session, project_id: int, project_data: ProjectUpdate):
    db_project = db.query(Project).filter(Project.ProjectId == project_id).first()
    if db_project:
        for key, value in project_data.model_dump(exclude_unset=True).items():
            setattr(db_project, key, value)
        db.commit()
        db.refresh(db_project)
    return db_project

def delete_project(db: Session, project_id: int):
    db_project = db.query(Project).filter(Project.ProjectId == project_id).first()
    if db_project:
        db.delete(db_project)
        db.commit()
    return db_project

def get_all_projects(db: Session):
    return db.query(Project).all()
