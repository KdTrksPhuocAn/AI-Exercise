from collections import deque


def sliding_window_max(num_list, k):
    result = []
    queue = deque()

    for index, value in enumerate(num_list):
        if queue and queue[0] <= index - k:
            queue.popleft()

        while queue and num_list[queue[-1]] < value:
            queue.pop()

        queue.append(index)

        if index >= k - 1:
            result.append(num_list[queue[0]])

    return result


print('s:', sliding_window_max(
    num_list=[3, 4, 5, 1, -44, 5, 10, 12, 33, 1], k=3))
