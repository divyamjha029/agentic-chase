
from sqlalchemy import Column, String, Text
from database import Base

class Project(Base):
    __tablename__ = "projects"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)

class ChatContext(Base):
    __tablename__ = "chats"
    id = Column(String, primary_key=True, index=True)
    project_id = Column(String, index=True) # Links chat to a specific project workspace
    chat_type = Column(String) # Stores either "GROUP" or "DIRECT"
    title = Column(String)

class Persona(Base):
    __tablename__ = "personas"
    participant_id = Column(String, primary_key=True, index=True)
    chat_id = Column(String, index=True) # Locks the persona strictly to a specific chat context
    name = Column(String)
    base_tone = Column(Text) # e.g., "sarcastic, uses short sentences"
    communication_habits = Column(Text) # e.g., "sends voice notes frequently"
