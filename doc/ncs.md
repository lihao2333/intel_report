顶层通信代码主要包含以下几点：

1. 寻找ncs设备：

   ```python
   # ---- Step 1: Open the enumerated device and get a handle to it -------------
   
   mvnc.global_set_option(mvnc.GlobalOption.RW_LOG_LEVEL, 2)
   # Look for enumerated NCS device(s); quit program if none found.
   devices = mvnc.enumerate_devices()
   if len(devices) == 0:
       print("No devices found")
       quit()
   
   # Get a handle to the first enumerated device and open it
   device = mvnc.Device(devices[0])
   device.open()
   ```

2. 将之前转换好的graph文件导入到ncs设备中，为接下来的神经网络运行做好准备：

   ```python
   # ---- Step 2: Load a graph file onto the NCS device -------------------------
   
   # Read the graph file into a buffer
   with open(GRAPH_PATH, mode='rb') as f:
       blob = f.read()
   
   # Load the graph buffer into the NCS
   graph = mvnc.Graph("graph1")
   
   fifoIn, fifoOut = graph.allocate_with_fifos(
       device, blob, input_fifo_num_elem=2)
   ```

3. 处理图片，将输入的图片处理成tensorflow需要的格式：

   ```python
   # ---- Step 3: Pre-process the images ----------------------------------------
   
   # Resize image [Image size is defined during training]
   
   img_c = print_img = skimage.io.imread(CONTENT_PATH)
   img_c = skimage.transform.resize(img_c, IMAGE_DIM, preserve_range=True)
   # Convert RGB to BGR [skimage reads image in RGB, some networks may need BGR]
   ...
   
   # Mean subtraction & scaling [A common technique used to center the data]
   img_c = img_c.astype(numpy.float32)
   ```

4. 将处理好的图片发送到ncs中，获取输出的结果

   ```python
   # ---- Step 4: Read & print inference results from the NCS -------------------
   
   # The first inference takes an additional ~20ms due to memory
   # initializations, so we make a 'dummy forward pass'.
   
   graph.queue_inference_with_fifo_elem(fifoIn, fifoOut, img_c, '-c')
   
   output, userobj = fifoOut.read_elem()
   #handle the result
   ...
   ```

   