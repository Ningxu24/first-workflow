import heapq


class ProductTracker:
    """
    A data structure that tracks pending orders for products and supports
    efficient retrieval of the product with the most pending orders.

    Data structure design:
    - `self.pending`: a dict mapping product_id -> current pending order count.
      Provides O(1) lookup and update for add_order, process_order, get_pending.
    - `self.heap`: a max-heap (implemented as a min-heap with negated counts)
      storing (-count, product_id) entries. Uses lazy deletion so that stale
      entries are skipped in top_product without requiring explicit removal.

    Time complexity:
    - add_order:     O(log n) amortized  (heap push)
    - process_order: O(1)                (dict update only; heap updated lazily)
    - get_pending:   O(1)                (dict lookup)
    - top_product:   O(log n) amortized  (lazy cleanup of stale heap entries)
    """

    def __init__(self):
        # Maps each product_id to its current number of pending orders
        self.pending = {}
        # Max-heap stored as (-count, product_id) tuples
        self.heap = []

    def add_order(self, product_id):
        """Add one pending order for product_id."""
        self.pending[product_id] = self.pending.get(product_id, 0) + 1
        # Push the updated count onto the heap
        heapq.heappush(self.heap, (-self.pending[product_id], product_id))

    def process_order(self, product_id):
        """
        Mark one pending order for product_id as processed.
        The heap is not updated immediately; stale entries are removed lazily
        in top_product to keep process_order at O(1).
        """
        if self.pending.get(product_id, 0) > 0:
            self.pending[product_id] -= 1

    def get_pending(self, product_id):
        """Return the current number of pending orders for product_id."""
        return self.pending.get(product_id, 0)

    def top_product(self):
        """
        Return the product_id with the largest number of pending orders.
        If multiple products share the maximum, any one of them may be returned.
        Returns None if there are no pending orders.

        Stale heap entries (whose stored count no longer matches self.pending)
        are discarded until a valid entry is found.
        """
        while self.heap:
            neg_count, product_id = self.heap[0]
            # Check whether this heap entry is still current and count is positive
            if -neg_count == self.pending.get(product_id, 0) and -neg_count > 0:
                return product_id
            # Entry is stale (count has decreased); discard and continue
            heapq.heappop(self.heap)
        return None


# ---------------------------------------------------------------------------
# Example usage
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    tracker = ProductTracker()

    tracker.add_order("A")
    tracker.add_order("A")
    tracker.add_order("B")
    tracker.add_order("C")
    tracker.add_order("C")
    tracker.add_order("C")

    print("Pending A:", tracker.get_pending("A"))  # 2
    print("Pending B:", tracker.get_pending("B"))  # 1
    print("Pending C:", tracker.get_pending("C"))  # 3
    print("Top product:", tracker.top_product())   # C

    tracker.process_order("C")
    tracker.process_order("C")
    tracker.process_order("C")

    print("After processing all C orders:")
    print("Pending C:", tracker.get_pending("C"))  # 0
    print("Top product:", tracker.top_product())   # A
