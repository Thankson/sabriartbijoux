from django.contrib import admin

from sito.models import *
from image_cropping import ImageCroppingMixin


class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

class SliderAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "titolo", "active")

class ImmaginiAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "titolo")

def get_category(self):
    return self.categoria.all()

class PostAdmin(ImageCroppingMixin, admin.ModelAdmin):
    #duplicate function
    def duplicate_event(ModelAdmin, request, queryset):
        for object in queryset:
            object.id = None
            object.save()
    duplicate_event.short_description = "Duplica Record Selezionati"

    list_display = ("image_img", "titolo")
    actions = ['duplicate_event']



admin.site.register(Categorie, MyModelAdmin)
admin.site.register(Immagini, ImmaginiAdmin)
admin.site.register(Video, MyModelAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Box, MyModelAdmin)
admin.site.register(News, MyModelAdmin)
admin.site.register(Slider, ImmaginiAdmin)
admin.site.register(Page, MyModelAdmin)
admin.site.register(TipologiaEventi, MyModelAdmin)



