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
    
    # API для поиска навыков (автодополнение)
    path('skills/', views.SkillSearchView.as_view(), name='skill_search'),
    
    # API для добавления навыка к проекту
    path('<int:project_id>/skills/add/', views.SkillAddView.as_view(), name='skill_add'),
    
    # API для удаления навыка из проекта
    path('<int:project_id>/skills/<int:skill_id>/remove/', views.SkillRemoveView.as_view(), name='skill_remove'),
    
    # Участие в проекте
    path('api/participate/<int:project_id>/', views.ParticipateView.as_view(), name='participate'),

    # Завершение проекта
    path('api/complete/<int:project_id>/', views.CompleteProjectView.as_view(), name='complete_project'),
    
    # Избранное
    path('api/favorite/<int:project_id>/', views.ToggleFavoriteView.as_view(), name='toggle_favorite'),
]
