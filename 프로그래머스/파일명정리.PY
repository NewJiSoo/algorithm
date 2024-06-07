import re


def parse_file(file):
    # 정규 표현식을 사용하여 HEAD, NUMBER, TAIL로 분리
    match = re.match(r'([a-zA-Z\s.-]+)(\d{1,5})(.*)', file)
    if match:
        return match.groups()
    else:
        return (file, '', '')  # 매칭이 안 되면 원래 파일명을 그대로 반환


def solution(files):
    parsed_files = [parse_file(file) for file in files]

    # 정렬 기준:
    # 1. HEAD를 대소문자 구분 없이 사전 순으로 정렬
    # 2. NUMBER를 숫자 순으로 정렬
    # 3. 원래 순서를 유지
    sorted_files = sorted(parsed_files, key=lambda x: (
        x[0].lower(), int(x[1]), files.index(''.join(x))))

    # 정렬된 파일명 반환
    return [''.join(file) for file in sorted_files]


# 예제 입력
files1 = ["img12.png", "img10.png", "img02.png",
          "img1.png", "IMG01.GIF", "img2.JPG"]
files2 = ["F-5 Freedom Fighter", "B-50 Superfortress",
          "A-10 Thunderbolt II", "F-14 Tomcat"]

# 정렬된 결과 출력
# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
print(solution(files1))
# ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
print(solution(files2))
