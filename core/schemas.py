
# the menue, whats allowed to be orderd



from typing import Optional, List
from datetime import datetime, date
from pydantic import BaseModel, EmailStr



# USER & AUTH

class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(UserBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True



# PROFILE

class ProfileBase(BaseModel):
    boss_type: Optional[str] = "default"   # enum: default, funny, serious, minion
    preferences: Optional[dict] = {}

class ProfileCreate(ProfileBase):
    goals: Optional[List[str]] = []

class ProfileResponse(ProfileBase):
    user_id: str
    goals: Optional[List[str]] = []

    class Config:
        orm_mode = True



# GOALS

class GoalBase(BaseModel):
    title: str
    description: Optional[str] = None
    thesis_statement: Optional[str] = None

class GoalCreate(GoalBase):
    pass

class GoalUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    thesis_statement: Optional[str]

class GoalResponse(GoalBase):
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# TASKS

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None

class TaskCreate(TaskBase):
    goal_id: str

class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]   # pending, in-progress, completed
    due_date: Optional[datetime]

class TaskResponse(TaskBase):
    id: str
    goal_id: str
    status: str
    created_at: datetime

    class Config:
        orm_mode = True


# JOURNAL

class JournalBase(BaseModel):
    entry_type: str   # morning or evening
    content: str

class JournalCreate(JournalBase):
    pass

class JournalResponse(JournalBase):
    id: str
    user_id: str
    date: date
    analysis: Optional[dict] = None

    class Config:
        orm_mode = True



# NOTIFICATIONS

class NotificationBase(BaseModel):
    message: str
    channel: str   # app, whatsapp, email

class NotificationCreate(NotificationBase):
    pass

class NotificationResponse(NotificationBase):
    id: str
    user_id: str
    timestamp: datetime
    ai_reason: Optional[str] = None

    class Config:
        orm_mode = True



# TEAM MEMBERS

class TeamMemberBase(BaseModel):
    name: str
    role: Optional[str] = None

class TeamMemberCreate(TeamMemberBase):
    pass

class TeamMemberResponse(TeamMemberBase):
    id: str
    user_id: str
    assigned_tasks: Optional[List[str]] = []

    class Config:
        orm_mode = True


# AI PROMPTS / RESPONSES
