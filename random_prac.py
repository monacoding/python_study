import random 

#random.random () 함수 : 0.0 이상 1.0 미만의 float 값
print("무작위float",random.random()) 

#random.randint(a,b) - a이상, b 이하의 정수
print("무작위 정수 (1~10):", random.randint(1,10))

#random.choice(seq) - 시컨스에서 무작위 요소 하나 선택
colors = ['red','green', 'blue', 'yellow']
print("선택된 색상",random.choice(colors))

#random.sample(seq,k) - 중복없이 k개 선택
lotto = random.sample(range(1,46),6)
print("로또 번호",sorted(lotto))

#random.shuffle(list) - 리스트 순서를 섞음 (제자리에서 변경)
cards = ['A', 'B', 'C', 'D']
random.shuffle(cards)
print("섞인 카드", cards)

#random.seed(x) - 결과를 고정시킴 (재현 가능)
random.seed(1234)
print("고정된 난수",random.random())