import random 
youcnt = mecnt = 0
print('じゃんけんスタート')
print('自分の手を入力してください')
you = int(input('あなたの手は？ 0:グー 1:チョキ 2:パー'))

while(youcnt>3 or mecnt<3):

    me = random.randint(0,2)

    if you == 0:    
        print('コンピュータ:' + str(me))
        if me == you: print('あいこ')
        elif me == 1:
            print('あなたの勝ち')
            youcnt+=1
        else :
            print('あなたの負け')
            mecnt+=1


    elif you == 1:
        print('コンピュータ:' + str(me))
        if me == you: print('あいこ')
        elif me == 2: print('あなたの勝ち')
        else : print('あなたの負け')


    elif you == 2:
        print('コンピュータ:' + str(me))
        if me == you: print('あいこ')
        elif me == 0: print('あなたの勝ち')
        else : print('あなたの負け')

    else : print('終了')