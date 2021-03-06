

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Article")
    title = models.CharField(max_length = 50,verbose_name = "Title")
    content = RichTextField()
    content_with_uploadImage = RichTextUploadingField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Created At")
    article_image = models.FileField(blank = True,null = True,verbose_name="Article Image")
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)        

    class Meta:
        ordering = ['-created_date']
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name ="Commet",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "Author")
    comment_content = models.CharField(max_length = 200,verbose_name = "Comment_Content")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']