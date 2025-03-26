from django.db import models


'''
Define Post Class
'''
class Category(models.Model):
    name=models.CharField( max_length=50)





class Post(models.Model):
    '''
    Define Post Class
    '''
    title=models.CharField( max_length=255)
    content=models.CharField( max_length=50)
    author=models.CharField( max_length=50)
    status=models.BooleanField()
    category=models.ForeignKey("Category", on_delete=models.SET_NULL,null=True)
    image=models.ImageField(blank=True,null=True)
    createddate=models.DateTimeField( auto_now_add=True)
    updateddate=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField()


    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
