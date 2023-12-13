from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(label='Имя', required=True, max_length=150,
                           widget=forms.TextInput(attrs={'placeholder': 'Представьтесь', 'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea({'placeholder': 'Расскажите о Вашем опыте',
                                                     'class': 'form-control'}), label='Отзыв', required=True)





