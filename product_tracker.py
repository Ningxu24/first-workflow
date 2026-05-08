import heapq


class ProductTracker:
    """Track pending orders per product and support efficient max-pending queries.

    Data structures:
      - self.pending (dict): maps product_id -> current pending order count.
        Provides O(1) lookup and update.
      - self.heap (list): max-heap implemented as a min-heap with negated counts.
        Each entry is (-count, product_id). The heap may contain stale entries;
        they are removed lazily inside top_product().

    Complexity:
      add_order     – O(log n)
      process_order – O(log n)
      get_pending   – O(1)
      top_product   – amortized O(log n)
    """

    def __init__(self):
        self.pending = {}   # product_id -> current pending count
        self.heap = []      # max-heap stored as (-count, product_id)

    def add_order(self, product_id, quantity):
        """Add *quantity* pending orders for *product_id*.

        Raises ValueError if quantity is negative.
        """
        if quantity < 0:
            raise ValueError("quantity must be non-negative")
        current = self.pending.get(product_id, 0)
        new_value = current + quantity
        self.pending[product_id] = new_value
        heapq.heappush(self.heap, (-new_value, product_id))

    def process_order(self, product_id, quantity):
        """Process (fulfill) *quantity* orders for *product_id*.

        Pending count never drops below zero.
        Raises ValueError if quantity is negative.
        """
        if quantity < 0:
            raise ValueError("quantity must be non-negative")
        current = self.pending.get(product_id, 0)
        new_value = max(0, current - quantity)
        if new_value == 0:
            self.pending.pop(product_id, None)
        else:
            self.pending[product_id] = new_value
        heapq.heappush(self.heap, (-new_value, product_id))

    def get_pending(self, product_id):
        """Return the current number of pending orders for *product_id*."""
        return self.pending.get(product_id, 0)

    def top_product(self):
        """Return the product_id with the largest number of pending orders.

        If multiple products share the maximum count, any one may be returned.
        Returns None if no products have pending orders.
        Uses lazy deletion to skip heap entries that have become stale.
        """
        while self.heap:
            neg_count, product_id = self.heap[0]
            current = self.pending.get(product_id, 0)
            if -neg_count == current and current > 0:
                return product_id
            heapq.heappop(self.heap)
        return None
