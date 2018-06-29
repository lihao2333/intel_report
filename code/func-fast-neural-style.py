def gen_img(content,style):
    cmd="python3 fast-neural-style-tensorflow/eval.py\
            --image_file {0} \
            --model_file fast-neural-style-tensorflow/models/{1}".format(content,style)
