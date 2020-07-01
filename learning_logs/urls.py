"""Defines urls for learning_logs"""

from django.urls import path
from . import views as ll_views

app_name = 'learning_logs'
urlpatterns = [
    # Homepage
    path('', ll_views.index, name='index'),
    # page that shows all topics
    path('topics', ll_views.topics, name='topics'),
    # detail page for a single topic
    path('topics/<int:topic_id>/', ll_views.topic, name='topic'),
    # page for adding new topic
    path('new_topics/', ll_views.new_topic, name='new_topic'),
    # page for adding new_entry
    path('new_entry/<int:topic_id>', ll_views.new_entry, name='new_entry'),
     # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', ll_views.edit_entry, name='edit_entry'),
]