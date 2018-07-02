   # ---- Step 2: Load a graph file onto the NCS device -------------------------
   
   # Read the graph file into a buffer
   with open(GRAPH_PATH, mode='rb') as f:
       blob = f.read()
   
   # Load the graph buffer into the NCS
   graph = mvnc.Graph("graph1")
   
   fifoIn, fifoOut = graph.allocate_with_fifos(
       device, blob, input_fifo_num_elem=2)
