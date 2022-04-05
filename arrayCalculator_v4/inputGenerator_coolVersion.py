import glob as gl
import pathlib
import random
import time
import os


#this fuzzer function was taken from fuzzingbook.org
#A string of up to max_length characters in the range [char_start, char_start + char_range)
def fuzzer(max_length, char_start, char_range) -> str:
    
    string_length = random.randrange(0, max_length + 1)

    out = ""
    for i in range(0, string_length):
        out += chr(random.randrange(char_start, char_start + char_range))
    return out
    
def saveArraysInputs(numb, fileNamePath):
    
    with open(fileNamePath, "a") as f:
        f.write(numb + '\n')

def conv(fuzzerOutput):
    aux = []
    for i in fuzzerOutput:
        aux.append(i)
    return aux
    
def start(t, file_name, paths):
    start_time = time.time()
    end_time = 0
    filenamePath = paths +'\\' + file_name
    while end_time <= int(t) :
        #fuzzerOutput = conv(fuzzer(20, ord('0'), 10))
        #saveArraysInputs(fuzzerOutput, filenamePath)
        saveArraysInputs(fuzzer(20, ord('0'), 10), filenamePath)
        end_time = time.time() - start_time
    
if __name__ == '__main__':
    import click
    
    @click.command()
    @click.option('-t', '--time', 'time_limit', help = 'time limit=[time in seconds]')
    @click.option('-o', '--output_name', 'file_out', help = 'File name')
    
    def main(time_limit, file_out):
        print('*** Executing ***')
        
        paths = str(pathlib.Path().absolute()) + '\\' + 'FuzzerInputs'
        
        if not os.path.exists(paths):
            os.mkdir('FuzzerInputs')

        start(time_limit, file_out, paths)
        print('*** Finished ***')
        print('Generated inputs are saved in ' + paths + '\\' + file_out )

main()
        