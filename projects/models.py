from django.db import models

# Create your models here.

'''
    1. Create a project model
    2. Add the "projects" app to the settings
    3. Create a migration
    4. Migrate
    5. Add to the admin
'''


class Project(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    pub_date = models.DateField()
    tools = models.CharField(max_length=200)
    summary = models.CharField(max_length=250)
    details = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
