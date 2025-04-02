import os

#현재 작업 디렉토리 확인
print(os.getcwd())
#디렉터리 내 파일 목록 출력
print(os.listdir('.'))
#디렉터리 만들기
#os.mkdir('새폴더')
#경로 합치기 
path = os.path.join('새폴더','파일.txt')
print(path)

#환경 변수 만들기 
print(os.environ.get('HOME'))

#현재 작업중인 디렉 토리 확인

current_dir = os.getcwd()
print("현재 작업중인 디렉토리",current_dir)

#os.getcwd() 는 "get current working directory의 약자임 ", 현재 작업중인 디렉토리를 반환

#새 디렉토리 만들기
new_dir_name = "연습폴더"

#디렉토리가 없다면 새로 생성
if not os.path.exists(new_dir_name) :
    os.mkdir(new_dir_name)
    print(f"'{new_dir_name}'디렉토리를 생성했습니다.")
else :
    print(f"'{new_dir_name}'디렉토리가 존재 합니다")
    
#경로 합치기 
file_name = "연습파일.txt"
file_path = os.path.join(new_dir_name, file_name)

print("생성될 파일 경로 ",file_name)

#디렉토리 안 파일 보기 
print(f"'{new_dir_name}'안에 파일 목록")
print(os.listdir(new_dir_name))

#디렉토리 안의 모든 파일 이름 출력 + 확장자 필터링 
for file in os.listdir(new_dir_name):
    if file.endswith('.txt'):
        print("텍스트 파일 발견",file)
        
#파일이 있는지 확인하고 파일 생성하기 
file_path = os.path.join(new_dir_name,"연습파일.txt")

if not os.path.exists(file_path):
    with open(file_path,'w') as f:
        f.write("이것은 os 연습입니다.\n")
    print("파일을 생성했습니다.")
else: 
    print("파일이 존재 합니다. ")
    
#전체 디렉토리 탐색
for root, dirs, files in os.walk(new_dir_name):
    print("현재 경로", root)
    print("디렉토리",dirs)
    print("파일",files)
    
    