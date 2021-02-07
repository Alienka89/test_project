from django.contrib import admin

from .models import Page, Content, Text, Audio, Video, Photo


@admin.register(Photo)
class PhotoAdminInline(admin.ModelAdmin):
    pass


@admin.register(Text)
class TextAdminInline(admin.ModelAdmin):
    pass


@admin.register(Audio)
class AudioAdminInline(admin.ModelAdmin):
    pass


@admin.register(Video)
class VideoAdminInline(admin.ModelAdmin):
    pass


class ContentAdminInline(admin.TabularInline):
    readonly_fields = ('counter',)
    model = Content
    extra = 0
    min_num = 1


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    save_on_top = True
    preserve_filters = True
    show_full_result_count = True
    list_display = ('title', 'hide', 'counter')
    list_filter = ('hide',)
    search_fields = ('title', 'content__title',)
    readonly_fields = ('counter',)
    inlines = [ContentAdminInline]

    def delete_model(self, request, obj):
        obj.hide = True
        obj.save()
