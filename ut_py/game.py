from tkinter.tix import *
from utagger_use import word_game, swap, local_list

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
img_heart1 = PhotoImage(file='../icon/목숨1.png')
img_heart2 = PhotoImage(file='../icon/목숨2.png')
img_heart3 = PhotoImage(file='../icon/목숨3.png')
img_gamebg = PhotoImage(file='../icon/게임화면.png')
img_start = PhotoImage(file='../icon/게임시작.png')
img_game = PhotoImage(file='../icon/게임배경.png')

global game_win, start_win, final_win, explain_win
global ans_ent, que_label, heart_image3, heart_image2, heart_image1
global answers1, answers2, answers3, answers4, answers5
global answers6, answers7, answers8, answers9
global count, check_logo
global quiz_time
global quiz_score
global label_time
global label_score
global label_explain
global root
global dia_some


def total_score():
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
   label_score.place(x=700, y=26)


def explain():
   global final_win, explain_win
   global root
   final_win.destroy()
   explain_win = Toplevel(root)
   explain_win.geometry("820x580+200+150")
   explain_win.resizable(False, False)
   explain_win.title("해설")
   explain_win.option_add("*Font", "굴림 15")

   explain_win.configure(background='white')
   explain_image = Label(explain_win, image=img_explain)
   explain_image.pack()

   onemore_button = Button(explain_win, image=img_onemore, highlightthickness=0, relief='flat', bd=0,
                           command=onemoretime)
   onemore_button.pack()
   onemore_button.place(x=510, y=477)

   for i in range(7):
       for j in range(2):
           label = Label(explain_win, text=label_explain[i][j], bg='white')
           label.pack()
           label.place(x=180+350*j, y=163+i*44)


def onemoretime():
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


def timer():
   global quiz_time
   global label_time
   global check_logo
   global count
   global start_win
   label_time = Label(start_win, text=quiz_time, bg='white')
   label_time.pack()
   label_time.place(x=700, y=490)
   label_time.after(1000, timer)
   label_time.after(1000, label_time.destroy)
   if quiz_time < 0:
       ans_ent.delete('0', END)
       label_score.destroy()
       total_score()
       label_time.destroy()
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
       no_bingo = Label(start_win, image=img_incorrect, highlightthickness=0, relief='flat', bd=0, bg='white')
       no_bingo.pack()
       no_bingo.place(x=452, y=462)
       no_bingo.after(800, no_bingo.destroy)
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
   # 점수 배점하기
   quiz_time -= 1


def gameover():
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


def new_problem():  # 9개짜리 그 화면 뜨는부분!!! 9개 선정하는거
   global dia_some
   global que_label
   global answers1, answers2, answers3, answers4, answers5
   global answers6, answers7, answers8, answers9
   global dia_some
   global quiz_time
   global count
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
   answers1.place(x=60, y=142)
   answers2.configure(text=dia_some[num[1]])
   answers2.place(x=300, y=142)
   answers3.configure(text=dia_some[num[2]])
   answers3.place(x=540, y=142)
   answers4.configure(text=dia_some[num[3]])
   answers4.place(x=60, y=225)
   answers5.configure(text=dia_some[num[4]])
   answers5.place(x=300, y=225)
   answers6.configure(text=dia_some[num[5]])
   answers6.place(x=540, y=225)
   answers7.configure(text=dia_some[num[6]])
   answers7.place(x=60, y=303)
   answers8.configure(text=dia_some[num[7]])
   answers8.place(x=300, y=303)
   answers9.configure(text=dia_some[num[8]])
   answers9.place(x=540, y=303)

   current_problem = Label(start_win, text=count, bg='white')
   current_problem.pack()
   current_problem.place(x=60, y=40)

   que_label = Label(start_win, text='\"' + dia_some[0] + '\"' + '의 사투리로 옳은 것은?', bg='white')
   que_label.pack()
   que_label.place(x=125, y=397)
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
       answers5.configure(text='')
       answers6.configure(text='')
       answers7.configure(text='')
       answers8.configure(text='')
       answers9.configure(text='')
       count += 1
       bingo = Label(start_win, image=img_correct, highlightthickness=0, relief='flat', bd=0, bg='white')
       bingo.pack()
       bingo.place(x=452, y=462)
       bingo.after(800, bingo.destroy)
       label_score.destroy()
       total_score()
       label_time.destroy()
       new_problem()
       if count == 8:
           start_win.destroy()
           final_score()
   else:
       ans_ent.delete('0', END)
       no_bingo = Label(start_win, image=img_incorrect, highlightthickness=0, relief='flat', bd=0, bg='white')
       no_bingo.pack()
       no_bingo.place(x=452, y=462)
       no_bingo.after(800, no_bingo.destroy)
       if check_logo == 3:
           heart_image1.destroy()
           check_logo = 2
       elif check_logo == 2:
           heart_image2.destroy()
           check_logo = 1
       else:
           heart_image3.destroy()
           gameover()


def start():
   global start_win
   global ans_ent
   global count
   global heart_image3, heart_image2, heart_image1
   global quiz_score
   global label_score
   global check_logo
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
   game_back = Label(start_win, image=img_gamebg)
   game_back.pack()
   heart_image1 = Label(start_win, image=img_heart1, highlightthickness=0, relief='flat', bd=0, bg='white')
   heart_image1.pack()
   heart_image1.place(x=410, y=17)
   heart_image2 = Label(start_win, image=img_heart2, highlightthickness=0, relief='flat', bd=0, bg='white')
   heart_image2.pack()
   heart_image2.place(x=480, y=17)
   heart_image3 = Label(start_win, image=img_heart3, highlightthickness=0, relief='flat', bd=0, bg='white')
   heart_image3.pack()
   heart_image3.place(x=550, y=17)

   whole_problem = Label(start_win, text='7', bg='white')
   whole_problem.pack()
   whole_problem.place(x=123, y=40)

   quiz_score = 0
   label_score = Label(start_win, text=quiz_score, bg='white')
   label_score.pack()
   label_score.place(x=700, y=25)

   new_problem()

   ans_ent = Entry(start_win, width=10)
   ans_ent.bind("<Return>", check_ans)
   ans_ent.pack()
   ans_ent.place(x=128, y=485)


def retry():
   global final_win
   final_win.destroy()
   game()


def game():
   global game_win
   game_win = Toplevel(root)
   game_win.geometry("820x580+200+150")
   game_win.resizable(False, False)
   game_win.title("낱말게임")
   game_win.configure(background='white')
   game_image = Label(game_win, image=img_game)
   game_image.pack()
   start_bu = Button(game_win, image=img_start, command=start, relief='flat', bd=0, highlightthickness=0)
   start_bu.pack()
   start_bu.place(x=257, y=410)


