import sys

from docx import Document
from bs4 import BeautifulSoup

from spider import request_util as requestUtil
from spider.exam_lib.exam_lib import ExamLib

'''华图公考题目'''
class HuatuExamLib(ExamLib):

    base_url = 'http://www.huatu.com/guojia/ziliao/'
    '''
    exam_type_dict = {
            '常识判断': 'cspd',
            '语言理解与表达':'yyljybd',
            '数量关系': 'slgx',
            '判断推理': 'pdtl',
            '行测专题': 'xczt',
            '行测模拟': 'xcmn',
            '每日一练': 'mryl',
            '经验分享': 'jyfx',
            '申论真题': 'slzt',
            '申论模拟': 'slmn',
            '申论': 'sl',
            '面试真题': 'mszt'
            }
    '''
    exam_type_dict = {
            '行测': 'xc',
            '申论': 'sl',
            '面试': 'ms'
            }
    def __init__(self, file_dir = './'):
        self.file_dir = file_dir

    def request(self, file_name, exam_type='行测', from_page=1, to_page=5):
        word = Document()
        type_value = self.exam_type_dict.get(exam_type)
        if type_value != None:
            print('--------开始下载试题---------')
            for index in range(from_page, to_page+1):
                url = None
                if index > 1:
                    url = self.base_url+type_value+'/'+str(index)+'.html'
                else:
                    url = self.base_url+type_value
                self.request_index_page(word, url)
            word.save(self.file_dir+'/'+file_name)
            print('\n-------试题下载完成-------')
        else:
            print('-------没有该类型试题------')

    def request_index_page(self, word, url):
        html = requestUtil.get_html(url, self.encoding)
        if html != None:
            bs = BeautifulSoup(html, features='html5lib')
            div = bs.find('div', class_='fxlist_Conday')
            if div != None:
                for ul in div.findAll('ul'):
                    for li in ul.findAll('li'):
                        a = li.find('a', class_='title')
                        if a != None:
                            self.request_exam_page(a['href'], word) 
                            print('>', end='', flush=True)

    '''解析页面'''
    def request_exam_page(self, url, word, is_depth=False):
        html = requestUtil.get_html(url, self.encoding)
        if html != None:
            doc = BeautifulSoup(html, features='html5lib')
            self.add_paragraph(word, doc.find('div', class_='artBcon'), is_depth)


