import datetime #날짜 범위 설정
import FinanceDataReader as fdr
# uv pip install finance-datareader
import matplotlib.pyplot as plt

# 한글 폰트 설정 (Windows 기준: 맑은 고딕, 깨짐 방지)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

#조회 시작
start=datetime.datetime(2023,2,19)
#조회 마감 날짜
end=datetime.datetime(2024,7,30)

# 구글: google finance => https://www.google.com/finance/?hl=ko
# 한국거래소 상장종목 전체
df_krx=fdr.StockListing('KRX') 
# KRX : Korea Exchang 한국 거래소(KOSPI, KOSDAQ, KONEX)정보 요청
#리스트 10개 출력
print(df_krx.head(10))

print(df_krx.index)
print(df_krx['Stocks'])
print(df_krx['Name'].head(10))
print(df_krx.iloc[0]) # 첫번째 종목의 정보
print(df_krx.describe())

print('-'*30)
print('-'*30)
# 미국 거래소 상장종목중 아마존 금융정보
df_amz = fdr.DataReader('AMZN',start,end)

print(df_amz.head(10))
print(df_amz.iloc[0]) # 첫번째 종목의 정보
print(df_amz.loc['2024-07-16'])
print(df_amz.describe())

print('-'*30)
print('-'*30)
# 미국 거래소 상장종목중 구글 금융정보
df_goog = fdr.DataReader('GOOG',start,end)

print(df_goog.head(10))
print(df_goog.iloc[0]) # 첫번째 종목의 정보
print(df_goog.loc['2024-07-16'])
print(df_goog.describe())

plt.figure(figsize=(14, 6))
plt.plot(df_amz.index, df_amz['Close'], label='Amazon (AMZN)', color='orange')
plt.plot(df_goog.index, df_goog['Close'], label='Google (GOOG)', color='blue')
plt.title('아마존 vs 구글 종가 추이 (2023.02 ~ 2024.07)')
plt.xlabel('날짜')
plt.ylabel('종가 (USD)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('amz_goog_close_compare.png', dpi=150)
plt.show()

# 2) 아마존 캔들스틱 느낌 - 고가/저가/종가 밴드
plt.figure(figsize=(14, 6))
plt.fill_between(df_amz.index, df_amz['Low'], df_amz['High'], alpha=0.2, color='orange', label='고가-저가 범위')
plt.plot(df_amz.index, df_amz['Close'], color='darkorange', label='종가')
plt.title('Amazon (AMZN) 주가 변동 범위')
plt.xlabel('날짜')
plt.ylabel('가격 (USD)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('amz_price_range.png', dpi=150)
plt.show()