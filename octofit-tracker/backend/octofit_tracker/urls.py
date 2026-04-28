"""
URL configuration for octofit_tracker project.
Backend API hosted at: https://jasontklr-skills-build-applications-w-copilot-agent-mode-8000.app.github.dev
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('octofit_tracker.api_urls')),
]
