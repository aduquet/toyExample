import random
import time 
#this fuzzer function was taken from fuzzingbook.org
#A string of up to max_length characters in the range [char_start, char_start + char_range)
def fuzzer(max_length, char_start, char_range) -> str:
    
    string_length = random.randrange(0, max_length + 1)

    out = ""
    for i in range(0, string_length):
        out += chr(random.randrange(char_start, char_start + char_range))
    return out
    
def saveArraysInputs(numb, fileName):
    
    with open(fileName, "a") as f:
        f.write(numb + '\n')

start_time = time.time()
end_time = 0
while end_time <= 5 :
    
    out = fuzzer(20, ord('0'), 10)
    out2 = saveArraysInputs(out)
    print(out2)
    print(out)
    end_time = time.time() - start_time
    print(end_time)
    
#print(random.randrange(0,100))