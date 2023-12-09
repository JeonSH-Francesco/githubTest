from datetime import datetime

# 현재 시간을 가져옵니다.
current_time = datetime.now()

# 시간을 원하는 형식으로 포맷팅합니다.
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 결과를 출력합니다.
print("현재 시간:", formatted_time)
