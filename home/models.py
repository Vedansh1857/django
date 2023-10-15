from django.db import models

# Create your models here.

# Models simply represent your database... So, let's create our model...
# This below class 'contact' is basically a table which will be get feed into the database.
# It is just lyk an excel sheet and these variables :- "name","email","date" etc. are just the columns of database.
# And the class name : "contact" is the name of the excel sheet.

class contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    # By this str method we can change the name of the entry to the name entered by the user in the form.
    def __str__(self):
        return self.name