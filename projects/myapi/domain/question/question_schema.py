import datetime
from pydantic import BaseModel, field_validator,Field
from domain.answer.answer_schema import Answer
from domain.user.user_schema import User
from typing import Union

class Question(BaseModel):
  id:int
  subject: str
  content: str
  create_date: datetime.datetime
  answers: list[Answer]=[]
  user: Union[User, None]
  modify_date: Union[datetime.datetime,None] = None

  
class QuestionCreate(BaseModel):
  subject: str
  content: str

  
  @field_validator('subject','content')
  def not_empty(cls, v):
    if not v or not v.strip():
      raise ValueError('not allow empty value')
    return v
class QuestionList(BaseModel):
  total: int =0
  question_list: list[Question] = []

class QuestionUpdate(QuestionCreate):
  question_id:int

class QuestionDelete(BaseModel):
  question_id: int