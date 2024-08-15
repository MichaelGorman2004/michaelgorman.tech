from pydantic import BaseModel


class ProjectBase(BaseModel):
    title: str
    description: str
    github_link: str
    live_link: str


class ProjectCreate(ProjectBase):
    pass


class ProjectInDBBase(ProjectBase):
    id: int

    class Config:
        orm_mode = True


class Project(ProjectInDBBase):
    pass
