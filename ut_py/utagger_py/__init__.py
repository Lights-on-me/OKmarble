#-*- coding: utf-8 -*-
import sys
import os
from ctypes import *
from ctypes import cdll
import json

#주의! 유태거 dll은 보통 64비트이기 때문에, 파이썬도 64비트를 사용해야 합니다.
#기본은 파이썬3 지원입니다. 파이썬2도 사용하기 위해 아래 u8, my_in 필요.
#파이썬 2, 3 지원. py소스파일이 u8로 코딩. dll로 wchar_p를 넘기는 용도.
v = sys.version_info[0]
def u8(s):
    if v==2:
        #print '2 '
        return unicode( s.decode('utf-8') )
    else : # if v==3:
        #print '3 '
        return c_wchar_p(s)
    
#파이썬2에서 키보드입력 받은 것을 utf8로 사용. msg는 유니코드여야한다. my_in(u'샘플:') 이런식으로
def my_in(msg):
    print(msg)
    if v==2:
        text = raw_input().decode(sys.stdin.encoding or locale.getpreferredencoding(True)).encode('utf-8')
    else :
        text = input()
    return text

#lib = cdll.LoadLibrary('../bin/UTagger.so') # so 로드 리눅스.

class UTagger(object):
    global_loaded = False

    @staticmethod
    def Load_global(dll_path, hlxcfg_path):
        if UTagger.global_loaded == True:
            return 'already loaded'
        
        print("python call utagger function")

        lib = cdll.LoadLibrary(dll_path) # dll 로드 윈도우
        UTagger.lib = lib

        #설정파일의 위치를 절대경로로 구하기. py에서의 현재경로와, dll에서의 현재경로가 다르기 때문.
        #hlx_pass = os.path.join( os.path.dirname(sys.argv[0]), hlxcfg_path)
        hlx_pass = os.path.abspath(hlxcfg_path)
        print(hlx_pass)
        cstr_hlx = c_char_p( hlx_pass.encode('cp949') )#hlxcfg 파일 경로를 cp949로 인코딩.

        lib.Global_init2.restype = c_wchar_p #유태거 초기화 함수의 반환자 정의
        msg = lib.Global_init2( cstr_hlx , 0) # Hlxcfg.txt 위치 지정. 학습 파일 로딩. 오래걸림.

        if msg != '': # Hlxcfg.txt와 모든 학습 파일을 읽었는지 확인.
            return msg

        
        UTagger.lib.newUCMA2.restype = c_wchar_p #ucma 생성 함수의 반환자 정의
        
        #dll의 태깅함수 정의. 사용하기 편하게.
        tag_line = lib.cma_tag_line_BSP #함수 가져오기
        tag_line.restype = c_wchar_p #반환자 설정.

        tag_line_json = lib.cma_tag_line_json2 #함수 가져오기
        tag_line_json.restype = c_wchar_p #반환자 설정.

        #uwm api 함수 정의
        lib.DLL_UWM_1.restype=c_wchar_p

        #대역어 함수 정의
        lib.cma_tag_target_word_json2.restype=c_wchar_p
        
        lib.cma_analyze1.restype = c_wchar_p
        lib.cma_word_info.restype = c_wchar_p
        lib.cma_polysemy.restype = c_wchar_p
        lib.cma_bsp_dep2_js.restype = c_wchar_p
        lib.cma_bsp_dep_srl_js.restype = c_wchar_p

        lib.cma_line_depen_json.restype = c_wchar_p #의존 규

        UTagger.global_loaded = True
        return ''

    @staticmethod
    def Release_global():
        if UTagger.global_loaded:
            UTagger.lib.Global_release()
            UTagger.global_loaded = False

    def __init__(self, th_num):
        self.th_num = th_num

    def __del__(self):
        self.release_ucma()
    
    def new_ucma(self):
        msg = UTagger.lib.newUCMA2(self.th_num) # 유태거의 th_num번 객체 생성(0~99까지 생성 가능)
        if msg != '':
            return msg
        
        UTagger.lib.cmaSetNewlineN(self.th_num) #유태거 tag_line이 newline을 만들 때 /r/n 이 아니라 /n이 되게 한다.
        return ''

    def release_ucma(self):
        UTagger.lib.deleteUCMA(self.th_num)
        
    def tag_line(self, s, style):
        rt = UTagger.lib.cma_tag_line_BSP(self.th_num, u8(s), style)
        return rt

    def analyze1(self, sent, cand, lang_code):
        rt = UTagger.lib.cma_analyze1(self.th_num, u8(sent), cand, lang_code)
        return rt

    def uwm1(self, api):
        rt = UTagger.lib.DLL_UWM_1(self.th_num, u8(api))
        return rt

    def word_info(self, bsp, lang_code):
        rt = UTagger.lib.cma_word_info( self.th_num, u8(bsp), lang_code )
        return rt

    def polysemy(self, b, p):
        rt = UTagger.lib.cma_polysemy(self.th_num, u8(b), u8(p))
        return rt

    def depen(self, s):
        rt = UTagger.lib.cma_line_depen_json( self.th_num, u8(s), 0 )
        return rt

    def depen2(self, s):
        rt = UTagger.lib.cma_bsp_dep2_js( self.th_num, u8(s) )
        return rt
    
    def bsp_dep_srl_js(self, s):
        rt = UTagger.lib.cma_bsp_dep_srl_js( self.th_num, u8(s) )
        return rt






              
