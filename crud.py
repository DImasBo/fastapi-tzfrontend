from sqlalchemy.orm import Session
import models, schemas

def create_comment( db: Session, comment: schemas.CommentCreate):
    db_comment = models.Comment(name=comment.name, description=comment.description, image_id=comment.image_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comments( db: Session, image_id):
    return db.query(models.Comment).filter(models.Comment.image_id == image_id).all()