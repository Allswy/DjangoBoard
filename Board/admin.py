# from django.contrib import admin
#
# # Register your models here.
# from .models import Board
#
# admin.site.register(Board)

# Board/admin.py
from django.contrib import admin
from .models import Board


# 1. 定义自定义的 ModelAdmin 类
class BoardAdmin(admin.ModelAdmin):
    # ----------------------------------------------------
    # list_display: 控制在列表页（变更列表页）显示的字段
    # ----------------------------------------------------
    list_display = (
        'title',
        'content',
        'created_time',
        'updated_time'  # 现在它们将显示在列表页
    )

    # ----------------------------------------------------
    # readonly_fields: 让这些字段在编辑页只读 (推荐)
    # ----------------------------------------------------
    readonly_fields = (
        'created_time',
        'updated_time'
    )

    # ----------------------------------------------------
    # fields: 控制在编辑页（添加/修改页）显示的字段的顺序和内容
    # ----------------------------------------------------
    fields = (
        'title',
        'content',
        'created_time',
        'updated_time'
    )


# 2. 注册模型时，传入自定义的 Admin 类
admin.site.register(Board, BoardAdmin)