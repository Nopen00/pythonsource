# 사용자 정의 모듈
# 함수 2개 정의
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

PI = 3.141592
class Math:
    def solv(self, r):
        return PI * (r ** 2)

# 모듈 테스트
if __name__ == '__main__': # 테스트용 다른데서 불러오면 이부분은 미실행
    print(add(7,5))
    print(sub(7,5))
    m = Math()
    print(m.solv(6))
