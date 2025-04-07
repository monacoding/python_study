import matplotlib.pyplot as plt
import platform
import pandas as pd

# macOS 한글 폰트 설정
if platform.system() == 'Darwin':
    plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

# 그래프 그리기
날짜= ['월','화','수','목','금']
매출= [100,200,250,300,150]

plt.plot(날짜, 매출)
plt.title("요일별 매출 추이")
plt.xlabel("요일")
plt.ylabel("매출(만원)")
plt.grid(True)
plt.show()

plt.bar(날짜, 매출)
plt.title("요일별 매출 비교")
plt.xlabel("요일")
plt.ylabel("매출 (만원)")
plt.show()

제품 = ['A','B','C','D']
판매비율 = [40,30,20,10]

plt.pie(판매비율, labels=제품, autopct='%1.1f%%')
plt.title("제품별 판매 비율")
plt.show()

#pandas + matplotlib 연동

data = {
    '요일': ['월', '화', '수', '목', '금'],
    '매출': [100, 200, 250, 300, 150]
}

df=pd.DataFrame(data)

df.plot(x='요일', y='매출', kind='line', title='pandas로 선 그래프', legend=False)
plt.ylabel("매출 (만원)")        
plt.grid(True)
plt.show()
         