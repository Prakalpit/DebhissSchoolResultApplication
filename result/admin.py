from django.contrib import admin
from .models import Result
from import_export.admin import ExportActionMixin
from import_export import resources

class ResultResources(resources.ModelResource):

    class Meta:
        model = Result
        fields = ('name', 'grade_class', 'gpa', 'password')

class ResultAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['name', 'grade_class', 'gpa', 'password']
    list_filter = ['grade_class', 'gpa']
    search_fields = ['name', 'grade_class']
    resource_class = ResultResources

admin.site.register(Result, ResultAdmin)
