def BurrowsWheelerTransform(string):
    BWT_arr = []
    str_len = len(string)
    string = string + "$"
    BWT_arr.append(string)
    curr_str = string
    for i in range(str_len):
        curr_str = curr_str[-1] + curr_str[:-1]
        BWT_arr.append(curr_str)
    BWT_arr.sort()
    BWT = ""
    for i in range(str_len+1):
        BWT += BWT_arr[i][str_len]
    return BWT



if __name__ == "main":
    string = "chitchat"
    print (BurrowsWheelerTransform(string))
