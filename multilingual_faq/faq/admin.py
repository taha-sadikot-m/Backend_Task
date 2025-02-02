from django.contrib import admin
from .models import FAQ
from ckeditor.widgets import CKEditorWidget
from django import forms

class FAQAdminForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorWidget())
    answer_hi = forms.CharField(widget=CKEditorWidget(), required=False)
    answer_bn = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = FAQ
        fields = '__all__'

class FAQAdmin(admin.ModelAdmin):
    form = FAQAdminForm
    list_display = ('question', 'question_hi', 'question_bn')  # Show translated questions

admin.site.register(FAQ, FAQAdmin)
