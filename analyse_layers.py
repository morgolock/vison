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
import json
from configparser import *
import argparse 
import numpy as np
import pprint
from difflib import Differ
from difflib import SequenceMatcher
 
def parse_layers(filename):
    layers = {} 
    try:
        with open(filename, 'r') as in_file1:
            Lines = in_file1.readlines()
            json_str = '' 
            finished = False
            ln_i = 0
            while ln_i < len(Lines):
                line = Lines[ln_i]
                ln_i +=1
                if line.startswith('{'):
                    json_str+=line
                    jdict = json.loads(line)
                    #print (jdict['layerName'])
                    layers[jdict['layerName']] = jdict
        return layers  
    except IOError:
        print("Could not read file:", jfilename)
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog = 'ArmNN profiler analyser',
                    description = 'This program compares data',
                    epilog = 'Text at the bottom of help')

    parser.add_argument("-j", "--jfile", dest="jfile", default="", help="JSON file to be analysed", metavar="JSON_FILE")
    parser.add_argument("-w", "--wfile", dest="wfile", default="", help="JSON file to be analysed", metavar="JSON_FILE2")
    parser.add_argument("-d", "--dumpdata", dest="dumpdata", default=False, help="dumpdata")
    parser.add_argument("-n", "--layername", dest="layername", default="", help="layername")
    parser.add_argument("-l", "--listlayers",default=False, help="Prints all layers in jfile", action="store_true")
 
    args = parser.parse_args()
    config = ConfigParser()
    jfilename = args.jfile
    wfilename = args.wfile

    layers1 = parse_layers(jfilename)
    assert not layers1 is None 
    if args.listlayers:
        print(f"Listing layers in {jfilename}")
        for k,d in layers1.items():
            print(f"{k}\n", end = "" )
    else:
        layers2 = parse_layers(wfilename)
        assert not layers2 is None 
        pp = pprint.PrettyPrinter(indent=4,compact=True)
        if len(args.layername) == 0:
            for k,d in layers1.items():
                assert k in layers2
                assert layers2[k]['shape'] == d['shape']
                data1 = d['data']
                data2 = layers2[k]['data']
                flat_array1 = np.array(data1).flat
                flat_array2 = np.array(data2).flat
            
                print(f"Analysing {k}... ", end = "" )
                if not np.allclose(flat_array1,flat_array2) :
                    pp.pprint(f"MISMATCHES....!")
                    flat_list1 = list(flat_array1)
                    flat_list2 = list(flat_array2)
                    lst1 = [str(x) for x in flat_list1]
                    lst2 = [str(x) for x in flat_list2]
                    print(f"    Computing score for {k}... Shape: {d['shape']}")
                    sim = SequenceMatcher(a=lst1, b=lst2)
                    score = sim.ratio()
                    print(f"    SCORE: {score} for {k}" )
                    if args.dumpdata:
                        np.set_printargs(threshold=np.inf)
                        #pp.pprint(np.column_stack((flat_array1, flat_array2)))
                        result = np.subtract(np.array(data1), np.array(data2))
                        pp.pprint (result)
                else:
                    print("OKAY....!")
        else:
            assert args.layername in layers1
            assert args.layername in layers2
            assert layers2[args.layername]['shape'] == layers1[args.layername]['shape']
            data1 = layers1[args.layername]['data']
            data2 = layers2[args.layername]['data']
            flat_array1 = np.array(data1).flat
            flat_array2 = np.array(data2).flat
            print(f"Analysing {args.layername}... ", end = "" )
            if not np.allclose(flat_array1,flat_array2,1e-08, 1e-10) :
                pp.pprint(f"MISMATCHES....!")
                flat_list1 = list(flat_array1)
                flat_list2 = list(flat_array2)
                lst1 = [str(x) for x in flat_list1]
                lst2 = [str(x) for x in flat_list2]
                print(f"    Computing score for {args.layername}... Shape: {layers1[args.layername]['shape']}")
                sim = SequenceMatcher(a=lst1, b=lst2)
                score = sim.ratio()
                print(f"    SCORE: {score} for {args.layername}" )
                if args.dumpdata:
                    np.set_printargs(threshold=np.inf)
                    np.set_printargs(precision=6)
                    result = np.subtract(np.array(data1), np.array(data2))
                    result = result[ result != 0]
                    pp.pprint (result)
            else:
                print("OKAY....!")
        

