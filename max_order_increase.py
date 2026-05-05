def max_crossing_sum(arr, left, mid, right):
    """Return the maximum subarray sum that crosses the midpoint."""
    # Left suffix maximum
    left_sum = float('-inf')
    total = 0
    for i in range(mid, left - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total

    # Right prefix maximum
    right_sum = float('-inf')
    total = 0
    for i in range(mid + 1, right + 1):
        total += arr[i]
        if total > right_sum:
            right_sum = total

    return left_sum + right_sum


def max_order_increase(arr, left=None, right=None):
    """Return the maximum contiguous subarray sum using divide and conquer."""
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1

    # Base case: single element
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    left_max = max_order_increase(arr, left, mid)
    right_max = max_order_increase(arr, mid + 1, right)
    cross_max = max_crossing_sum(arr, left, mid, right)

    return max(left_max, right_max, cross_max)


if __name__ == "__main__":
    orders_change = [4, -2, 3, -1, 5, -3]
    print(max_order_increase(orders_change))  # Expected output: 9
