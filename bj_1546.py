# 문제번호: 1546
# 평균 구하기
# url: https://www.acmicpc.net/problem/1546
# 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# 2022.06.19.~2022.07.01.

#########################
# [문제]
# 세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다.
# 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
# 예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
# 세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.
# 
# - 첫째 줄에 시험 본 과목의 개수 N이 주어진다. 이 값은 1000보다 작거나 같다.
# - 둘째 줄에 세준이의 현재 성적이 주어진다. 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.
#########################


# be about to revise soon... Below is a prior solution.


import random
N = input('과목 수:')
score = []
new_score = []
sum = 0
for i in range(int(N)):
	score.append(random.randint(0,100))
for i in range(int(N)):
	new_score.append(round(score[i]/max(score)*100, 2))
	sum += new_score[i]
print('기존 과목별 점수는 {}점이며,\n새로운 과목별 점수는 {}접이다.'.format(score, new_score))
print('세준이의 새로운 평균은 {}점입니다.'.format(int(sum/len(new_score))))


# fin.