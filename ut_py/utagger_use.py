# -*- coding: utf-8 -*-
import sys
import json
import os
from random import *
from utagger_py import UTagger
import pandas as pd

file = ['../workbook/강원.txt', '../workbook/경기.txt', '../workbook/경남.txt', '../workbook/경북.txt',
        '../workbook/전남.txt', '../workbook/전북.txt', '../workbook/충남.txt', '../workbook/충북.txt',
        '../workbook/제주.txt', '../workbook/평남.txt', '../workbook/평북.txt', '../workbook/함남.txt',
        '../workbook/함북.txt', '../workbook/황해.txt', '../workbook/중국 길림성.txt', '../workbook/중국 요령성.txt',
        '../workbook/중국 흑룡강성.txt', '../workbook/중앙아시아.txt']  # 지역별 파일
Js = [['은', '는'], ['이', '가'], ['을', '를'], ['과', '와'], ['아', '야'], ['이여', '여'], ['이랑', '랑'], ['으로', '로']]
print("프로그램 시작")
print('txt opening...')
df = pd.read_csv(os.path.abspath('../workbook/표준어사투리_뜻풀이.ver.txt'), sep="\t")  # 표준어 -> 사투리 엑셀파일 load
dt = [pd.read_csv(file[col], sep="\t") for col in range(18)]  # 사투리 -> 표준어 지역별 엑셀파일 load dt[0]=강원 dt[1]=경기...
print('txt open ok')

rt = UTagger.Load_global('..\\bin\\UTaggerR64.dll', '..\\Hlxcfg.txt')

if rt != '':
    print(rt)
    sys.exit(1)

ut = UTagger(0)  # 0은 객체 고유번호. 0~99 지정 가능. 같은 번호로 여러번 생성하면 안됨. 한 스레드당 하나씩 지정 필요.
rt = ut.new_ucma()  # 객체 생성. 객체가 있어야 유태거 이용 가능.
if rt != '':
    print(rt)
    sys.exit(1)


def df_dia(q):  # 화면에 띄울 랜덤한 사투리 8개 뽑기
    while 1:
        j = randint(4, 21)
        if df.values[q][j] != ' ':
            return df.values[q][j].split(',')[0]


def df_prime(q):  # 표준어에서 랜덤한 사투리 뽑기
    while 1:
        j = randint(4, 21)
        if df.values[q][j] != ' ':
            return df.values[q][j].split(',')[0], j


def word_game():  # 게임문제 만들기
    words = [0 for col in range(0, 12)]
    while 1:
        i = randint(0, len(df))
        if df.values[i][22] != '미존재 뜻풀이':
            break

    words[0] = df.values[i][0]
    words[11] = df.values[i][22]
    words[1], words[10] = df_prime(i)
    for t in range(2, 10):
        i = randint(0, len(df))
        words[t] = df_dia(i)
    return words


def Josa(jo):  # 조사 변경
    for i in range(len(Js)):
        for j in range(2):
            if Js[i][j] == jo:
                if j == 0:
                    return Js[i][1]
                else:
                    return Js[i][0]
    return 0


def BinarySearch_number(start, end, input_values, word_class, cal, number):  # 표준어 -> 사투리 사전검색
    mid = int((start + end) / 2)
    if (input_values == df.values[mid][0]) and (word_class == df.values[mid][2]):
        for k in range(start - 1, end + 2):
            if (input_values == df.values[k][0]) and (df.values[k][3].split('_')[0] == number):
                if df.values[k][int(cal) + 3] == ' ':
                    return 0  # 해당문자가 있으나 그 지역에 사투리가 없는 경우
                else:
                    return df.values[k][int(cal) + 3]  # 해당문자의 사투리가 있는 경우
        return 0  # 해당 문자는 있으나 어깨번호가 다른 경우
    elif start > end:
        return 0  # 해당 문자가 없는 경우
    elif input_values < df.values[mid][0]:
        return BinarySearch_number(start, mid - 1, input_values, word_class, cal, number)
    elif input_values > df.values[mid][0]:
        return BinarySearch_number(mid + 1, end, input_values, word_class, cal, number)
    else:  # 같은 단어인데 품사가 다를경우 확인
        for k in range(mid - 1, mid + 2):
            if (input_values == df.values[k][0]) and (word_class == df.values[k][2]):
                if df.values[k][3].split('_')[0] == number:
                    if df.values[k][int(cal) + 3] == ' ':
                        return 0
                    else:
                        return df.values[k][int(cal) + 3]
        return 0


