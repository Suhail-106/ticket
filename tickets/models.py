from django.db import models
import uuid

class Ticket(models.Model):
    code = models.UUIDField(default=uuid.uuid4, unique=True)
    is_redeemed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.code)
    
