from django.db import models

# Create your models here.
class word(models.Model):
	id = models.AutoField(primary_key=True)
	bod = models.TextField('藏文')
	han = models.TextField('漢語')
	category = models.PositiveSmallIntegerField('品詞', choices=[
		(1, '名詞'),
		(2, '代詞'),
		(3, '動詞'),
		(4, '形容詞'),
		(5, '副詞'),
		(6, '連詞'),
		(7, '助詞'),
		(8, '後綴'),
		(9, '小品詞'),
		(10, '語氣詞'),
		(11, '片語'),
		(12, '例句'),
	])
	transliteration = models.CharField('轉寫', max_length=50)
	pronunciation = models.CharField('實際發音', max_length=50)
	explanation = models.TextField('釋義', blank=True, null=True)
	create_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.bod)

	class Meta:
		verbose_name = "藏文詞條"
		verbose_name_plural = "藏文詞條"
