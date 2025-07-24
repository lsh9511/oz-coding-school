from django.shortcuts import render, get_object_or_404
from bookmark.models import Bookmark
from django.http import Http404

def bookmark_list(request):
    bookmarks = Bookmark.objects.filter(id__gte=50)
    # all() = SELECT * FROM Bookmark
    # filter() 괄호안의 값은 WHERE문으로 쓰임 = SELECT * FROM bookmark  [] 리스트로 값을 불러옴
    # get() = SELECT * FROM bookmark WHERE id=id LIMIT 1  1개의 값만 나옴

    context = {'bookmarks':bookmarks}
    return render(request, 'bookmark_list.html', context)

def bookmark_detail(request, pk):
    # try:
    #     bookmark = Bookmark.objects.get(pk=pk)
    # except:
    #     raise Http404
    bookmark = get_object_or_404(Bookmark, pk=pk)

    context = {'bookmark':bookmark}
    return render(request, 'bookmark_detail.html', context)
