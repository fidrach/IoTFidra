from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Album
from .models import Song

def index(request):
    all_albums = Album.objects.all()

    context = {
        "all_albums": all_albums,
    }

    return render(request, "music/index.html", context)


def detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)

    context = {
        "album": album,
    }

    return render(request, "music/detail.html", context)


def favorite(request, album_id):
    album = get_object_or_404(Album, id=album_id)

    context = {
        "album": album,
    }

    try:
        selected_song = album.song_set.get(id=request.POST["song"])
    except (KeyError, Song.DoesNotExist):
        context["error_message"] = "You did not select a valid song"
    else:
        selected_song.is_favorite = True
        selected_song.save()

    return render(request, "music/detail.html", context)
