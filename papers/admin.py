from django.contrib import admin
from papers.models import *

class NameInline(admin.TabularInline):
    model = Name
    extra = 0

class ResearcherAdmin(admin.ModelAdmin):
    fieldsets = [
      #  (None, {'fields': ['nae']}),
        ('Affiliation', {'fields': ['department', 'groups']})
        ]
    inlines = [NameInline]

class AuthorInline(admin.TabularInline):
    model = Author
    extra = 0
    raw_id_fields = ('paper','name')

class OaiInline(admin.TabularInline):
    model = OaiRecord
    extra = 0

class PublicationInline(admin.StackedInline):
    model = Publication
    extra = 0

class PaperAdmin(admin.ModelAdmin):
    fields = ['title', 'year']
    inlines = [AuthorInline, PublicationInline, OaiInline]

admin.site.register(Department)
admin.site.register(ResearchGroup)
admin.site.register(Researcher, ResearcherAdmin)
admin.site.register(Name)
admin.site.register(Paper, PaperAdmin)
admin.site.register(OaiSource)
admin.site.register(OaiRecord)
admin.site.register(Journal)
admin.site.register(Publisher)
