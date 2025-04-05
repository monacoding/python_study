#시용목적
#특정 패턴의 문자열 찾기
#이메일, 전화번호, 날짜같은 형식 인식
#문자열 치환, 나누기 등

#1단계 re 로 문자열 안에서 찾기 
import re

test = "내 이메일은 hello@example.com입니다."

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

match = re.search(pattern, test)

if match :
    print("이메일 발견", match.group())
else :
    print("이메일이 없습니다.")
    
#2단계 정규표현식 기초 문법
# . : 아무 글자 1개 
# * : 0개 이상 반복
# + : 1개 이상 반복
# \d : 숫자 (0~9)
# \w : 단어 문자 (a-z, A-Z, 0-9,_)
# \s : 공백 문자 
# [a,b,c] : a,b,c 중 하나 
# [^a, b, c ] :a,b,c 외 문자
# ^,$ : 시작/끝을 나타냄 

#3단계 문자열 바꾸기 
text = "나는 010-1234-5678로 연락해요"
new_text = re.sub (r"\d{3}-\d{4}-\d{4}", "[전화번호 숨김]",text)
print(new_text)

sample = """
고객 리스트:
김철수: chulsoo99@gmail.com
박영희: younghee88@naver.com
연락처: 010-1234-5678, 010-8765-4321
"""

phone_pattern = r"010-\d{4}-\d{4}"
# 이름 패턴 (한글 이름 2-3글자)
name_pattern = r"([가-힣]{2,3}):"

email = re.findall(pattern, sample)

print(email)

phone= re.findall(phone_pattern, sample)

print(phone)
    
name= re.findall(name_pattern, sample)

print(name)
    
