from turtle import title
from django import forms

#from puzzlereader.home.models import Book

GENRES = (
    'Action', 'Classics', 'Comic', 'Mystery',
    'Fantasy', 'Historical Fiction',
    'Horror', 'Literary Fiction', 'Nonfiction',
)


class BookForm(forms.Form):
    class Meta:
        #model = Book
        fields = ('name', 'title', 'genre', 'bio', 'num_stars')


'''
    GENRES = (
        'Action', 'Classics', 'Comic', 'Mystery',
        'Fantasy', 'Historical Fiction',
        'Horror', 'Literary FIction', 'Nonfiction'
    )
    title = forms.CharField(label='Screen Name', required=True)
    #email = forms.EmailField(label='E-Mail')
    # extend array as needed
    genre = forms.Select(choices=GENRES, required=False)

    #subject = forms.CharField(required=False)
    # capture answers in body
    bio = forms.CharField(widget=forms.Textarea,
                          required=False, max_length=500)
    num_stars = forms.IntegerField(default=0)
    #image_field = forms.ImageField(required=False)
'''
