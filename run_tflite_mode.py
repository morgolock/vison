"""
MIT License

Copyright (c) 2022 Pablo Marquez Tello

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from configparser import *
from optparse import OptionParser        
import numpy as np
import tensorflow as tf


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-m", "--model", dest="model", default="", help="model", metavar="MODEL_FILE")
    parser.add_option("-w", "--wfile", dest="wfile", default="", help="JSON file to be analysed", metavar="JSON_FILE2")
    parser.add_option("-d", "--dumpdata", dest="dumpdata", default=False, help="dumpdata")
    parser.add_option("-n", "--layername", dest="layername", default="", help="layername")
    parser.add_option("-l", "--listlayers", dest="listlayers", default=False, help="layername")

    (options, args) = parser.parse_args()
    config = ConfigParser()
    print(options.model) 
    # Location of tflite model file
    if len(options.model) < 1:
        print("Use option --model to specify the path to the tflite file")
        exit()

    model_path = options.model

    # Load TFLite model and allocate tensors.
    interpreter = tf.lite.Interpreter(model_path=model_path)

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Allocate tensors
    interpreter.allocate_tensors()

    print(input_details)
    print(output_details)

    rand2 = np.random.random( input_details[0]['shape'] )
    rand2.flatten().tofile('tf_input.csv',sep=' ',format='%3.4f')
    input_data = np.array(rand2, dtype=np.float32)

    # Create input tensor out of raw features
    interpreter.set_tensor(input_details[0]['index'],input_data )

    # Run inference
    interpreter.invoke()

    # output_details[0]['index'] = the index which provides the input
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Print the results of inference
    print("Inference output is {}".format(output_data))
    output_data.tofile('tf_output.csv',sep=' ',format='%1.0f')



