from database import SessionLocal
from models import Question
from datetime import datetime
db=SessionLocal()
for i in range(300):
  q=Question(subject="배고파이 :{}".format(i),content="테스트데이터",create_date=datetime.now())
  db.add(q)
db.commit()