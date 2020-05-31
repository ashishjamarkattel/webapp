from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.db.models.signals import post_save,post_delete



class user_profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    images = models.ImageField(default='img1.jpg',upload_to='prof_pic')
    relation = models.TextField(max_length=100,blank=False,null=True)
    phone_no = models.IntegerField(default=000)

    def __str__(self):
        return self.user.username


def pre_save_profile(sender,**kwargs):
    print(kwargs)
    if kwargs["created"]:
        user_created = user_profile.objects.create(user=kwargs['instance'])




class profile_text(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=100)
    user_likes = models.ManyToManyField('profile_text',related_name='likes_of_users')

    def __str__(self):
        return self.user.username

def user_delete(sender,**kwargs):
    print('delete')
    user = User.objects.get(user=kwargs['instance'])
    user.delete()




class friends(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     all_users = models.ManyToManyField(User,related_name='users')

     def __str__(self):
         return self.user.username












