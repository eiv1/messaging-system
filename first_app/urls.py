from django.urls import include, path
from first_app import views

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('messages', views.messages), # get and post
    path('messages/<int:user_id>',views.show_all_messages_for_username), #get
    path('unreadMessages/<int:user_id>',views.show_unread_messages_for_username), #get
    path('readMessage/<int:message_id>',views.readMessage), #get
    path('delete_message/<int:message_id>/<int:user_id>',views.delete_message), #delete

    path('login', obtain_auth_token), #POST method, Login automatic, give unique token
    path('messagesAll', views.messagesAll.as_view()), # get and post
    path('unreadM',views.unreadMessage.as_view()), # get
    path('messageOne/<int:message_id>', views.messageOne.as_view()), # get and delete
]