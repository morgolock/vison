import json
from configparser import *
from optparse import OptionParser        

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-j", "--jfile", dest="jfile", default="", help="JSON file to be analysed", metavar="JSON_FILE")
    (options, args) = parser.parse_args()
    config = ConfigParser()
    jfilename = options.jfile
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
            unit = jdict['ArmNN']['inference_measurements_#1']['Wall clock time_#1']['unit']
            total_kernel_time= 0.0
            time_per_kernel = {}
            for key in jdict['ArmNN']['inference_measurements_#1']:
                 if 'Execute_#' in key:
                    for k in jdict['ArmNN']['inference_measurements_#1'][key]:
                        x = k.find("#")
                        if x != -1 and not 'Wall' in k:
                            print(k)
                            workload =  jdict['ArmNN']['inference_measurements_#1'][key][k]
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
        ##                        elif 'Wall clock time_' in v:
        ##                            print('\t', 'pa')                    
                            
            print('\n\n')
            print ('Inference time: ', jdict['ArmNN']['inference_measurements_#1']['Wall clock time_#1']['raw'][0],unit)
            print('Total kernel time ', total_kernel_time, unit)
            print('\nTotal time per kernel\t\t\t\tPercentage of total time\t\tKernel name')
            for kernel, time in sorted(time_per_kernel.items(), key=lambda x: x[1]):
                perc = time/total_kernel_time
                print('\t', format(format(time, '.4f'),'<20'),unit, '\t\t%', format(format(perc, '.8f'),'<5'),'\t\t\t', kernel )

           
    except IOError:
        print("Could not read file:", jfilename)


