from multiprocessing import Process
from tkinter import messagebox
from random import *
from tkinter.tix import *
import pyglet


def multi_process():  # 로딩 이미지
    ag_file = "Loading.gif"
    animation = pyglet.resource.animation(ag_file)
    sprite = pyglet.sprite.Sprite(animation)
    win = pyglet.window.Window(width=sprite.width, height=sprite.height)
    green = 0, 1, 0, 1
    pyglet.gl.glClearColor(*green)

    @win.event
    def on_draw():
        win.clear()
        sprite.draw()

    pyglet.app.run()


root = Tk()
root.geometry("820x580+350+100")
root.resizable(False, False)
root.configure(background='white')
root.title("OK구슬")
root.option_add("*Font", "돋움 11")
frame = Frame(root)
frame.pack()
Radiovar = IntVar()
var = StringVar()
var_analyze = IntVar()
img_ex = PhotoImage(file='../icon/예시.png')
img_help = PhotoImage(file='../icon/사용법.png')
img_okbg = PhotoImage(file='../icon/옥구슬 배경.png')
img_onemore = PhotoImage(file='../icon/onemore.png')
img_explain = PhotoImage(file='../icon/해설화면.png')
img_100 = PhotoImage(file='../icon/당신은 사투리 고수.png')
img_90 = PhotoImage(file='../icon/만점을 향하여.png')
img_80 = PhotoImage(file='../icon/좀 더 분발해볼까.png')
img_gameover = PhotoImage(file='../icon/gameover.png')
img_sol = PhotoImage(file='../icon/해설보기.png')
img_regame = PhotoImage(file='../icon/다시하기.png')
img_score = PhotoImage(file='../icon/점수화면.png')
img_incorrect = PhotoImage(file='../icon/incorrect.png')
img_correct = PhotoImage(file='../icon/correct.png')
img_heart1 = PhotoImage(file='../icon/목숨.png')
img_heart2 = PhotoImage(file='../icon/목숨.png')
img_heart3 = PhotoImage(file='../icon/목숨.png')
img_gamebg = PhotoImage(file='../icon/게임화면.png')
img_start = PhotoImage(file='../icon/게임시작.png')
img_game = PhotoImage(file='../icon/게임배경.png')
img_logo = PhotoImage(file='../icon/로고.png')  # 로고 옥구슬
img_std = PhotoImage(file='../icon/표준어to사투리.png')
img_dia = PhotoImage(file='../icon/사투리to표준어.png')
img_kor = PhotoImage(file='../icon/국내.png')
img_nkor = PhotoImage(file='../icon/북한.png')
img_oth = PhotoImage(file='../icon/국외.png')
img_translate = PhotoImage(file='../icon/변환하기.png')

global top
global game_win, start_win, final_win, explain_win
global dia_some
global que_label, definition_label
global answers1, answers2, answers3, answers4, answers5
global answers6, answers7, answers8, answers9
global count, check_logo, heart_image3, heart_image2, heart_image1
global quiz_time, label_time
global quiz_score, label_score
global label_explain
global ans_ent

local_list = ['강원', '경기', '경남', '경북', '전남', '전북', '충남', '충북', '제주',
              '평남', '함남', '함북', '황해',
              '중국 길림성', '중국 요령성', '중국 흑룡강성', '중앙아시아']


def top_exit():
    kor_button['state'] = 'normal'
    oth_button['state'] = 'normal'
    nkor_button['state'] = 'normal'
    Radiovar.set('0')
    top.destroy()


def sel_kor():  # 국내 버튼을 선택한 경우
    if Radiovar.get() == 1:
        area_label.configure(text='강원을 선택했습니다.')
    elif Radiovar.get() == 2:
        area_label.configure(text='경기를 선택했습니다.')
    elif Radiovar.get() == 3:
        area_label.configure(text='경남을 선택했습니다.')
    elif Radiovar.get() == 4:
        area_label.configure(text='경북을 선택했습니다.')
    elif Radiovar.get() == 5:
        area_label.configure(text='전남을 선택했습니다.')
    elif Radiovar.get() == 6:
        area_label.configure(text='전북을 선택했습니다.')
    elif Radiovar.get() == 7:
        area_label.configure(text='충남을 선택했습니다.')
    elif Radiovar.get() == 8:
        area_label.configure(text='충북을 선택했습니다.')
    elif Radiovar.get() == 9:
        area_label.configure(text='제주를 선택했습니다.')
    kor_button['state'] = 'normal'
    oth_button['state'] = 'normal'
    nkor_button['state'] = 'normal'
    top.destroy()


