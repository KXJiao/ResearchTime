from django.db import models
from django.utils import timezone
import json

class Article(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    summary = models.TextField()
    def setSummary(self,t):
        self.summary = json.dumps(t)
    def getSummary(self):
        return json.loads(self.summary)
    def getText(self):
        return self.text
    def __str__(self):
        return self.name
