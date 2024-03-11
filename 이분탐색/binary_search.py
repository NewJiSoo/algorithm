def binary_search(start, end, target, array):
    while start <= end:           # 엔드가 클때 동안 반복, 스타트가 엔드보다 클 때 종료
        mid = (start + end) // 2  # 중앙값

        if array[mid] == target:
            return mid
        elif target < array[mid]:  # 타켓이 중간값보다 작으면 엔드 값을 줄임
            end = mid-1            # mid 값이 계속 움직이도록 조정
        else:                      # 타켓이 중간값보다 크면 스타트 값을 높임
            start = mid+1          # mid 값이 계속 움직이도록 조정
            # 무한 루프에 빠지지 않도록 조정하는 것임
    return None


array = [1, 2, 3, 4, 5]
target = 5
# 최소값을 구할때는 start , 최대값을 구할때는 end
result = binary_search(0, len(array)-1, target, array)
print(result)
