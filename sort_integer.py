import unittest
from typing import List


def split_to_array(num) -> List[int]:
    try:
        arr = [int(x) for x in str(num)]
        print(f'result of split {arr}')
        return arr
    except Exception:
        return []


# def descending_order(num) -> int:
#     return join_list(merge_sort(split_to_array(num)))

def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))


def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        left_arr_idx = 0
        right_arr_idx = 0
        current_index = 0

        # loop as long as we are within bounds of both arrays
        while left_arr_idx < len(left_arr) and right_arr_idx < len(right_arr):
            # left smaller than right
            if left_arr[left_arr_idx] > right_arr[right_arr_idx]:
                arr[current_index] = left_arr[left_arr_idx]
                left_arr_idx += 1
            # right smaller than left
            else:
                arr[current_index] = right_arr[right_arr_idx]
                right_arr_idx += 1

            current_index += 1

        # check for leftovers
        while left_arr_idx < len(left_arr):
            arr[current_index] = left_arr[left_arr_idx]
            left_arr_idx += 1
            current_index += 1

        while right_arr_idx < len(right_arr):
            arr[current_index] = right_arr[right_arr_idx]
            right_arr_idx += 1
            current_index += 1
        print(f'merge sort complete - result {arr}')
    return arr


def join_list(arr):
    try:
        return int("".join([str(x) for x in arr]))
    except Exception as e:
        print(f'join list failed with Exception {e}')
        return None


class TestDescendingOrder(unittest.TestCase):

    def test_function(self):
        self.assertEqual(descending_order(0), 0)
        self.assertEqual(descending_order(51), 51)
        self.assertEqual(descending_order(123456789), 987654321)

    def test_split_array(self):
        self.assertEqual(split_to_array(5), [5])
        self.assertEqual(split_to_array(56), [5, 6])
        self.assertEqual(split_to_array(None), [])
        self.assertEqual(split_to_array(0), [0])

    def test_merge_sort(self):
        self.assertEqual(merge_sort([3, 1]), [3, 1])
        self.assertEqual(merge_sort([3, 77, 3, 1]), [77, 3, 3, 1])

    def test_join_list(self):
        self.assertEqual(join_list([3, 1]), 31)
        self.assertEqual(join_list([3, 0, 33, 1]), 30331)
        self.assertEqual(join_list([]), None)
