# 영어타자 프로그램

# word.txt 읽어서
# 섞는다 random.shuffle()
# 임의로 하나 추출 random.choice()

# Q1) then
# input()
# input 결과에 딸 정답!! or 오타!!

# 문제 5문제 출제
# 정답 개수

# 게임시간 출력
# 출력문 => 게임시간 : 10초, 정답개수 : 3개
# 3개이상 정답인 경우 합격 or 불합격

import time, random

game_count = 0

word_txt=[]
with open ('./ch1/data/word.txt','r',encoding='utf-8') as f:

    list1 = f.readlines()
    random.shuffle(list1)
    for i in range(5):
        choice1 = random.choice(list1).strip()
        word_txt.append(choice1)

    #print(word_txt)

start = time.time()
for i in word_txt:
    print(i)
    ok = input('입력하라')

    if(i == ok):
        print('정답')
        game_count += 1
    else:
        print('틀림')

if game_count >= 3:
    print('합격')
else:
    print('나가')

end = time.time()
print(f'총 정답 : {game_count}\n시간 : {(time.time()- start):.2f}')