import random
from flask import Flask, render_template




app = Flask(__name__)


GOOGLE_DRIVE_LINK = "https://drive.google.com/drive/folders/1aWweDKCRF_vrehtr3JQlUwTCTA9Llznv"





@app.route('/')
def hello():
  return '''<!doctype html>
<html>
  <body>
      <h2><a href="/download">유료 스팀게임 무료 다운로드</a></h2>
      <ol>
          <h1>무려 유료 스팀게임 무료로 다운로드 가능!</h1>
          <h1>복돌 방지 시스템에 의해 막힐 확률 0%!!</h1>
          <h1>지금 바로 다운로드!!!</h1>
      </ol>
      
      <!-- 이미지 표시 -->
      <img src="/static/img.jpg" width="1680">
      
      <h6>본 사이트는 다운로드로 일어나는 모든 불이익에 대해 책임지지 않습니다</h6>
      
  </body>
</html>
'''



@app.route('/ran')
def ran():
  return '랜덤 숫자 추출 : <strong>'+str(random.random())+'</strong>'


@app.route('/read/<id>')
def read(id):
  print(id)
  return 'id 값은 바로바로 : ' + id


# 사용자 요청에 따라 수정된 /download 경로 (선택 태그 제거)
@app.route('/download')
def index():
  # 요청하신 대로 최소한의 HTML에 클릭 가능한 링크를 추가합니다.
  # 불필요한 를 제거했습니다.
  return f'''<!doctype html>
<html>
  <body>
      <h1>즉시 연결하고 다운로드하세요!<h1>
      <h1><a href="{GOOGLE_DRIVE_LINK}" target="_blank">{GOOGLE_DRIVE_LINK}</a></h1>
  </body>
</html>
'''


@app.route('/web')
def index3():
  # 템플릿으로 변수 전달(예시)
  return render_template('index.html')






if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)



