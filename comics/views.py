from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import NameForm
from .external import Marvel

def index(request):
    template = loader.get_template('comics/index.html')
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))

def search(request):
    template = loader.get_template('comics/list.html')
    char_name = request.POST.get('char_name', '')
    list_char = Marvel().get_characteres(char_name)
    context = {
        'char_name' : char_name,
        'list_char' : list_char.json()
    }
    return HttpResponse(template.render(context, request))

def character(request, char_id):
    template = loader.get_template('comics/char.html')
    char = Marvel().get_id(char_id)
    context = {
        'char' : char.json()
    }
    return HttpResponse(template.render(context, request))

def story(request, story_id):
    template = loader.get_template('comics/story.html')
    story = Marvel().get_story(story_id).json()
    # print(story['data']['results'][0]['characters'])
    # TODO GET ID to return the pictures
    for char in story['data']['results'][0]['characters']['items']:
        print(char)
    context = {
        'story' : story
    }
    return HttpResponse(template.render(context, request))