def sel_oth():  # 국외 버튼을 선택한 경우
    if Radiovar.get() == 15:
        area_label.configure(text='중국 길림성을 선택했습니다.')
    elif Radiovar.get() == 16:
        area_label.configure(text='중국 요령성을 선택했습니다.')
    elif Radiovar.get() == 17:
        area_label.configure(text='중국 흑룡강성을 선택했습니다.')
    elif Radiovar.get() == 18:
        area_label.configure(text='중앙아시아를 선택했습니다.')
    kor_button['state'] = 'normal'
    oth_button['state'] = 'normal'
    nkor_button['state'] = 'normal'
    top.destroy()


def sel_nkor():  # 북한 버튼을 선택한 경우
    if Radiovar.get() == 10:
        area_label.configure(text='평남을 선택했습니다.')
    elif Radiovar.get() == 11:
        area_label.configure(text='평북을 선택했습니다.')
    elif Radiovar.get() == 12:
        area_label.configure(text='함남을 선택했습니다.')
    elif Radiovar.get() == 13:
        area_label.configure(text='함북을 선택했습니다.')
    elif Radiovar.get() == 14:
        area_label.configure(text='황해를 선택했습니다.')
    kor_button['state'] = 'normal'
    oth_button['state'] = 'normal'
    nkor_button['state'] = 'normal'
    top.destroy()


def radio_kor():  # 국내를 선택했을때 뜨는 라디오버튼(국내 상세 지역 선택)
    global top
    kor_button['state'] = 'disabled'
    oth_button['state'] = 'disabled'
    nkor_button['state'] = 'disabled'
    area_label.configure(text='국내를 선택했습니다.')
    area_label.option_add("*Font", "돋움 10")
    top = Toplevel()
    top.configure(background='white')
    top.option_add("*Font", "돋움 10")
    radio_button1_1 = Radiobutton(top, text="강원", bg='white', variable=Radiovar, value=1)
    radio_button1_1.pack()
    radio_button1_2 = Radiobutton(top, text="경기", bg='white', variable=Radiovar, value=2)
    radio_button1_2.pack()
    radio_button1_3 = Radiobutton(top, text="경남", bg='white', variable=Radiovar, value=3)
    radio_button1_3.pack()
    radio_button1_4 = Radiobutton(top, text="경북", bg='white', variable=Radiovar, value=4)
    radio_button1_4.pack()
    radio_button1_5 = Radiobutton(top, text="전남", bg='white', variable=Radiovar, value=5)
    radio_button1_5.pack()
    radio_button1_6 = Radiobutton(top, text="전북", bg='white', variable=Radiovar, value=6)
    radio_button1_6.pack()
    radio_button1_7 = Radiobutton(top, text="충남", bg='white', variable=Radiovar, value=7)
    radio_button1_7.pack()
    radio_button1_8 = Radiobutton(top, text="충북", bg='white', variable=Radiovar, value=8)
    radio_button1_8.pack()
    radio_button1_9 = Radiobutton(top, text="제주", bg='white', variable=Radiovar, value=9)
    radio_button1_9.pack()
    radio_click = Button(top, text="선택", command=sel_kor)
    radio_click.pack()
    top.protocol('WM_DELETE_WINDOW', top_exit)


def radio_oth():  # 국외를 선택했을때 뜨는 라디오버튼(국외 상세 지역 선택)
    global top
    kor_button['state'] = 'disabled'
    oth_button['state'] = 'disabled'
    nkor_button['state'] = 'disabled'
    area_label.configure(text='국외를 선택했습니다.')
    area_label.option_add("*Font", "돋움 10")
    top = Toplevel(root)
    top.configure(background='white')
    top.option_add("*Font", "돋움 10")
    radio_button2_1 = Radiobutton(top, text="중국 길림성", bg='white', variable=Radiovar, value=15)
    radio_button2_1.pack()
    radio_button2_2 = Radiobutton(top, text="중국 요령성", bg='white', variable=Radiovar, value=16)
    radio_button2_2.pack()
    radio_button2_3 = Radiobutton(top, text="중국 흑룡강성", bg='white', variable=Radiovar, value=17)
    radio_button2_3.pack()
    radio_button2_4 = Radiobutton(top, text="중앙아시아", bg='white', variable=Radiovar, value=18)
    radio_button2_4.pack()
    radio_click = Button(top, text="선택", command=sel_oth)
    radio_click.pack()
    top.protocol('WM_DELETE_WINDOW', top_exit)


