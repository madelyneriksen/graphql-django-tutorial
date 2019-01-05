from django.db import models

class BlogPost(models.Model):
    """A blog post model."""
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.CharField(max_length=255)

    def __str__(self):
        """Return the title."""
        return self.title
