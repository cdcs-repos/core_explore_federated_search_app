""" Url router for the administration site
"""
from django.contrib import admin
from django.conf.urls import url
from views.admin import views as admin_views, ajax as admin_ajax

admin_urls = [
    url(r'^repositories/add', admin_views.add_repository,
        name='core_explore_federated_search_app_repositories_add'),
    url(r'^repositories/delete', admin_ajax.delete_repository,
        name='core_explore_federated_search_app_repositories_delete'),
    url(r'^repositories/edit', admin_ajax.edit_repository,
        name='core_explore_federated_search_app_repositories_edit'),
    url(r'^repositories/refresh', admin_ajax.refresh_repository,
        name='core_explore_federated_search_app_repositories_refresh'),
    url(r'^repositories', admin_views.manage_repositories,
        name='core_explore_federated_search_app_repositories'),
]

urls = admin.site.get_urls()
admin.site.get_urls = lambda: admin_urls + urls
