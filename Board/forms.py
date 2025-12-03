# Board/forms.py
from django import forms
from .models import Board


class BoardForm(forms.ModelForm):
    # 内部 Meta 类用于将表单与模型关联
    class Meta:
        model = Board
        # 指定表单中包含的模型字段
        fields = ['title', 'content']

        # 可选：自定义字段的显示名称
        labels = {
            'title': '标题',
            'content': '内容',
        }

        # 可选：自定义小部件，例如将 content 字段显示为更大的文本区域
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }