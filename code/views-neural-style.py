def gen_video(request):
    if request.method == 'POST':
        form = gallaryVideoForm(request.POST, request.FILES)
        if form.is_valid():
            if 'content' in request.FILES\
                    and 'style' in request.FILES:
                content = request.FILES['content']
                style = request.FILES['style']
                s = gallaryVideo(owner=request.user, content=content,style=style)
                s.save()
                func.gen_video(s.content.path,s.style.path)
                return HttpResponseRedirect("list_video")
        else :
                return render(request, "info.html",{"info":"choose content image first"})

    else :
        return render(request,"way_video/gen_video.html",{})
