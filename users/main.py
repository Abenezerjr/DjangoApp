from  .models import Profile
import  uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save , post_delete
from django.dispatch import receiver


# @receiver(post_save,sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    """
    :param sender: the model that send the data what model send that data
    :param instance: the instance of that actully triggerd this object
    :param created: it give boolin value true or fales true if the post or a model request add in the database fales other wise
    :return:
    """
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )
        print("it created")

def UpdateUser(sender, instance,created,**kwargs,):
    profile=instance
    user=profile.user

    if created == 'False':
        user.first_name=profile.name
        user.username=profile.username
        user.email=profile.email
        user.save()





def deletUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass


post_save.connect(createProfile, sender=User)
post_save.connect(UpdateUser, sender=Profile)
post_delete.connect(deletUser, sender=Profile)
