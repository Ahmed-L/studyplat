from django.http import HttpResponse
from .models import Chapter, Subject
from django.shortcuts import render, redirect, get_list_or_404


# Create your views here.
def home(request):
    # chaps = get_chapters_from_subject("Biology")
    # context = {'chaps': chaps}
    return render(request, 'app_core/home.html')


def get_chapters_from_subject(subject_name):
    chap_list = []
    all_chapters = Chapter.objects.all()
    for chapters in all_chapters:
        if chapters.subject.name == subject_name:
            chap_list.append(chapters)

    return chap_list


def subject(request, name):
    context = {}
    obj_l = get_list_or_404(Subject, name=name)
    obj = obj_l[0]
    subject_name = obj.name
    chap_list = get_chapters_from_subject(subject_name)
    context = {'subject_name': subject_name, 'chapter_list': chap_list}
    # context = {'subject_name': subject_name}
    return render(request, 'app_core/subject_page.html', context)


def chapter(request, name):
    context = {}
    obj = get_list_or_404(Chapter, name=name)
    chapter_name = obj[0].name
    ch = get_list_or_404(Chapter, name=chapter_name)
    chapter_main = ch[0]
    context = {'chapter_name': chapter_name, 'chapter_num': chapter_main.chapter_num,
               'description': chapter_main.description,
               'chapter_video': chapter_main.video}

    return render(request, 'app_core/chapter.html', context)


def search(request):
    context = {}
    searched_name_list = {}
    if request.method == 'GET':
        searched_string = request.GET['search']
        obj_list = Chapter.objects.filter(name__icontains=searched_string)
        context = {'searched_name_list': obj_list}

    return render(request, 'app_core/search.html', context)
