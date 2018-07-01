   # ---- Step 3: Pre-process the images ----------------------------------------
   
   # Resize image [Image size is defined during training]
   
   img_c = print_img = skimage.io.imread(CONTENT_PATH)
   img_c = skimage.transform.resize(img_c, IMAGE_DIM, preserve_range=True)
   # Convert RGB to BGR [skimage reads image in RGB, some networks may need BGR]
   ...
   
   # Mean subtraction & scaling [A common technique used to center the data]
   img_c = img_c.astype(numpy.float32)
