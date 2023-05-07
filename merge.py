import os
import json
import shutil
import sys

from PyPDF2 import PdfMerger

def merge_dir_pdfs(s_path, f_name, t_path='./MergedBooks/'):
    fl = [f for f in os.listdir(s_path) 
          if f.endswith('.pdf') 
          and not f.endswith('整体布局.pdf')]
    fl = [os.path.join(s_path, fname) for fname in fl]
    fmerger = PdfMerger()
    for f in fl:
        fmerger.append(f)
    if not os.path.exists(t_path):
        os.mkdir(t_path)
    fmerger.write(t_path+f_name+'.pdf')

def merge_dir_codes(s_path, f_name, t_path='\\MergedBooks\\'):
    cwd = os.getcwd()
    fl = [f for f in os.listdir(s_path) 
          if not f.endswith('.pdf') 
          and not f.endswith('.md') 
          and not f.endswith('.git')]
    fl = [os.path.join(s_path, fname) for fname in fl]
    t_root_dir = cwd+t_path+f_name+'\\'
    if os.path.exists(t_root_dir):
        shutil.rmtree(t_root_dir)
    if not os.path.exists(t_root_dir):
        os.mkdir(t_root_dir)
    for d in fl:
        for f in os.listdir(d):
            nf = d+'\\'+f
            shutil.copy(nf, t_root_dir+f)

def get_lib_list(s_path, f_name):
    fl = [f for f in os.listdir(s_path) 
          if not f.endswith('.pdf') 
          and not f.endswith('.md') 
          and not f.endswith('.git')]
    fl = [os.path.join(s_path, fname) for fname in fl]
    libs = []
    for d in fl:
        for f in os.listdir(d):
            nf = d+'\\'+f
            if f.endswith('ipynb'):
                nlibs = get_ipynb_lib_list(nf)
            elif f.endswith('py'):
                nlibs = get_py_lib_list(nf)
            else:
                continue
            if nlibs:
                libs.extend(nlibs)
    return libs

def write_libs_txt(libs):
    with open('libs.txt', 'w', encoding='utf8') as f:
        fstr = ''
        for l in set(libs):
            if l in ('random', 'mpl_toolkits', 'pylab', 'calendar', 'os',
                     'colorsys', 'copy'):
                continue
            if l == 'skimage':
                l = 'scikit-image'
            fstr += f'{l}\n'
        f.write(fstr)

def get_ipynb_lib_list(fname):
    libs = []
    with open(fname, encoding='utf8') as f:
        cells = json.loads(f.read())['cells']
        for cell in cells:
            t = cell['cell_type']
            lines = cell['source']
            if t != "code":
                continue
            for line in lines:
                if line.startswith('from'):
                    lib = line.split(' ')[1]
                    lib = lib.split('.')[0].strip()
                    if lib not in sys.builtin_module_names:
                        libs.append(lib)
                if line.startswith('import'):
                    lib = line.split(' ')[1]
                    lib = lib.split('.')[0].strip()
                    if lib not in sys.builtin_module_names:
                        libs.append(lib)
    return libs

def get_py_lib_list(fname):
    libs = []
    with open(fname, encoding='utf8') as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith('from'):
                lib = line.split(' ')[1]
                lib = lib.split('.')[0].strip()
                if lib not in sys.builtin_module_names:
                    libs.append(lib)
            if line.startswith('import'):
                lib = line.split(' ')[1]
                lib = lib.split('.')[0].strip()
                if lib not in sys.builtin_module_names:
                    libs.append(lib)
    return libs

def get_dir_list():
    cwd = os.getcwd()
    fl = [f for f in os.listdir('./') if f.startswith('Book')]
    fl = [[f, cwd + '\\' + f] for f in fl]
    return fl

def merge_dirs(dir_list):
    libs = []
    for fname, fpath in dir_list:
        nlibs = get_lib_list(fpath, fname)
        libs.extend(nlibs)
        # merge_dir_codes(fpath, fname)
        # merge_dir_pdfs(fpath, fname)
    write_libs_txt(libs)

if __name__ == '__main__':
    dir_list = get_dir_list()
    merge_dirs(dir_list)
