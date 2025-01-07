from django.urls import path

from . import views

app_name = "polls"

'''urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.vote, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]'''

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
# DetailView expects the primary key value captured from the URL to be called "pk"
# class-based views have an as_view() class method
# advantages of class-based views: can be reused and extended by other views, can be customized by overriding attributes and methods