from django.contrib import admin
from handlemoney.models import Project, Category, Expense

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'budget', 'total_transactions', 'budget_left')
    exclude      = ('slug',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('project_slug', 'name')
    def project_slug(self, obj):
        return obj.project.slug

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('project_slug', 'title', 'amount', 'category')

    def project_slug(self, obj):
        return obj.project.slug



admin.site.register(Project,   ProjectAdmin)
admin.site.register(Category,  CategoryAdmin)
admin.site.register(Expense,   ExpenseAdmin)
