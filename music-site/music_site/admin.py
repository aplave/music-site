# from django.contrib import admin
# from polls.models import Choice, Poll
# from Profile.models import Profile
# from Profile.admin import ProfileAdmin

# class ChoiceInline(admin.TabularinLine):
#     model = Choice
#     extra = 3

# class PollAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#     list_filter = ['pub_date']
#     search_fields = ['question']
#     date_hierarchy = 'pub_date'

# admin.site.register(Poll, PollAdmin)
# # admin.site.register(Profile, ProfileAdmin)