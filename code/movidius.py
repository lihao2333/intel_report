path_to_networks = './'
path_to_images = '../../data/images/'
graph_filename = 'graph'
image_filename = path_to_images + 'nps_electric_guitar.png'

#mvnc.global_set_option(mvnc.GlobalOption.RW_LOG_LEVEL, 2)
devices = mvnc.enumerate_devices()
if len(devices) == 0:
    print('No devices found')
    quit()

device = mvnc.Device(devices[0])
device.open()

#Load graph
with open(path_to_networks + graph_filename, mode='rb') as f:
    graphFileBuff = f.read()

#Load preprocessing data
mean = 128
std = 1/128

#Load categories
categories = []
with open(path_to_networks + 'categories.txt', 'r') as f:
    for line in f:
        cat = line.split('\n')[0]
        if cat != 'classes':
            categories.append(cat)
    f.close()
    print('Number of categories:', len(categories))

#Load image size
with open(path_to_networks + 'inputsize.txt', 'r') as f:
    reqsize = int(f.readline().split('\n')[0])

graph = mvnc.Graph('graph')
fifoIn, fifoOut = graph.allocate_with_fifos(device, graphFileBuff)

img = cv2.imread(image_filename).astype(numpy.float32)

dx,dy,dz= img.shape
delta=float(abs(dy-dx))
if dx > dy: #crop the x dimension
    img=img[int(0.5*delta):dx-int(0.5*delta),0:dy]
else:
    img=img[0:dx,int(0.5*delta):dy-int(0.5*delta)]

img = cv2.resize(img, (reqsize, reqsize))

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

for i in range(3):
    img[:,:,i] = (img[:,:,i] - mean) * std

print('Start download to NCS...')
graph.queue_inference_with_fifo_elem(fifoIn, fifoOut, img, 'user object')
output, userobj = fifoOut.read_elem()

top_inds = output.argsort()[::-1][:5]

print(''.join(['*' for i in range(79)]))
print('inception-v1 on NCS')
print(''.join(['*' for i in range(79)]))
for i in range(5):
    print(top_inds[i], categories[top_inds[i]], output[top_inds[i]])

print(''.join(['*' for i in range(79)]))
fifoIn.destroy()
fifoOut.destroy()
graph.destroy()
device.close()
print('Finished')
~                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
~                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
~                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
~                                        
