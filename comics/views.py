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
    list_char = Marvel().get_characteres(char_name).json()
    context = {
        'char_name' : char_name,
        'list_char' : list_char['data']
    }
    return context, template

def character(request, char_id):
    template = loader.get_template('comics/char.html')
    char_json = Marvel().get_id(char_id).json()
    char_id_stories = Marvel().get_id_stories(char_id).json()
    char = char_json['data']['results'][0]
    char_stories = char_id_stories['data']['results']
    attribution_text = char_json['attributionText']
    form = NameForm()
    context = {
        'form' : form,
        'char_id' : char,
        'char_stories' : char_stories,
        'attr' : attribution_text
    }
    return HttpResponse(template.render(context, request))

def story(request, story_id):
    template = loader.get_template('comics/story.html')
    story_json = Marvel().get_story(story_id).json()
    storty_char_json = Marvel().get_story_characters(story_id).json()
    story = story_json['data']['results'][0]
    story_char = storty_char_json['data']['results']
    attribution_text = story_json['attributionText']
    context = {
        'story' : story,
        'story_char' : story_char,
        'attr' : attribution_text
    }
    return HttpResponse(template.render(context, request))
