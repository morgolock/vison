"""
MIT License

Copyright (c) 2021 Pablo Marquez Tello

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
from optparse import OptionParser        
import matplotlib.pyplot as plt
import matplotlib.colors as clrs
import matplotlib.patches as mpatches
import random
import numpy as np

def get_rnd_colors(count):
	color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(count)]
	print(color)
	return color

def plot_chart(time_per_kernel,total_time):
    # Fixing random state for reproducibility
    np.random.seed(19680801)
    plt.rcdefaults()
    fig, ax = plt.subplots()
    # Example data
    labels = tuple(list(time_per_kernel.keys()))
    y_pos = np.arange(len(labels))
    error = np.random.rand(len(labels))
    colors = get_rnd_colors(len(labels))
    ax.barh(y_pos, time_per_kernel.values(), xerr=error, align='center',color=colors)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel(unit)
    ax.set_title('How fast do you want to go today?')
    patches = list()
    k=0
    for l in labels:
        per_str = format(format(((time_per_kernel[l]/total_time)*100.0), '.4f'),'<5')
        npatch = mpatches.Patch(color=colors[k], label=per_str + '%' + ' ' + l )
        k+=1
        patches.append(npatch)
    plt.legend(handles=patches)
    plt.show()

def convert_to_ms(in_time, in_unit):
    return in_time / 1000

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-j", "--jfile", dest="jfile", default="", help="JSON file to be analysed", metavar="JSON_FILE")
    parser.add_option("--image",dest="image", default=False, action="store_true",help="The script will generate an image summary")
    parser.add_option("-k", "--inferencekey", dest="ik", default="1", help="Inference key", metavar="IK")
 
    (options, args) = parser.parse_args()
    config = ConfigParser()
    jfilename = options.jfile
    ik = options.ik
    try:
        with open(jfilename, 'r') as in_file1:
            Lines = in_file1.readlines()
            count = 0
            found_first_line = False
            found_last_line  = False
           
            json_str = '' 
            finished = False
            ln_i = 0
            while not finished:
                line = Lines[ln_i]
                ln_i +=1
                if line[0] == '{':
                    found_first_line = True
                elif line[0] == '}':
                    found_last_line  = True
                    finished = True
                    json_str+=line
                if found_first_line and not found_last_line:
                    json_str+=line
                count+=1

            jdict = json.loads(json_str)
            unit = jdict['ArmNN']['inference_measurements_#{}'.format(ik)]['Wall clock time_#{}'.format(ik)]['unit']
            inference_time = jdict['ArmNN']['inference_measurements_#{}'.format(ik)]['Wall clock time_#{}'.format(ik)]['raw'][0]
            total_kernel_time= 0.0
            time_per_kernel = {}
            for key in jdict['ArmNN']['inference_measurements_#{}'.format(ik)]:
                 if 'Execute_#' in key:
                    for k in jdict['ArmNN']['inference_measurements_#{}'.format(ik)][key]:
                        x = k.find("#")
                        if x != -1 and not 'Wall' in k:
                            print(k)
                            workload =  jdict['ArmNN']['inference_measurements_#{}'.format(ik)][key][k]
                            for kernel in workload:
                                if 'OpenClKernelTimer' in kernel or 'NeonKernelTimer' in kernel:
                                    timer = float(workload[kernel]['raw'][0])
                                    total_kernel_time += timer
                                    #Drop the prefix of the string and keep the kernel name
                                    j = kernel.find(":")
                                    t = kernel.find("GWS")
                                    if t == -1:
                                        t = kernel.find("_#")
                                    kernel= kernel[j+1:t]
                                    if kernel in time_per_kernel:
                                        time_per_kernel[kernel] += timer
                                    else:
                                        time_per_kernel[kernel] = timer
                                    s = format(timer, '>12')
                                    print('\t',s,unit,'\t\t\t', kernel)
            print('\n\n')

            print(f"Inference time: {inference_time} {unit}")
            print(f"Total kernel time {format(total_kernel_time,'.4f')} {unit}")
            print(f'\nTotal time per kernel in {unit} \t\t\t\tPercentage of total time\t\tKernel name')
            for kernel, time in sorted(time_per_kernel.items(), key=lambda x: x[1]):
                perc = time/total_kernel_time
                fmt_time = format(time, '.4f')
                print(f"\t  {format(fmt_time, '>14')}   \t\t\t\t  {format(format(perc, '.4f'),'<5')}% \t\t\t\t {kernel}")

            if options.image:
                plot_chart(time_per_kernel,total_kernel_time)
          
    except IOError:
        print("Could not read file:", jfilename)


