# load data from the file 
def load_deprecation_lib():
    filename = 'data.txt'
    lines = open(filename).readlines()
    deprecation_lib = {}
    for line in lines:
        tmp = line.strip().split(':')
        API_name = tmp[0]
        arg_name=None
        if len(tmp)>1:
            arg_name = tmp[1].split(',')
        if arg_name == '':
            deprecation_lib[API_name]=None
        else:
            deprecation_lib[API_name]=arg_name
    return deprecation_lib
