import random

#this fuzzer function was taken from fuzzingbook.org
#A string of up to max_length characters in the range [char_start, char_start + char_range)
def fuzzer(max_length, char_start, char_range) -> str:
    
    string_length = random.randrange(0, max_length + 1)
    # print(string_length)
    out = ""
    for i in range(0, string_length):
        # print(i, string_length)
        out += chr(random.randrange(char_start, char_start + char_range))
    return out

