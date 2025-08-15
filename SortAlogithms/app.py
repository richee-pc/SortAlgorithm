import streamlit as st
import streamlit.components.v1 as components
import os

# Streamlit 페이지 설정
st.set_page_config(layout="wide", page_title="정렬 알고리즘 시뮬레이터")

# HTML 파일의 경로를 지정합니다.
# 이 파일을 Streamlit 앱과 같은 디렉토리에 두는 것이 가장 간단합니다.
# 예를 들어, 'index.html'이라는 이름으로 저장했다고 가정합니다.
# 실제 배포 시에는 파일 이름이 '정렬 알고리즘 교육용 웹 페이지 (최종 업데이트).html'일 수 있으므로,
# 해당 이름을 'index.html'로 변경하여 사용하시거나 아래 파일명을 수정해주세요.
HTML_FILE_PATH = "index.html" # 여기에 실제 HTML 파일 이름을 넣어주세요 (예: "sorting_algorithms.html")

# HTML 파일을 읽어오는 함수
def load_html_file(file_path):
    # 파일이 존재하는지 확인
    if not os.path.exists(file_path):
        st.error(f"Error: HTML file not found at '{file_path}'")
        st.stop() # 파일이 없으면 앱 실행 중지
    
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return html_content

st.title("정렬 알고리즘 시뮬레이터 🧑‍💻")
st.write("다양한 정렬 알고리즘의 동작을 시뮬레이션을 통해 직접 확인하고 배워보세요!")

# HTML 콘텐츠 로드
html_content = load_html_file(HTML_FILE_PATH)

# Streamlit 앱 내에 HTML 콘텐츠를 임베드합니다.
# height와 scrolling 속성은 필요에 따라 조절할 수 있습니다.
components.html(html_content, height=1000, scrolling=True)

st.markdown("---")
st.write("질문이 있으시면 언제든지 문의해주세요!")

