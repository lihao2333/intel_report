def gen_img(request):
    if request.method == 'POST':
        form = gallaryImgForm(request.POST, request.FILES)
        if form.is_valid():
            if 'content' in request.FILES:
                content = request.FILES['content']
                style = request.POST['style']
                s = gallaryImg(owner=request.user, content=content,style=style)
                s.save()
                func.gen_img(s.content.path,s.style)
                return HttpResponseRedirect("list_img")
        else :
                return render(request, "info.html",{"info":"choose content image first"})

    else :
        style_list = os.listdir(os.path.join(settings.WAY_IMAGE_ROOT,"models"))
        return render(request,"way_img/gen_img.html",{"style_list":style_list})
