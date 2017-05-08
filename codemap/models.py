from django.db import models


class MemoryMapKey(models.Model):
    name = models.CharField(verbose_name='字母编码', max_length=30)
    frequency = models.IntegerField(verbose_name='出现次数', default=0)

    def __str__(self):
        return self.name


class SignificantValue(models.Model):
    RELATED_TYPE_CHOICE = (
        ('acronym', '拼写缩写'),
        ('comics', '动漫'),
        ('game', '游戏'),
        ('Internet', '网络用语'),
        ('dialect', '方言俗语'),
        ('personal', '个人专用'),
    )

    key = models.ForeignKey(MemoryMapKey)
    content = models.CharField(verbose_name='联想词汇', max_length=128)
    remark = models.CharField(verbose_name='描述', max_length=512)
    related_type = models.CharField(verbose_name='联想类型', max_length=30,
                                    choices=RELATED_TYPE_CHOICE, default='acronym')
    images = models.CharField(max_length=512, null=True, blank=True)
    supported =  models.IntegerField(verbose_name='支持人数', default=0)

    def __str__(self):
        return self.content + '-' + self.key.name
