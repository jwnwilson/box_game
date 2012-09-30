from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('boxGame.apps.game.views',
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^main$', 'main', name='main'),
    url(r'^gameover$', 'gameover', name='gameover'),
    url(r'^highscore$', 'highscore', name="highscore"),
    url(r'^newhighscore$', 'new_hs', name="new_hs"),
)
