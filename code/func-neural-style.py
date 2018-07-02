def gen_video(content,style):
    cmd="cd neural-style_diy;th main.lua\
            -content_image {0} \
            -style_image {1}".format(content,style)
    os.system(cmd)
def gen_video2(dirname):
    cmd="cd {0};pwd;ffmpeg -y -r 10 -i res_%04d.png  output.mp4; ".format(dirname)
    os.system(cmd)

