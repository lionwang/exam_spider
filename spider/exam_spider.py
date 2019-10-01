import sys

from spider.exam_lib.offcn_exam_lib import OffcnExamLib
from spider.exam_lib.huatu_exam_lib import HuatuExamLib

import os

def parse_arg(arg, kv):
    args = arg.split('=')
    if len(args) != 2:
        print(arg+'参数错误')
    kv[args[0]] = args[1]

def main():    
    argv = sys.argv
    lib = argv[1]
    if lib == 'help':
        print('使用方法:python examspider doc=[doc_name.docx] [options]-------\n\
                type=option option可取值[行测，申论，面试]\n\
                from=option 为爬取开始页面\n\
                to=option   为爬取结束页面')
    else:
        file_path = './exam_doc'
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        kv = {}
        for arg in argv[2:]:
            parse_arg(arg, kv)
        doc_name = kv.get('doc')
        if doc_name == None:
            print('没有输入生成的word文件名称，请输入要保存到的文件名称')
            return
        
        exam_type = kv.get('type')
        if exam_type == None:
            exam_type = '行测'
        
        from_page = kv.get('from')
        if from_page == None:
            from_page = '1'
        
        to_page = kv.get('to')
        if to_page == None:
            to_page = '5'
        
        if lib == 'offcn':
            # 中公
            OffcnExamLib(file_path).request(doc_name, exam_type, int(from_page), int(to_page))
        elif lib == 'huatu':
            # 华图
            HuatuExamLib(file_path).request(doc_name, exam_type, int(from_page), int(to_page))
        else:
            print('参数不正确，使用help查看使用方法')

if __name__ == '__main__':
    main()