def BinarySearch_dia(start, end, input_values, word_class, cal, number):  # 사투리 -> 표준어 사전검색
    mid = int((start + end) / 2)
    if (input_values == dt[int(cal) - 1].values[mid][0]) and (word_class == dt[int(cal) - 1].values[mid][2]):
        for k in range(start - 2, end + 2):
            if (input_values == dt[int(cal) - 1].values[k][0]) and (
                    str(number) == dt[int(cal) - 1].values[k][3].split('_')[0]):
                return dt[int(cal) - 1].values[k][4]  # 그 지역의 사투리가 있는 경우
        return 0  # 해당 문자가 있으나 어깨번호가 다른 경우
    elif start > end:
        return 0  # 해당 문자가 없는 경우
    elif input_values < dt[int(cal) - 1].values[mid][0]:
        return BinarySearch_dia(start, mid - 1, input_values, word_class, cal, number)
    elif input_values > dt[int(cal) - 1].values[mid][0]:
        return BinarySearch_dia(mid + 1, end, input_values, word_class, cal, number)
    else:  # 같은 단어인데 품사가 다른경우를 확인
        for k in range(mid - 1, mid + 2):
            if (input_values == dt[int(cal) - 1].values[k][0]) and (word_class == dt[int(cal) - 1].values[k][2]):
                if str(number) == dt[int(cal) - 1].values[k][3].split('_')[0]:
                    return dt[int(cal) - 1].values[k][4]
                else:
                    return 0
        return 0


