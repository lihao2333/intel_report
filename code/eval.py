    with tf.Graph().as_default():
        with tf.Session().as_default() as sess:
            # Read image data.
            ...
            # Add batch dimension
            ...
            # Remove batch dimension
            ...
            # Restore model variables.
            saver = tf.train.Saver(tf.global_variables(), write_version=tf.train.SaverDef.V1)
            sess.run([tf.global_variables_initializer(), tf.local_variables_initializer()])
            # Use absolute path
            FLAGS.model_file = os.path.abspath(FLAGS.model_file)
            saver.restore(sess, FLAGS.model_file)

            # Make sure 'generated' directory exists.
#            generated_file = 'generated/res.jpg'
            generated_file = FLAGS.image_file.replace("content","res")
            if os.path.exists('generated') is False:
                os.makedirs('generated')

            # Generate and write image data to file.
            with open(generated_file, 'wb') as img:
                img.write(sess.run(tf.image.encode_jpeg(generated)))
            tf.train.export_meta_graph(filename='model.meta',as_text=True)
