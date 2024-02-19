from django.db import models

class Article(models.Model):

    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    # Generate the migration file which has no foreignKey
    # Add the app name if foreignKey is defined
    author = models.ForeignKey('channels.User', models.CASCADE, blank=True, null=True)
    # Use mapping to solve the confilct table name
    tags = models.ManyToManyField("Tag",db_table='article_tags')

    class Meta:
        db_table = 'article'

    def __str__(self):
        return "<Article:(title:%s,content:%s)>" % (self.title,self.content)


class Tag(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'tag'

class ArticleTag(models.Model):
    article = models.OneToOneField(Article, models.DO_NOTHING)
    tag = models.OneToOneField(Tag, models.DO_NOTHING)

    class Meta:
        db_table = 'article_tag'