def radio_nkor():  # 북한을 선택했을때 뜨는 라디오버튼(북한 상세 지역 선택)
    global top
    kor_button['state'] = 'disabled'
    oth_button['state'] = 'disabled'
    nkor_button['state'] = 'disabled'
    area_label.configure(text='북한을 선택했습니다.')
    area_label.option_add("*Font", "돋움 10")
    top = Toplevel(root)
    top.configure(background='white')
    top.option_add("*Font", "돋움 10")
    radio_button3_1 = Radiobutton(top, text="평남", bg='white', variable=Radiovar, value=10)
    radio_button3_1.pack()
    radio_button3_2 = Radiobutton(top, text="평북", bg='white', variable=Radiovar, value=11)
    radio_button3_2.pack()
    radio_button3_3 = Radiobutton(top, text="함남", bg='white', variable=Radiovar, value=12)
    radio_button3_3.pack()
    radio_button3_4 = Radiobutton(top, text="함북", bg='white', variable=Radiovar, value=13)
    radio_button3_4.pack()
    radio_button3_5 = Radiobutton(top, text="황해", bg='white', variable=Radiovar, value=14)
    radio_button3_5.pack()
    radio_click = Button(top, text="선택", command=sel_nkor)
    radio_click.pack()
    top.protocol('WM_DELETE_WINDOW', top_exit)


def translate():  # 번역하기 버튼을 선택한 경우
    var.set('')
    global txt_output
    root.option_add("*Font", "돋움 11")
    if Radiovar.get() == 0:
        messagebox.showwarning('!', '지역을 선택해 주세요!')
    else:
        if std_button['image'] == str(img_std):
            word, analysis = std_to_dia(Radiovar.get(), txt_input.get("1.0", "end"))
            txt_output = Text(root, bg='white', state='disabled', relief='flat', width=30, height=7)
            txt_output.configure(state='normal')
            txt_output.insert(END, word)
            txt_output.configure(state='disabled')
            txt_output.pack()
            txt_output.place(x=489, y=368)
            root.option_add("*Font", "돋움 10")
            analyze = Message(root, textvariable=var_analyze, bg='white', relief='flat', width=700)
            var_analyze.set(analysis)
            analyze.pack()
            analyze.place(x=80, y=513)
        else:
            word, analysis = dia_to_std(Radiovar.get(), txt_input.get("1.0", "end"))
            txt_output = Text(root, bg='white', state='disabled', relief='flat', width=30, height=7)
            txt_output.configure(state='normal')
            txt_output.insert(END, word)
            txt_output.configure(state='disabled')
            txt_output.pack()
            txt_output.place(x=489, y=368)
            root.option_add("*Font", "돋움 10")
            analyze = Message(root, textvariable=var_analyze, bg='white', relief='flat', width=700)
            var_analyze.set(analysis)
            analyze.pack()
            analyze.place(x=80, y=513)


def change():  # 표준어 to 사투리 / 사투리 to 표준어 버튼 선택
    if std_button['image'] == str(img_std):
        std_button['image'] = img_dia
    else:
        std_button['image'] = img_std


def reset():  # 로고 선택시 입력값, 출력값, 지역 리셋
    global txt_output
    root.option_add("*Font", "돋움 10")
    kor_button['state'] = 'normal'
    oth_button['state'] = 'normal'
    nkor_button['state'] = 'normal'
    area_label.configure(text='지역을 선택해 주세요.')
    std_button['image'] = img_std
    txt_input.delete("1.0", "end")
    txt_output.configure(state='normal')
    txt_output.delete("1.0", "end")
    txt_output.configure(state='disabled')
    Radiovar.set('0')
    var_analyze.set('')


