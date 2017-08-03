from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import NameForm
from .external import Marvel

def index(request):
    template = loader.get_template('comics/base.html')
    context = {}
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            context, template = search(request)
    else:
        form = NameForm()
    context['form'] = form
    return HttpResponse(template.render(context, request))

def search(request):
    template = loader.get_template('comics/list_char.html')
    char_name = request.POST.get('char_name', '')
    list_char = Marvel().get_characteres(char_name)
    if list_char:
        context = {
            'char_name' : char_name,
            'list_char' : list_char
        }
    else:
        context = {}
    return context, template

def character(request, char_id):
    template = loader.get_template('comics/char.html')
    char, attribution_text = Marvel().get_id(char_id)
    char_comics = Marvel().get_id_comics(char_id)
    context = {
        'form' : NameForm(),
        'char_id' : char,
        'char_comics' : char_comics,
        'attr' : attribution_text
    }
    return HttpResponse(template.render(context, request))

def comic(request, comic_id):
    template = loader.get_template('comics/comics.html')
    comic, attribution_text = Marvel().get_comics(comic_id)
    comic_char = Marvel().get_comics_characters(comic_id)
    context = {
        'form' : NameForm(),
        'comic' : comic,
        'comic_char' : comic_char,
        'attr' : attribution_text
    }
    return HttpResponse(template.render(context, request))
