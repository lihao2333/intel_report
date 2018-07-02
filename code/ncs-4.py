   # ---- Step 4: Read & print inference results from the NCS -------------------
   
   # The first inference takes an additional ~20ms due to memory
   # initializations, so we make a 'dummy forward pass'.
   
   graph.queue_inference_with_fifo_elem(fifoIn, fifoOut, img_c, '-c')
   
   output, userobj = fifoOut.read_elem()
   #handle the result
   ...
