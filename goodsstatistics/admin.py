from django.contrib import admin

# Register your models here.
from goodsstatistics.models import ArrivalPlan


class ArrivalPlanForm(admin.ModelAdmin):
    search_fields = ('id', 'cabinet', 'sku','productName')
    list_display = ('id', 'cabinet', 'sku', 'productName','orderInfo')
    # list_display_links = ('id', 'name',)
    list_filter = ('sku', 'productName')
    list_per_page = 20
    ordering = ('id',)
    list_display_links =  ('id', 'cabinet', 'sku','productName')
    # fieldsets = ((
    # '项目',
    # {
    # 'fields': ('name', 'version', 'type', 'description', 'status', 'user')
    #
    # }
    # ),
    # )
    class Meta:
        model =  ArrivalPlan
        fields = '__all__'

admin.site.register( ArrivalPlan, ArrivalPlanForm)