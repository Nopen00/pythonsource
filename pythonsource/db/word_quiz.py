# csv 파일의 내용을 테이블에 insert하기(단, 테이블이 비어 있는 경우만 삽입)

# 테이블의 내용을 읽어서 섞은후 문제 내기
# Question #1 : 'apple' 의 뜻은?
# 1. 버스
# 2. 남편
# 3. 수줍은
# 4. 사과

# 결과 : 3 / 5 정답

# 결과를 테이블에 저장하기
# total, correct, regdate

import csv
import random
import oracledb
from datetime import datetime

conn = oracledb.connect(user='python_user', password='2394', dsn='localhost/xe')
cursor = conn.cursor()


def load_words_from_csv(file_path='./words.csv'):
    '''csv 파일을 읽어서 튜플 리스트로 반환'''
    # [(wife, 아내), (apple, 사과)]
    words_data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    word = row[0].strip()
                    meaning = row[1].strip()
                    if word and meaning:
                        words_data.append((word, meaning))
    except FileNotFoundError:
        print(f"[{file_path}] 파일을 찾을 수 없습니다.")
    return words_data


def seed_words_if_empty():
    '''words 테이블이 비어 있으면 csv 파일 내용을 읽어서 넣기'''
    sql_check = "SELECT COUNT(*) FROM words"
    cursor.execute(sql_check)
    count = cursor.fetchone()[0]

    # 테이블이 비어 있는 경우만 삽입
    if count == 0:
        words_data = load_words_from_csv()
        if words_data:
            sql_insert = "INSERT INTO words (word, meaning) VALUES (:1, :2)"
            cursor.executemany(sql_insert, words_data)
            conn.commit()
            print(f"words 테이블에 {len(words_data)}개의 단어를 등록했습니다.\n")
        else:
            print("삽입할 단어 데이터가 없습니다.\n")


def run_quiz(total_questions=5):
    '''
    1) all_words = words 테이블 읽기
    2) 무작위 문제 추출 random.sample()
    3) all_words 문제를 제외한 내용을 섞은 후 거기서 틀린 meaning 추출
    4) 답변입력받은 후 정답 맞는지 확인
    5) 최종 결과 입력
    '''
    # 1) 전체 단어 목록 조회
    cursor.execute("SELECT word_id, word, meaning FROM words")
    all_words = cursor.fetchall()

    if len(all_words) < 4:
        print("4지선다 퀴즈를 출제하기에 단어 수가 부족합니다. (최소 4개 필요)")
        return

    # 출제할 문제 수 결정 (전체 단어 수보다 클 수 없음)
    num_questions = min(total_questions, len(all_words))
    
    # 2) 무작위 문제 추출
    quiz_pool = random.sample(all_words, num_questions)
    correct_count = 0

    print("=== 단어 퀴즈 시작 ===")
    for idx, current_q in enumerate(quiz_pool, start=1):
        _, q_word, correct_meaning = current_q

        # 3) 현재 문제를 제외한 단어들에서 오답 보기(meaning) 3개 무작위 추출
        wrong_candidates = [item[2] for item in all_words if item[2] != correct_meaning]
        wrong_choices = random.sample(wrong_candidates, 3)

        # 정답과 오답 합친 후 셔플
        options = wrong_choices + [correct_meaning]
        random.shuffle(options)

        # 보기 출력
        print(f"\nQuestion #{idx} : '{q_word}' 의 뜻은?")
        for num, option in enumerate(options, start=1):
            print(f"{num}. {option}")

        # 4) 사용자 입력 및 정답 확인
        while True:
            user_input = input("정답 번호 입력 (1~4): ").strip()
            if user_input in ['1', '2', '3', '4']:
                break
            print("1, 2, 3, 4 중 하나를 입력해주세요.")

        selected_meaning = options[int(user_input) - 1]
        if selected_meaning == correct_meaning:
            print(">> 정답입니다!")
            correct_count += 1
        else:
            print(f">> 땡! 오답입니다. (정답: {correct_meaning})")

    # 결과 출력
    print("\n" + "=" * 30)
    print(f"결과 : {correct_count} / {num_questions} 정답")
    print("=" * 30)

    # 5) 최종 결과 quiz_records 테이블에 저장
    sql_record = "INSERT INTO quiz_records (total, correct, regdate) VALUES (:1, :2, SYSDATE)"
    cursor.execute(sql_record, (num_questions, correct_count))
    conn.commit()
    print("게임 결과가 저장되었습니다.\n")


if __name__ == '__main__':
    try:
        seed_words_if_empty()
        run_quiz()
    finally:
        cursor.close()
        conn.close()