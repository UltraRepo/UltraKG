from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel
from fastapi_amis_admin.models.fields import Field

class APIKey(SQLModel, table=True):
    __tablename__ = "api_keys"
    
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    name: str = Field(title='Name', max_length=100, unique=True, index=True, nullable=False)
    key: str = Field(title='API Key', max_length=100, unique=True, index=True, nullable=False)
    description: str = Field(default='', title='Description', max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow, title='Created At')
    last_used: Optional[datetime] = Field(default=None, title='Last Used') 