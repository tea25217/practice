import heapq

N, L = map(int, input().split())
K = int(input())
a = list(map(int, input().split()))

min_dist = 10 ** 9
min_selected_section = 100001
current_section_start = -1
section_dist = [0] * (K + 1)
selected = []
selected_section = []
heapq.heapify(selected_section)  # 中身: (区間の距離, (start, end))


# TODO
def calc_section_dist(start, end):
    pass


current_section_start = K - 1

for i in range(N):
    # まずK個選択する
    if len(selected) < K:
        selected.append(i)
        if i == 0:
            min_dist = a[0]
            min_selected_section = 0
            section_dist[0] = a[0]
            heapq.heappush(selected_section, (a[i], (-1, 0)))
        else:
            min_dist = min(min_dist, a[i - 1] - a[i])
            section_dist[i] = calc_section_dist(i - 1, i)
            min_selected_section min(min_selected_section, section_dist[i])
            heapq.heappush(selected_section, (section_dist[i], (i - 1, i)))
        continue

    # 次の区間がmin_distより長ければ選択区間を更新する
    if calc_section_dist(current_section_start, a[i]) < min_dist:
        pass
