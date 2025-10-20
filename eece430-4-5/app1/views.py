from django.shortcuts import render, redirect, get_object_or_404
from .models import Video
from .forms import VideoForm

def list_videos(request):
    videos = Video.objects.all().order_by('MovieTitle')
    return render(request, 'app1/list_videos.html', {'videos': videos})

def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_videos')
    else:
        form = VideoForm()
    return render(request, 'app1/add_video.html', {'form': form})

def update_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('list_videos')
    else:
        form = VideoForm(instance=video)
    return render(request, 'app1/update_video.html', {'form': form, 'video': video})

def delete_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        video.delete()
        return redirect('list_videos')
    return render(request, 'app1/delete_video.html', {'video': video})
