from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

def smart_truncate(content, length=180, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix

# вывод данных из БД
def post_list(request):
    notes = Post.objects.order_by('created_date')
    for note in notes:
        note.desc = smart_truncate(note.text)
    return render(request, "my_app/index.html", {"notes": notes})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'my_app/post_new.html', {'form': form})

# def make_a_note(request):
#     return render(request, "my_app/make_a_note.html", {})

# def create(request):
#     if request.method == "POST":
#         note = Post()
#         note.title = request.POST.get("title")
#         note.text = request.POST.get("text")
#         note.file = request.POST.get("file")
#         note.save()
#     return HttpResponseRedirect("/")
