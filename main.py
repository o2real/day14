from art import logo,vs
from game_data import data
import random
from replit import clear

def format_data(account):
  """데이터를 정렬해서 출력"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}."

def check_answer(guess, a_followers, b_followers):
  """맞는지 확인하려면 if구문 사용하기 """
  if a_followers > b_followers :
    return guess == "a"
  else:
    return guess == "b"

#display art
print(logo)
score = 0 
game_should_continue = True

account_b = random.choice(data)

# 게임을 반복하게 만들기
while game_should_continue :

  # Generate a random account from the game data. 

  # 포지션 B를 A로 올리기
  account_a = account_b
  account_b = random.choice(data)

  while account_a == account_b :
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}.")

  print(vs)

  print(f"Against B: {format_data(account_b)}.")


  # 사용자한테 추측한거 물어보기
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  # 사용자가 답을 맞췄는지 확인 
  ##각각의 팔로워 수를 확인
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]

  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  # 매 라운드마다 초기화하기 클리어 스크린  
  clear()
  print(logo)
  # 사용자에게 사용자의 추측에 대한 피드백 주기
  # 점수 저장
  if is_correct :
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    print(f"Sorry, that' wrong Final score: {score}.")
    game_should_continue = False


