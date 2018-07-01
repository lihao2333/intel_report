def list_img(request):
    model = gallaryImg.objects.get(owner=request.user) 
    print(model.style)
    content = {"content_url":model.content.url,
                "style_url":settings.MEDIA_URL+"img/%s"%model.style.replace("ckpt-done","jpg"),
                "res_url":model.content.url.replace('content','res')}
    return render(request,"way_img/list_img.html",content)
