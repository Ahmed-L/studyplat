from django.db import models

cat_choices = [('IGSE', 'IGCSE'), ('IAL', 'IAL')]


# Subject model class
class Subject(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    cat_choices = models.CharField(max_length=100, choices=cat_choices)
    chapters = 0
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    # def add_chapter(self, chapter_name):
    #    self.chapterList.append(chapter_name)


# chapters model class
class Chapter(models.Model):
    # chapter_number = models.CharField(max_length=20, default="1")
    name = models.CharField(max_length=100, primary_key=True)
    description = models.CharField(max_length=1000, blank=True)
    video = models.CharField(max_length=300, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    chapter_num = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #    created = not self.pk
    #    super().save(*args, **kwargs)
    #    if created:
    #        self.subject