def dia_example():  # 국내 각 지역별 예시 사투리 문장
    ex = Toplevel(root)
    ex.geometry("590x440+150+70")
    ex.resizable(False, False)
    ex.title("사투리 예시 모음")
    ex.configure(background='white')
    ex.option_add("*Font", "돋움 12")
    ex_marvel = Label(ex, image=img_ex)
    ex_list = Text(ex, state='disabled', width=60, height=15, bg="white", highlightthickness=0,
                   relief='flat', bd=0)
    ex_list.configure(state='normal')
    ex_list.insert(END, '\n<강원>\n\n\t마날장아찌랑 맛소굼 가주와라\n\n\t저 게그른 눔 거칫하문 그짓말이야\n\n\n<경기>\n\n\t우째 방뎅이를 그리 흔드냐\n\n'
                        '\t아츰에 암쾡이가 을마나 애옹애옹 울던지\n\n\n<경남>''\n\n\t아릿동네 쌍디네 내러가면서 고고매랑 구구매 쪼매 가가라\n\n'
                        '\t저개 정지에서 감자찌짐이랑 덴장국 꾸렁내가 나더라\n\n\n<경북>\n\n\t앤 복송아 색까리 와 이래?!\n\n'
                        '\t바댁에 멀까락이랑 속눈섶이 니찌네.\n\n\n<전남>\n\n\t가는비가 뜬걸로 오네?\n\n'
                        '\t마댕에서 띤죽 머그자.\n\n\n<전북>\n\n\t냇갈에 가달썩이 많네!\n\n\t갑재키 퇴깽이가 숨풀로 냇다 단발진다.\n\n\n'
                        '<충남>\n\n\t얘! 봄판 하지감자가 맛있단다!\n\n\t진당 이르내야?\n\n\n'
                        '<충북>\n\n\t그거 워요일 새벅에 새닥이 가주온 청북장이라더라\n\n'
                        '\t올개 에사춘 결온식에 나랑 누야만 가나?\n\n\n'
                        '<제주>\n\n\t얼저뭇에 그 아주방네 집에 한갑잔체 했다던데.\n\n'
                        '\t가싸 강생이랑 멜락 퀴던 소나의놈이 어느제 베개동산에\n\n\t갔는지 알고 있나?\n')
    ex_list.configure(state='disabled')
    ex_list.pack()
    ex_list.place(x=42, y=93)
    ex_marvel.pack()



def help():  # 옥구슬 프로그램 사용방법
    he = Toplevel(root)
    he.geometry("590x440+150+150")
    he.resizable(False, False)
    he.title("옥구슬 설명서")
    he.option_add("*Font", "돋움 10")
    help_marvel = Label(he, image=img_help)
    help_marvel.pack()
    he.configure(background='white')


def input_reset():  # X버튼 눌렀을 때 입력값, 출력값 리셋
    txt_input.delete("1.0", "end")
    txt_output.configure(state='normal')
    txt_output.delete("1.0", "end")
    txt_output.configure(state='disabled')
    var_analyze.set('')


def swap():  # 퀴즈 자리 섞기
    dia_random = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    t = randint(0, 8)
    tmp = dia_random[0]
    dia_random[0] = dia_random[t]
    dia_random[t] = tmp
    return dia_random


def total_score():  # 퀴즈 7문제 점수 계산
    global quiz_score
    global label_score
    if quiz_time >= 16:
        quiz_score += 10
    elif quiz_time >= 12:
        quiz_score += 8
    elif quiz_time >= 8:
        quiz_score += 6
    elif quiz_time >= 4:
        quiz_score += 4
    elif quiz_time >= 2:
        quiz_score += 2
    elif quiz_time >= 0:
        quiz_score += 1
    label_score = Label(start_win, text=quiz_score, bg='white')
    label_score.pack()
    label_score.place(x=710, y=37)


def explain():  # 퀴즈 해설
    global final_win, explain_win
    final_win.destroy()
    explain_win = Toplevel(root)
    explain_win.geometry("820x580+200+150")
    explain_win.resizable(False, False)
    explain_win.title("해설")
    explain_win.option_add("*Font", "굴림 15")

    explain_win.configure(background='white')
    explain_image = Label(explain_win, image=img_explain)
    explain_image.pack()

    onemore_button = Button(explain_win, image=img_onemore, highlightthickness=0,
                            relief='flat', bd=0, command=onemoretime)
    onemore_button.pack()
    onemore_button.place(x=583, y=510)

    for i in range(7):
        for j in range(2):
            label = Label(explain_win, text=label_explain[i][j], bg='white')
            label.pack()
            label.place(x=105+270*j, y=139+i*53)


