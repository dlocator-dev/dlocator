
##What is DLocator? 
Dlocator is to developed for automactically extracting APIs from Python source.
##How it works
The tool firstly take python source project as input and then search all Python scripts. For each of source files, it firstly build the abstract syntax tree (AST), then visit all nodes of the tree. By using two mapping structures constructed from import and from-import statements  in source code, the tool will recover function call names to its full names (fully qualified name [1]) for futher analysis. 

##How to use it
You can use the following command to run this tool in Linux system.
```console
 python main.py  project_folder  number_of_threads
```
For example,
```console
  python main.py  my_code_repo  8
```
 where my_code_repo is a Python project folder. 8 is the number of threads you are going to use.

##References
[1] Zhang, Z., Zhu, H., Wen, M., Tao, Y., Liu, Y., & Xiong, Y. How Do Python Framework APIs Evolve?.

