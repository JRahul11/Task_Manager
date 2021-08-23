from django.contrib import admin
from django.urls import path
from auth_app.views import user_login, user_signup, user_logout, user_np
from task_app.views import home, newtask, history, deletetask, complete, sortnew, sortpriority, updatetask

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path("login/", user_login, name="user_login"),
    path("signup/", user_signup, name="user_signup"),
    path("logout/", user_logout, name="user_logout"),
    path("forgotpassword/", user_np, name="user_np"),

    # Main Project
    path("", home, name="home"),
    path("newestfirst", sortnew, name="sortnew"),
    path("sortbypriority", sortpriority, name="sortpriority"),
    path("newtask/", newtask, name="newtask"),
    path("history/", history, name="history"),
    path("deletetask/<task_id>", deletetask, name="deletetask"),
    path("complete/<task_id>", complete, name="complete"),
    path("updatetask/<task_id>", updatetask, name="updatetask"),
]