def onemoretime():  # 다시하기 버튼
    global explain_win
    explain_win.destroy()
    game()


def final_score():  # 점수 화면 창에 뜰 최종 점수
    global check_logo, quiz_score
    global final_win
    final_win = Toplevel(root)
    final_win.geometry("820x580+200+150")
    final_win.resizable(False, False)
    final_win.title("점수")
    final_win.option_add("*Font", "굴림 70")
    final_win.configure(background='white')
    final_image = Label(final_win, image=img_score)
    final_image.pack()
    final_score = quiz_score + (check_logo * 10)
    final_s = Label(final_win, text=final_score, bg='white', fg='dodger blue', pady=1)
    final_s.pack()
    final_s.place(x=350, y=103)
    regame_button = Button(final_win, image=img_regame, highlightthickness=0, relief='flat', bd=0, command=retry)
    regame_button.pack()
    regame_button.place(x=118, y=360)
    solution_button = Button(final_win, image=img_sol, highlightthickness=0, relief='flat', bd=0, command=explain)
    solution_button.pack()
    solution_button.place(x=430, y=360)

    if final_score == 100:
        score_100 = Label(final_win, image=img_100, highlightthickness=0, relief='flat', bd=0)
        score_100.pack()
        score_100.place(x=202, y=230)
    elif 90 <= final_score <= 99:
        score_90 = Label(final_win, image=img_90, highlightthickness=0, relief='flat', bd=0)
        score_90.pack()
        score_90.place(x=270, y=230)
    else:
        score_80 = Label(final_win, image=img_80, highlightthickness=0, relief='flat', bd=0)
        score_80.pack()
        score_80.place(x=197, y=230)


def timer():  # 퀴즈 타이머
    global quiz_time, label_time
    global check_logo
    global count
    global start_win
    label_time = Label(start_win, text=quiz_time, bg='white')
    start_win.option_add("*Font", "굴림 20")
    label_time.pack()
    label_time.place(x=700, y=515)
    label_time.after(1000, timer)
    label_time.after(1000, label_time.destroy)
    if quiz_time < 0:
        ans_ent.delete('0', END)
        label_score.destroy()
        total_score()
        label_time.destroy()
        definition_label.destroy()
        ans_ent.delete('0', END)
        que_label.configure(text='')
        answers1.configure(text='')
        answers2.configure(text='')
        answers3.configure(text='')
        answers4.configure(text='')
        answers5.configure(text='')
        answers6.configure(text='')
        answers7.configure(text='')
        answers8.configure(text='')
        answers9.configure(text='')

        count += 1
        incorrect = Label(start_win, image=img_incorrect, highlightthickness=0, relief='flat', bd=0, bg='white')
        incorrect.pack()
        incorrect.place(x=443, y=504)
        incorrect.after(800, incorrect.destroy)
        if check_logo == 3:
            heart_image1.destroy()
            check_logo = 2
        elif check_logo == 2:
            heart_image2.destroy()
            check_logo = 1
        else:
            heart_image3.destroy()
            gameover()
        new_problem()
        if count == 8:
            start_win.destroy()
            final_score()
        return 0

    quiz_time -= 1


def gameover():  # 게임오버 화면
    global final_win, start_win
    start_win.destroy()
    final_win = Toplevel(root)
    final_win.geometry("820x580+200+150")
    final_win.resizable(False, False)
    final_win.title("게임종료")
    gameover_image = Label(final_win, image=img_gameover)
    gameover_image.pack()
    retry_bu = Button(final_win, image=img_regame, command=retry, relief='flat', bd=0, highlightthickness=0)
    retry_bu.pack()
    retry_bu.place(x=412, y=355)
    solution_bu = Button(final_win, image=img_sol, command=explain, relief='flat', bd=0, highlightthickness=0)
    solution_bu.pack()
    solution_bu.place(x=140, y=355)


