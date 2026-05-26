from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    # Список проектов
    path('list/', views.ProjectListView.as_view(), name='project_list'),
    
    # Избранные проекты
    path('favorites/', views.FavoriteProjectsView.as_view(), name='favorite_projects'),
    
    # Создание и редактирование проекта
    path('create-project/', views.ProjectCreateView.as_view(), name='project_create'),
    path('<int:project_id>/edit/', views.ProjectEditView.as_view(), name='project_edit'),
    
    # Детали проекта
    path('<int:project_id>/', views.ProjectDetailView.as_view(), name='project_detail'),
    
    # API для навыков проекта
    path('api/skills/<int:project_id>/', views.SkillAPIView.as_view(), name='skill_api'),
    
    # Участие в проекте
    path('api/participate/<int:project_id>/', views.ParticipateView.as_view(), name='participate'),
    
    # Завершение проекта
    path('api/complete/<int:project_id>/', views.CompleteProjectView.as_view(), name='complete_project'),
    
    # Избранное
    path('api/favorite/<int:project_id>/', views.ToggleFavoriteView.as_view(), name='toggle_favorite'),
]
