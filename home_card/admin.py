from django.contrib import admin
from .models import home_card_1,home_card_2,home_card_3,home_card_4

# Register your models here.
class home_card_1Admin(admin.ModelAdmin):
    list_display= ("card_title", "card_author", "card_pdate", "card_desc","card_image","card_lng")
class home_card_2Admin(admin.ModelAdmin):
    list_display= ("card_title", "card_author", "card_pdate", "card_desc","card_image","card_lng")
class home_card_3Admin(admin.ModelAdmin):
    list_display= ("card_title", "card_author", "card_pdate", "card_desc","card_image","card_lng")
class home_card_4Admin(admin.ModelAdmin):
    list_display= ("card_title", "card_author", "card_pdate", "card_desc","card_image","card_lng") 

admin.site.register(home_card_1,home_card_1Admin)    
admin.site.register(home_card_2,home_card_1Admin)    
admin.site.register(home_card_3,home_card_1Admin)    
admin.site.register(home_card_4,home_card_1Admin)    
