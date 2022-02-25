from django_request_mapping import UrlPattern

from web.views import MyView
from web.views_article import ArticleView
from web.views_guest import GuestView

urlpatterns = UrlPattern();
urlpatterns.register(MyView);
urlpatterns.register(GuestView);
urlpatterns.register(ArticleView);