import os
import re


def vlookup(p):
    names = os.listdir(p)
    for name in names:
        new_path = p+'/'+name
        if os.path.isdir(new_path):
            vlookup(new_path)
        elif os.path.isfile(new_path):
            file_rename(new_path)

# 要求f是个完整路径
def file_rename(f):
    rename_str = '【瑞客论坛 www.ruike1.com】'
    pass_str = 'bdc-downloading'
    if rename_str in f and pass_str not in f:
        os.rename(f,f.replace(rename_str,''))
        print(f,'==>',f.replace(rename_str,''))
    else:
        print(f, "：文件名未匹配，跳过")


filepath = '/Users/xxxl/Study/达内Python1903班【完整 无加密】'
if __name__ == '__main__':
    vlookup(filepath)

    
