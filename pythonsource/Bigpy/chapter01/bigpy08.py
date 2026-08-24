import pandas as pd

#계절별 서울/부산 지역 온도 데이터 정의
temperatures = [[3.3,34.5,14.2,-10],[7.1,32.1,10.7,2]]
seasons = ['spring', 'summer','fall','winter']
regions = ['seoul','pusan']

data = pd.DataFrame(temperatures, index=regions, columns=seasons)

print(data)
print('-'*10)

print(data.index)
print(data.columns)
print(data.values)