def std_to_dia(local, s):  # input:s 를 사투리로 변경
    word = ''
    slang = ''
    analysis = ''
    original = s.split()
    rt = ut.analyze1(s, 3, 1)  # 분석! 형태소로 분석하여 json 형태로 보여준다. 후보(동형이의어 수준)와 대역어 등 다양한 정보를 포함한다.
    j = json.loads(rt)
    count = -1
    for i in range(1, len(j)):
        if 'CAND' not in j[i]:
            continue
        else:
            check = 0
            count += 1
            tmp_original = ''
            tmp_analyze = ''
            for t in range(len(j[i]['CAND'])):  # CAND를 기준으로 for문을 돌린다. 모든 경우의 수 확인 가능.
                point = j[i]['CAND'][t]['TAGGED'].split('+')
                tmp_std = ''
                for q in range(len(point)):  # +기준으로 split하여 for문을 돌린다. Ex) 하+여도 -> 하, 여도 각각 사전에 검색
                    if -1 == point[q].find('__'):  # 어깨번호가 없는 경우!
                        point[q] = point[q].split('/')
                        if 0 == point[q][1].find('V'):  # 용언의 경우 단어에 '다'를 붙여서 검색해준다. Ex) 먹자 -> 먹/VV + 자/EC '먹다'로 검색
                            point[q][0] += '다'
                        text = BinarySearch_number(0, len(df), point[q][0], point[q][1], local, '00')  # 사전에 단어를 검색
                        if (text == 0) and (t == 0) and (check == 0):  # 표쥰어가 사투리로 변환되지 않고 첫번째 문장일 경우!
                            tmp_original = original[count]
                            if 0 == point[q][1].find('V'):
                                tmp_std += point[q][0][:-1]
                            else:
                                tmp_std += point[q][0]
                        elif check == 1:  # 앞 단어가 사투리로 변환 되었을 경우!
                            if 0 == point[q][1].find('V'):
                                point[q][0] = point[q][0][:-1]
                            tmp_std += point[q][0]
                        elif text != 0:  # 표준어가 사투리로 변환 되었을 경우!
                            if 0 == point[q][1].find('V'):
                                tmp_std += point[q][0][:-1] + '(' + text.split(',')[0][:-1] + ')'
                            else:
                                tmp_std += point[q][0] + '(' + text.split(',')[0] + ')'
                            slang = slang + point[q][0] + ' = [ ' + text + ' ]\n'
                            tmp_analyze = j[i]['CAND'][t]['TAGGED']
                            check = 1
                    else:  # 어깨번호가 있는 경우!
                        point[q] = point[q].split('__')
                        point[q][1] = point[q][1].split('/')
                        if 0 == point[q][1][1].find('V'):  # 용언의 경우 단어에 '다'를 붙여서 검색해준다. Ex) 먹자 -> 먹/VV + 자/EC '먹다'로 검색
                            point[q][0] += '다'
                        text = BinarySearch_number(0, len(df), point[q][0], point[q][1][1], local,
                                                   point[q][1][0])  # 사전에 단어를 검색
                        if (text == 0) and (t == 0) and (check == 0):  # 표준어가 사투리로 변환되지 않고 첫 문장 일 경우!
                            tmp_original = original[count]
                            if 0 == point[q][1][1].find('V'):
                                tmp_std += point[q][0][:-1]
                            else:
                                tmp_std += point[q][0]
                        elif check == 1:  # 앞 단어가 사투리로 변환 되었을 경우!
                            if 0 == point[q][1][1].find('V'):
                                point[q][0] = point[q][0][:-1]
                            tmp_std += point[q][0]
                        elif text != 0:  # 표준어가 사투리로 변환 되었을 경우!
                            if 0 == point[q][1][1].find('V'):
                                tmp_std += point[q][0][:-1] + '(' + text.split(',')[0][:-1] + ')'
                            else:
                                tmp_std += point[q][0] + '(' + text.split(',')[0] + ')'
                            slang = slang + point[q][0] + ' = [ ' + text + ' ]\n'
                            tmp_analyze = j[i]['CAND'][t]['TAGGED']
                            check = 1
                if check == 1:  # 표준어가 사투리로 변환되었을경우 값을 저장하고 for(t)문을 멈춘다.
                    word = word + tmp_std + ' '
                    analysis = analysis + tmp_analyze + ' '
                    break
                elif (check == 0) and (t == (len(j[i]['CAND']) - 1)):  # 변환되지 않고 for문의 끝에 도달하였을때
                    word = word + tmp_original + ' '
                    analysis = analysis + j[i]['CAND'][0]['TAGGED'] + ' '
    word = word + '\n\n' + slang
    return word, analysis


