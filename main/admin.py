from django.contrib import admin
from main.models import Customer , Guide, Hike, EnrolledHikers, NewsLetter, Contact

admin.site.site_header = 'GUIDE DASHBOARD'

class hikes_admin(admin.ModelAdmin):
    # inlines = (what_you_learn_TubulurinLine, requirements_TublurinLine, Video_TubulurinLine)
    list_display = ["trail", "user_id"]

    def changelist_view(self, request, extra_context=None):
        queryset = self.get_queryset(request)

        if not queryset.exists():
            empty_message = "No courses found for the current user."
            context = {'empty_message': empty_message}
            return super().changelist_view(request, extra_context=context)

        return super().changelist_view(request, extra_context=extra_context)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset

        print(request.user)
        author_detail = Guide.objects.filter(username=request.user)[0]
        print(author_detail)
        queryset = queryset.filter(user_id=author_detail)

        if not queryset.exists():
            return queryset.none()

        return queryset




# Register your models here.
admin.site.register(Customer)
admin.site.register(Guide)
admin.site.register(Hike, hikes_admin)
admin.site.register(EnrolledHikers)
admin.site.register(NewsLetter)
admin.site.register(Contact)