from django.db import models

class Data(models.Model):
    type = ForeignKey(Type)
    title = models.CharField()
    body = models.CharField()

def render(self):
    rep = Rep.objects.filter(name=default, type=self.type)
    return render_to_template(rep.template, self)


class Type(models.Model):
    name = models.CharField()


class Rep(models.Model):
    template = ForeignKey(Template)
    type = ForeignKey(Type)
    name = models.CharField()
    slug = models.CharField()
    filter = models.CharField()
    limit = models.IntegerField()
    order_by = models.ChoiceField(['asc', 'desc'])


class DataRep(models.Model):
    rep = ForeignKey(Rep)
    data = ForeignKey(Data)


def dispatcher(slug):
    dr = DataRep.objects.filter(slug=slug)

    if dr.data_id:
        return data_view(dr)

    return rep_view(dr)

article_tpl = Template(name='article.tpl').save()
top5_article = Template(name='top5_article.tpl')

article_type = Type(name='article').save()

article1 = Data(type=article_type, title="first article", body="test body 1").save()
article2 = Data(type=article_type, title="second article", body="test body 2").save()

rep1 = Rep(type=article_type, template=tpl_article, name='default').save()

# /articles/how-to-win-friends
def data_view(dr):
    return render_to_template(dr.rep.template, dr.data)

# /featured/top5-articles
def rep_view(dr):
    data_list = Data.objects.filter(type=dr.type)

    data_list.order_by(dr.order_by)
    data_list.limit(dr.limit)
    data_list.filter(title.startswith=dr.filter)

    return render_to_template(dr.rep.template, data_list)

# top_articles.tpl
{% for data in data_list %}
    {% data.render %}
{% endfor %}