def dia_to_std(local, s):  # input:s를 표준어로 변경
    word = ''
    analysis = ''
    original = s.split()
    rt = ut.analyze1(s, 20, 1)  # 분석! 형태소로 분석하여 json 형태로 보여준다. 후보(동형이의어 수준)와 대역어 등 다양한 정보를 포함한다.
    j = json.loads(rt)
    count = -1
    for i in range(1, len(j)):
        if 'CAND' not in j[i]:
            continue
        else:
            check = 0
            count += 1
            tmp_original = ''
            tmp_analyze = ''
            for t in range(len(j[i]['CAND'])):  # CAND를 기준으로 for문을 돌린다. 모든 경우의 수 확인 가능.
                point = j[i]['CAND'][t]['TAGGED'].split('+')
                tmp_dia = ''
                for q in range(len(point)):  # +기준으로 split하여 for문을 돌린다. Ex) 하+여도 하, 여도
                    if -1 == point[q].find('__'):  # 어깨번호가 없는 경우!
                        point[q] = point[q].split('/')
                        if 0 == point[q][1].find('V'):  # 용언의 경우 단어에 '다'를 붙여서 검색해준다. Ex) 묵자 -> 묵/VV + 자/EC '묵다'로 검색
                            point[q][0] += '다'
                        text = BinarySearch_dia(0, len(dt[int(local) - 1]), point[q][0], point[q][1], local,
                                                '00')  # 사전에 검색
                        if (text == 0) and (t == 0) and (check == 0):  # 사투리가 표준어로 변환되지 않고 첫번째 문장일 경우!
                            tmp_original = original[count]
                            if 0 == point[q][1].find('V'):
                                tmp_dia += point[q][0][:-1]
                            else:
                                tmp_dia += point[q][0]
                        elif check == 1:  # 앞 단어가 표준어로 변환 되었을 경우!
                            if ((ord(tmp_dia[-1]) - 44032) % 28) == 0 and (  # 종성에 유무에따라 조사를 변환시킨다. Ex) 이->가
                                    (ord(point[q - 1][0][-1]) - 44032) % 28) != 0:
                                if Josa(point[q][0]) != 0:
                                    point[q][0] = Josa(point[q][0])
                            elif ((ord(tmp_dia[-1]) - 44032) % 28) != 0 and (
                                    (ord(point[q - 1][0][-1]) - 44032) % 28) == 0:
                                if Josa(point[q][0]) != 0:
                                    point[q][0] = Josa(point[q][0])
                            if 0 == point[q][1].find('V'):
                                point[q][0] = point[q][0][:-1]
                            tmp_dia += point[q][0]
                        elif text != 0:  # 사투리가 표준어로 변환 되었을 경우!
                            if 0 == point[q][1].find('V'):
                                text = text[:-1]
                            tmp_dia += text
                            tmp_analyze = j[i]['CAND'][t]['TAGGED']
                            check = 1
                    else:  # 어깨번호가 있는 경우!
                        point[q] = point[q].split('__')
                        point[q][1] = point[q][1].split('/')
                        if 0 == point[q][1][1].find('V'):
                            point[q][0] += '다'
                        text = BinarySearch_dia(0, len(dt[int(local) - 1]), point[q][0], point[q][1][1], local,
                                                point[q][1][0])  # 사전에 검색
                        if (text == 0) and (t == 0) and (check == 0):  # 사투리가 표준어로 변환되지 않았을 경우!
                            tmp_original = original[count]
                            if 0 == point[q][1][1].find('V'):
                                tmp_dia += point[q][0][:-1]
                            else:
                                tmp_dia += point[q][0]
                        elif check == 1:  # 앞 단어가 표준어로 변환 되었을 경우!
                            if ((ord(tmp_dia[-1]) - 44032) % 28) == 0 and (  # 종성에 유무에따라 조사를 변환시킨다. Ex) 이->가
                                    (ord(point[q - 1][0][-1]) - 44032) % 28) != 0:
                                if Josa(point[q][0]) != 0:
                                    point[q][0] = Josa(point[q][0])
                            elif ((ord(tmp_dia[-1]) - 44032) % 28) != 0 and (
                                    (ord(point[q - 1][0][-1]) - 44032) % 28) == 0:
                                if Josa(point[q][0]) != 0:
                                    point[q][0] = Josa(point[q][0])
                            if 0 == point[q][1][1].find('V'):
                                point[q][0] = point[q][0][:-1]
                            tmp_dia += point[q][0]
                        elif text != 0:  # 사투리가 표준어로 변환 되었을 경우!
                            if 0 == point[q][1][1].find('V'):
                                text = text[:-1]
                            tmp_dia += text
                            tmp_analyze = j[i]['CAND'][t]['TAGGED']
                            check = 1
                if check == 1:  # 표준어가 사투리로 변환되었을경우 값을 저장하고 for(t)문을 멈춘다.
                    word = word + tmp_dia + ' '
                    analysis = analysis + tmp_analyze + ' '
                    break
                elif (check == 0) and (t == (len(j[i]['CAND']) - 1)):  # 변환되지 않고 for문의 끝에 도달하였을때
                    word = word + tmp_original + ' '
                    analysis = analysis + j[i]['CAND'][0]['TAGGED'] + ' '
    return word, analysis