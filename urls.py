"""
URL configuration for QuestGame project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from chooseRole import views
from chooseRole.views import task1_view_id_3, task2_view_id_3, task3_view_id_3, check_answer_task_1_id_3, \
    code_page_task1, code_page_task2, check_answer_task_2_id_3, task1_view_id_4, check_answer_task_1_id_4, \
    code_page_task41, check_answer_task_2_id_4, task2_view_id_4, code_page_task42, task3_view_id_4, \
    check_answer_task_3_id_4, code_page_task43, task1_view_id_5, check_answer_task_1_id_5, code_page_task51, \
    task2_view_id_5, check_answer_task_2_id_5, task3_view_id_5, check_answer_task_3_id_5, code_page_task52, \
    code_page_task53, check_answer_task_1_id_1, code_page_task11, task1_view_id_1, task2_view_id_1, \
    check_answer_task_2_id_1, code_page_task12, check_answer_task_3_id_1, code_page_task13, task3_view_id_1, \
    task1_view_id_2, code_page_task21, task2_view_id_2, task3_view_id_2, code_page_task22, code_page_task23

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list_roles, name='list_roles'),


    path('roles/1/tasks/1/', task1_view_id_1, name='task11'),
    path('roles/1/tasks/2/', task2_view_id_1, name='task12'),
    path('roles/1/tasks/3/', task3_view_id_1, name='task13'),

    path('roles/2/tasks/1/', task1_view_id_2, name='task21'),
    path('roles/2/tasks/2/', task2_view_id_2, name='task22'),
    path('roles/2/tasks/3/', task3_view_id_2, name='task23'),

    path('roles/3/tasks/1/', task1_view_id_3, name='task31'),
    path('roles/3/tasks/2/', task2_view_id_3, name='task32'),
    path('roles/3/tasks/3/', task3_view_id_3, name='task33'),

    path('roles/4/tasks/1/', task1_view_id_4, name='task41'),
    path('roles/4/tasks/2/', task2_view_id_4, name='task42'),
    path('roles/4/tasks/3/', task3_view_id_4, name='task43'),

    path('roles/5/tasks/1/', task1_view_id_5, name='task51'),
    path('roles/5/tasks/2/', task2_view_id_5, name='task52'),
    path('roles/5/tasks/3/', task3_view_id_5, name='task53'),

    path('roles/1/tasks/1/check_answer/', check_answer_task_1_id_1, name='check_answer_task11'),
    path('roles/1/tasks/2/check_answer/', check_answer_task_2_id_1, name='check_answer_task12'),
    path('roles/1/tasks/3/check_answer/', check_answer_task_3_id_1, name='check_answer_task13'),

    path('roles/3/tasks/1/check_answer/', check_answer_task_1_id_3, name='check_answer'),
    path('roles/3/tasks/2/check_answer/', check_answer_task_2_id_3, name='check_answer_task2'),

    path('roles/4/tasks/1/check_answer/', check_answer_task_1_id_4, name='check_answer_task41'),
    path('roles/4/tasks/2/check_answer/', check_answer_task_2_id_4, name='check_answer_task42'),
    path('roles/4/tasks/3/check_answer/', check_answer_task_3_id_4, name='check_answer_task43'),

    path('roles/5/tasks/1/check_answer/', check_answer_task_1_id_5, name='check_answer_task51'),
    path('roles/5/tasks/2/check_answer/', check_answer_task_2_id_5, name='check_answer_task52'),
    path('roles/5/tasks/3/check_answer/', check_answer_task_3_id_5, name='check_answer_task53'),


    path('roles/1/code/', code_page_task11, name='code_page11'),
    path('roles/1/code2/', code_page_task12, name='code_page12'),
    path('roles/1/code3/', code_page_task13, name='code_page13'),

    path('roles/2/tasks/1/code/', code_page_task21, name='code_page21'),
    path('roles/2/tasks/2/code2/', code_page_task22, name='code_page22'),
    path('roles/2/tasks/3/code3/', code_page_task23, name='code_page23'),

    path('roles/3/code/', code_page_task1, name='code_page'),
    path('roles/3/code2/', code_page_task2, name='code_page2'),

    path('roles/4/code/', code_page_task41, name='code_page41'),
    path('roles/4/code2/', code_page_task42, name='code_page42'),
    path('roles/4/code3/', code_page_task43, name='code_page43'),

    path('roles/5/code1/', code_page_task51, name='code_page51'),
    path('roles/5/code2/', code_page_task52, name='code_page52'),
    path('roles/5/code3/', code_page_task53, name='code_page53'),

]
