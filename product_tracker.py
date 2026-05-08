import heapq


class ProductTracker:
    """
    Tracks pending orders per product and supports efficient retrieval
    of the product with the most pending orders.

    Data structure design:
    - self.pending: dict mapping product_id -> current pending order count.
      Provides O(1) lookup and update.
    - self.heap: max-heap (simulated via negated counts in Python's min-heap)
      storing (-count, product_id) tuples.  Enables O(log n) push and
      amortised O(log n) top_product queries via lazy deletion.
    """

    def __init__(self):
        self.pending = {}   # product_id -> current pending count
        self.heap = []      # max-heap as (-count, product_id)

    def add_order(self, product_id, quantity):
        """Add `quantity` pending orders for `product_id`.  O(log n)."""
        current = self.pending.get(product_id, 0)
        new_count = current + quantity
        self.pending[product_id] = new_count
        heapq.heappush(self.heap, (-new_count, product_id))

    def process_order(self, product_id, quantity):
        """Process (fulfil) `quantity` orders for `product_id`.
        Pending count never drops below zero.  O(log n)."""
        current = self.pending.get(product_id, 0)
        new_count = max(0, current - quantity)
        self.pending[product_id] = new_count
        heapq.heappush(self.heap, (-new_count, product_id))

    def get_pending(self, product_id):
        """Return the current pending order count for `product_id`.  O(1)."""
        return self.pending.get(product_id, 0)

    def top_product(self):
        """Return the product_id with the largest pending order count.
        Returns None if no products have been tracked.

        Uses lazy deletion: stale heap entries (whose count no longer matches
        the hash table) are discarded until a valid entry is found.
        Amortised O(log n) per call."""
        while self.heap:
            neg_count, product_id = self.heap[0]
            # Check whether this heap entry still reflects the current count.
            if -neg_count == self.pending.get(product_id, 0):
                return product_id
            heapq.heappop(self.heap)   # discard stale entry
        return None
