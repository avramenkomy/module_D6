from django import forms
from p_lib.models import Book

class BookForm(forms.ModelForm):
    ISBN = forms.CharField(label='ISBN', widget=forms.TextInput)
    title = forms.CharField(widget=forms.TextInput, label='Название книги')
    description = forms.CharField(widget=forms.TextInput, label='Описание книги')
    publisher = forms.ChoiceField
    year_release = forms.IntegerField(label='Год издания')
    author = forms.ChoiceField
    copy_count = forms.IntegerField(label='Кол-во копий')
    price = forms.DecimalField(label="Цена", decimal_places=2, max_digits=8)
    photo = forms.ImageField(label="Фото", required=False)
    small_photo = forms.ImageField(label="Маленькое фото", required=False)

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.__class__.__name__ == "ImageField":
                visible.field.widget.attrs['class'] = 'form-control-file'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Book
        fields = '__all__'
