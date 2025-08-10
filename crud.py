# from sqlalchemy.orm import Session
# import models, schemas

# # ---------- Users ----------
# def create_user(db: Session, user: schemas.UserCreate):
#     db_user = models.User(**user.dict())
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def get_users(db: Session):
#     return db.query(models.User).all()

# # ---------- Activities ----------
# def create_activity(db: Session, activity: schemas.ActivityCreate):
#     db_activity = models.Activity(**activity.dict())
#     db.add(db_activity)
#     db.commit()
#     db.refresh(db_activity)
#     return db_activity

# def get_activities(db: Session):
#     return db.query(models.Activity).all()

# # ---------- Progress ----------
# def create_progress(db: Session, progress: schemas.ProgressCreate):
#     db_progress = models.Progress(**progress.dict())
#     db.add(db_progress)
#     db.commit()
#     db.refresh(db_progress)
#     return db_progress

# def get_progress(db: Session):
#     return db.query(models.Progress).all()