def new_problem():  # 퀴즈 보기 9문제 랜덤
    global dia_some
    global que_label, definition_label
    global answers1, answers2, answers3, answers4, answers5
    global answers6, answers7, answers8, answers9
    global dia_some
    global quiz_time
    global count
    start_win.option_add("*Font", "굴림 20")

    answers1 = Label(start_win, text='', bg='white')
    answers1.pack()
    answers2 = Label(start_win, text='', bg='white')
    answers2.pack()
    answers3 = Label(start_win, text='', bg='white')
    answers3.pack()
    answers4 = Label(start_win, text='', bg='white')
    answers4.pack()
    answers5 = Label(start_win, text='', bg='white')
    answers5.pack()
    answers6 = Label(start_win, text='', bg='white')
    answers6.pack()
    answers7 = Label(start_win, text='', bg='white')
    answers7.pack()
    answers8 = Label(start_win, text='', bg='white')
    answers8.pack()
    answers9 = Label(start_win, text='', bg='white')
    answers9.pack()

    dia_some = word_game()
    num = swap()
    label_explain[count - 1][0] = dia_some[0]
    label_explain[count - 1][1] = dia_some[1] + '(' + local_list[dia_some[10] - 4] + ')'

    answers1.configure(text=dia_some[num[0]])
    answers1.place(x=60, y=135)
    answers2.configure(text=dia_some[num[1]])
    answers2.place(x=300, y=135)
    answers3.configure(text=dia_some[num[2]])
    answers3.place(x=542, y=135)
    answers4.configure(text=dia_some[num[3]])
    answers4.place(x=60, y=217)
    answers5.configure(text=dia_some[num[4]])
    answers5.place(x=300, y=217)
    answers6.configure(text=dia_some[num[5]])
    answers6.place(x=542, y=217)
    answers7.configure(text=dia_some[num[6]])
    answers7.place(x=60, y=298)
    answers8.configure(text=dia_some[num[7]])
    answers8.place(x=300, y=298)
    answers9.configure(text=dia_some[num[8]])
    answers9.place(x=542, y=298)

    current_problem = Label(start_win, text=count, bg='white')
    current_problem.pack()
    current_problem.place(x=65, y=35)

    que_label = Label(start_win, text='\"' + dia_some[0] + '\"' + '의 사투리로 옳은 것은?', bg='white')
    que_label.pack()
    que_label.place(x=137, y=385)
    start_win.option_add("*Font", "굴림 13")
    definition_label = Label(start_win, text=dia_some[0] + ' : ' + dia_some[11], bg='white')
    definition_label.pack()
    definition_label.place(x=144, y=417)

    start_win.option_add("*Font", "굴림 20")
    quiz_time = 20
    timer()


def check_ans(event):  # 엔터 눌렀을때 정답인지 오답인지
    global count
    global check_logo
    global start_win
    if dia_some[1] == ans_ent.get():
        ans_ent.delete('0', END)
        que_label.configure(text='')
        answers1.configure(text='')
        answers2.configure(text='')
        answers3.configure(text='')
        answers4.configure(text='')
        answers5.configure(text='')
        answers6.configure(text='')
        answers7.configure(text='')
        answers8.configure(text='')
        answers9.configure(text='')
        count += 1
        correct = Label(start_win, image=img_correct, highlightthickness=0, relief='flat', bd=0, bg='white')
        correct.pack()
        correct.place(x=443, y=504)
        correct.after(800, correct.destroy)
        label_score.destroy()
        total_score()
        label_time.destroy()
        definition_label.destroy()
        new_problem()
        if count == 8:
            start_win.destroy()
            final_score()
    else:
        ans_ent.delete('0', END)
        incorrect = Label(start_win, image=img_incorrect, highlightthickness=0, relief='flat', bd=0, bg='white')
        incorrect.pack()
        incorrect.place(x=443, y=504)
        incorrect.after(800, incorrect.destroy)
        if check_logo == 3:
            heart_image1.destroy()
            check_logo = 2
        elif check_logo == 2:
            heart_image2.destroy()
            check_logo = 1
        else:
            heart_image3.destroy()
            gameover()


