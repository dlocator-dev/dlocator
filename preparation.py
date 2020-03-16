import sys
import os
import json
from load_deprecation_lib import load_deprecation_lib, load_deprecation_lib_present
import time

deprec_dict = load_deprecation_lib()
deprec_dict_present = load_deprecation_lib_present()
n_rep = 0
n_ori = len(deprec_dict)
for k,v in deprec_dict_present.items():
    if k not in deprec_dict:
        deprec_dict[k] = v

for k, v in deprec_dict.items():
    if v is None:
        print(k)
    else:
        arg_str = ",".join(v)
        print("{}:{}".format(k, arg_str))


def is_hit(api_str):
    if api_str.find(':')<0:
        return False
    tmp  = api_str.split(':')
    name = tmp[0]
    kws = tmp[1] # keywords
    if name in deprec_dict:
        if deprec_dict[name] is None:
            return True
        else:
            for k in kws:
                if k in deprec_dict[name]:
                    return True
    return False

def main():
    #filename = sys.argv[1]

    #get_lazy_projects(filename)
    pass

if __name__ == '__main__':
    main()

