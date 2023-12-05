from django.db import models
import uuid
from datetime import datetime


class BaseModel(models.Model):
    """
    Abstract base class for all models.
    """
    id = models.CharField(primary_key=True, max_length=100, blank=False, null=False, unique=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __init__(self, *args, **kwargs):
        """
        Constructor for BaseModel.
        """
        super().__init__(*args, **kwargs)
        if not self.id:
            self.id = str(uuid.uuid4())
        if not self.created_at:
            self.created_at = datetime.utcnow()
        if not self.updated_at:
            self.updated_at = datetime.utcnow()

    def save(self, *args, **kwargs):
        """
        Save method for BaseModel.
        """
        self.updated_at = datetime.utcnow()
        super().save(*args, **kwargs)        

    class Meta:
        abstract = True