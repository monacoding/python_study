import pandas as pd
import platform

#1단계 딕셔너리 만들기 
data = {
    '이름': ['철수','영희','민수'],
    '나이': [23,21,25],
    '성별': ['남','여','남']
    
}

df = pd.DataFrame(data)

print(df)

#2단계 데이터 접근 & 필터링
print(df['이름'])

#특정 조건에 해당하는 행
print(df[df['나이']>22])

#성별이 '남'인 데이터만 필터링
print(df[df['성별'] == '남'])

# 데이터프레임을 CSV 파일로 저장
if platform.system() == 'Darwin':  # macOS
    df.to_csv('person_data.csv', index=False, encoding='utf-8-sig')
else:  # Windows
    df.to_csv('person_data.csv', index=False, encoding='cp949')
print("CSV 파일이 저장되었습니다.")

#3단계 파일 앍고 쓰기 
#CSV 파일 읽기
#df = pd.read_csv('dd.csv')

#저장하기 
#df.to_csv ('결고.csv',index = False)

