import sys
import os
import json
from multiprocessing import Pool

from util import get_path_by_extension
from load_deprecation_lib import load_deprecation_lib
from API_name_formating import  get_API_calls

#load targeted APIs
deprec_dict = load_deprecation_lib()

# determine if an API in targets
# input format: a string like "APIname:keyword1, keyword2,..."

def is_hit(api_str):
    if api_str.find(':')<0:
        return False
    tmp  = api_str.split(':')
    name = tmp[0] # api name
    kws = tmp[1] # keywords
    if name in deprec_dict:
        if deprec_dict[name] is None:
            # target API has no keywords specifications
            return True
        else:
            # keywords
            for k in kws:
                if k in deprec_dict[name]:
                    return True
    return False
# check a list of files to see if deprecated ones can be found
def check_single_file(filename):
    count = 0
    code_text = open(filename).read()
    func_calls_names= get_API_calls(code_text)
    for api_str in func_calls_names:
        if is_hit(api_str):
            count += 1
    return count

def main():
    data_dir = sys.argv[1]
    n_threads = int(sys.argv[2])
    pool = Pool(n_threads)
    all_file_names = get_path_by_extension(data_dir)
    #all_file_names = all_file_names[0:10000]
    results = pool.map(check_single_file, all_file_names)
    for fn, num in zip(all_file_names,results):
        if num>0:
            print(fn)

if __name__ == '__main__':
    main()