def start():  # 게임 시작 화면
    global start_win
    global ans_ent, check_logo
    global count
    global heart_image3, heart_image2, heart_image1
    global quiz_score, label_score
    global label_explain

    label_explain = [['' for col in range(2)] for row in range(8)]
    check_logo = 3
    count = 1
    game_win.destroy()
    start_win = Toplevel(root)
    start_win.option_add("*Font", "굴림 20")
    start_win.geometry("820x580+200+150")
    start_win.resizable(False, False)
    start_win.title("낱말게임")
    game_background = Label(start_win, image=img_gamebg)
    game_background.pack()
    heart_image1 = Label(start_win, image=img_heart1, highlightthickness=0, relief='flat', bd=0, bg='white')
    heart_image1.pack()
    heart_image1.place(x=420, y=11)
    heart_image2 = Label(start_win, image=img_heart2, highlightthickness=0, relief='flat', bd=0, bg='white')
    heart_image2.pack()
    heart_image2.place(x=490, y=11)
    heart_image3 = Label(start_win, image=img_heart3, highlightthickness=0, relief='flat', bd=0, bg='white')
    heart_image3.pack()
    heart_image3.place(x=560, y=11)

    whole_problem = Label(start_win, text='7', bg='white')
    whole_problem.pack()
    whole_problem.place(x=129, y=35)

    quiz_score = 0
    label_score = Label(start_win, text=quiz_score, bg='white')
    label_score.pack()
    label_score.place(x=710, y=37)

    new_problem()

    ans_ent = Entry(start_win, width=10)
    ans_ent.bind("<Return>", check_ans)
    ans_ent.pack()
    ans_ent.place(x=135, y=512)


def retry():  # 다시하기
    global final_win
    final_win.destroy()
    game()


def game():  # 게임 화면
    global game_win
    game_win = Toplevel(root)
    game_win.geometry("820x580+200+150")
    game_win.resizable(False, False)
    game_win.title("낱말게임")
    game_win.configure(background='white')
    game_image = Label(game_win, image=img_game)
    game_image.pack()
    start_button = Button(game_win, image=img_start, command=start, relief='flat', bd=0, highlightthickness=0)
    start_button.pack()
    start_button.place(x=257, y=410)


ok_background = Label(root, image=img_okbg)
ok_background.pack()

imageLabel = Button(root, image=img_logo, bg='white', command=reset, relief='flat')
imageLabel.pack()
imageLabel.place(x=340, y=8)

std_button = Button(root, image=img_std, relief='flat', bd=1, command=change, bg="white")
std_button.pack()
std_button.place(x=290, y=172)

trans_button = Button(root, image=img_translate, relief='flat', bd=1, command=translate, bg="white")
trans_button.pack()
trans_button.place(x=357, y=350)

txt_input = Text(root, width=30, height=8, bd=0)
txt_input.pack()
txt_input.place(x=57, y=368)

txt_output = Text(root, bg='white', relief='flat', state='disabled', width=30, height=8)
txt_output.pack()
txt_output.place(x=489, y=368)

X_button = Button(root, text="X", bd=1, command=input_reset, relief='flat', bg="alice blue")
X_button.pack()
X_button.place(x=316, y=328)

root.option_add("*Font", "돋움 10")
area_label = Label(root, text="지역을 선택해 주세요", bg='white')
area_label.pack()
area_label.place(x=341, y=283)

kor_button = Button(root, image=img_kor, command=radio_kor, relief='flat',
                    bd=1, bg="white", activebackground="alice blue")
kor_button.pack()
kor_button.place(x=240, y=230)

oth_button = Button(root, image=img_oth, command=radio_oth, relief='flat',
                    bd=1, bg="white", activebackground="alice blue")
oth_button.pack()
oth_button.place(x=357, y=230)

nkor_button = Button(root, image=img_nkor, command=radio_nkor, relief='flat',
                     bd=1, bg="white", activebackground="alice blue")
nkor_button.pack()
nkor_button.place(x=473, y=230)

file = None
root.option_add("*Font", "돋움 11")

me = Menu(root)
menu_file = Menu(me, tearoff=0, bg='white')
menu_file.add_command(label="도움", command=help)
menu_file.add_command(label="예시", command=dia_example)
menu_file.add_command(label="퀴즈", command=game)
menu_file.add_separator()
menu_file.add_command(label="종료", command=root.destroy)
me.add_cascade(label="메뉴", me=menu_file)

root.config(me=me)

if __name__ == '__main__':
    t = Process(target=multi_process)
    t.start()
    from utagger_use import std_to_dia, dia_to_std, word_game

    t.kill()
    root.mainloop()