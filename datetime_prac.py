import datetime

# 1단계 현재 날짜와 시간 
# 현재 날짜와 시간
now = datetime.datetime.now()
print("현재 시간:", now)

# 오늘 날짜만
today = datetime.date.today()
print("오늘 날짜:", today)

#2단계 날짜 직접 만들기 
custom_date = datetime.date(2025,1,1)
print( "지정한날쨰" ,custom_date)

#3단계 날짜 계산 하기 

delta = datetime.timedelta(days=3)
future = today + delta 
print ("3일뒤",future)

#7일전
past = today - datetime.timedelta(days = 7)
print("7일전",past)

#4단계 문자열 날짜 변환
date_str = "2025-04-02"
parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
print("문자열 -> 날짜", parsed_date)

#날짜를 문자열로 바꾸기
formatted = parsed_date.strftime("%Y년 %m월 %d일")
print("날짜 -> 문자열",formatted)

weekday = today.weekday()
weekdays = ['월','화','수','목','금','토','일']
print("오늘은", weekdays[weekdays],"요일입니다.")