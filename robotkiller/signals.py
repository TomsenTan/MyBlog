from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from django.dispatch import receiver
from robotkiller.models import Robotkiller
import printlog


@receiver(pre_save, sender=Robotkiller)
def PRSVHandler(sender, **kwargs):
    printlog.info('Robot start caculate %s'%Robotkiller.rbip)

@receiver(post_save, sender=Robotkiller)
def SVHandler(sender, **kwargs):
    printlog.info('Robot add one %s'%Robotkiller.rbip)

@receiver(pre_delete, sender=Robotkiller)
def PRDELHandler(sender, **kwargs):
    pass

@receiver(post_delete, sender=Robotkiller)
def DELHandler(sender, **kwargs):
    pass