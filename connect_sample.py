import wda

# 디바이스 연결
c = wda.Client()
print(c.status())

# 홈버튼 클릭
c.home()

# 수행결과 확인
c.healthcheck()