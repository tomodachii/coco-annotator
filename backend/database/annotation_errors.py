from mongoengine import *

class AnnotationErrorModel(EmbeddedDocument):
    id = SequenceField(primary_key=True)
    problem = StringField(required=False)
    box_id = IntField(required=False)
    keypoint_id = IntField(required=False)

__all__ = ["AnnotationErrorModel"]