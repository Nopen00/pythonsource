import oracledb
from datetime import datetime

conn = oracledb.connect(user='python_user', password='2394', dsn='localhost/xe')
cursor = conn.cursor()

def add_transaction():
    tx_type = input('구분을 입력하세요(수입/지출) : ').strip()
    amount = input('금액을 입력하세요 : ').strip()
    memo = input('내역을 입력하세요 : ').strip()
    reg_date = input('날짜를 입력하세요 (YYYY-MM-DD, 엔터시 오늘): ').strip()

    if not reg_date:
        reg_date = datetime.now().strftime("%Y-%m-%d")


    sql = 'INSERT INTO transactions (tx_type, amount, memo,reg_date) VALUES (:1, :2,:3,:4)'
    cursor.execute(sql, (tx_type, amount, memo,reg_date))
    conn.commit()
    print('등록되었습니다.\n')

def list_transaction():
    """reg_date asc"""
    # 번호 [지출] 300000원 - 용돈(2026-08-18)
    sql = 'SELECT tx_id, tx_type, amount, memo,reg_date FROM transactions ORDER BY reg_date'
    cursor.execute(sql)
    rows = cursor.fetchall()

    if not rows:
        print('등록된 가계부 목록은 없습니다.\n')
        return

    print('-' * 50)
    for row in rows:
        print(f'{row[0]}. [{row[1]}] {row[2]}원 -  {row[3]}({row[4]})')
    print('-' * 50)
    print()

def monthly_transaction():

    month = input('조회할 월을 입력하세요 (YYYY-MM): ').strip()

    sql = '''
    SELECT tx_type, SUM(amount)
    FROM transactions
    WHERE reg_date LIKE '2026-08%' 
    GROUP BY tx_type
    '''
    cursor.execute(sql,(month+'%',))
    rows = cursor.fetchall()

    if not rows:
        print('요청하신 해당 월 가계부 내역은 없습니다.\n')
        return

    print('-' * 50)
    for row in rows:
        print(f'{row[0]} : {row[1]}원')
    print('-' * 50)
    print()

def menu():
    # 1. 내역 추가 2. 저체 조회 3. 월별 합계 4. 종료
    while True:
            print("=== 가계부 ===")
            print("1. 내역 추가 2. 전체 조회 3. 월별 합계 4. 종료")
    
            choice = input("선택 : ").strip()
    
            if choice == "1":
                add_transaction()
            elif choice == "2":
                list_transaction()
            elif choice == "3":
                monthly_transaction()
            elif choice == "4":
                print("종료합니다.")
                break
            else:
                print("번호를 확인해 주세요.\n")
    





if __name__ == '__main__':
    try:
        menu()
    finally:
        cursor.close()
        conn.close()