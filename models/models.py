from django.db import models

# from django.db import models

from brands.models import Brand



class Model(models.Model):
    name = models.ForeignKey(Brand,on_delete=models.CASCADE, null=True)
    engine = models.TextField(verbose_name="Двигатель", null=True)
    hp = models.IntegerField( verbose_name="Лошадиные силы", null=True)
    nm = models.IntegerField(verbose_name="Ньютон метр", null=True)
    image = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="+",null=True)
    series = models.TextField( null=True)


    def __str__(self):
        return str(self.name)



class AddBrand(models.Model):

    name = models.CharField(max_length=200, verbose_name="Название")
    engine = models.TextField(verbose_name="Двигатель")
    hp = models.CharField(max_length=200, verbose_name="Лошадиные силы")
    nm = models.CharField(max_length=200, verbose_name="Ньютон метр")
    image = models.ImageField(upload_to="media/",blank=True, null=True)
    series = models.CharField(max_length=200)
    comments = models.TextField(max_length=200,verbose_name="Комментарии", null=True)

    def __str__(self):
        return str(self.name)


class ModelComment(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=500)
    models = models.ForeignKey(Model,
                              on_delete=models.CASCADE,related_name="model_comment")


    def __str__(self):
        return self.models.name
