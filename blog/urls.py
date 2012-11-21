from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Signal
from django.contrib.syndication.views import Feed

class BlogFeed(Feed):
    title = "MySite"
    description = "Random Text"
    link = "/blog/feed/"

    def items(self):
        return Signal.objects.all().order_by("-created")[:2]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.body
    def item_link(self, item):
        return u"/blog/%d" % item.id

urlpatterns = patterns('',
	url(r'^$',ListView.as_view(
			queryset=Signal.objects.all().order_by("-created")[:3],
			template_name="blog.html")),

	 url(r'^(?P<pk>\d+)$',DetailView.as_view(
			model=Signal,
			template_name="signal.html")),

	url(r'^archives/$', ListView.as_view(
                           queryset=Signal.objects.all().order_by("-created"),
                           template_name="archives.html")),
    	url(r'^feed/$', BlogFeed()),
)
