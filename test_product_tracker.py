import unittest
from product_tracker import ProductTracker


class TestProductTracker(unittest.TestCase):

    def setUp(self):
        self.tracker = ProductTracker()

    # ------------------------------------------------------------------ #
    # get_pending                                                          #
    # ------------------------------------------------------------------ #

    def test_get_pending_unknown_product_returns_zero(self):
        self.assertEqual(self.tracker.get_pending("A"), 0)

    def test_get_pending_after_add_order(self):
        self.tracker.add_order("A", 5)
        self.assertEqual(self.tracker.get_pending("A"), 5)

    def test_get_pending_after_multiple_add_orders(self):
        self.tracker.add_order("A", 3)
        self.tracker.add_order("A", 4)
        self.assertEqual(self.tracker.get_pending("A"), 7)

    # ------------------------------------------------------------------ #
    # process_order                                                        #
    # ------------------------------------------------------------------ #

    def test_process_order_reduces_pending(self):
        self.tracker.add_order("B", 10)
        self.tracker.process_order("B", 4)
        self.assertEqual(self.tracker.get_pending("B"), 6)

    def test_process_order_does_not_go_below_zero(self):
        self.tracker.add_order("B", 3)
        self.tracker.process_order("B", 10)
        self.assertEqual(self.tracker.get_pending("B"), 0)

    def test_process_order_on_unknown_product(self):
        # Processing an unknown product should not raise and keeps count at 0.
        self.tracker.process_order("Z", 5)
        self.assertEqual(self.tracker.get_pending("Z"), 0)

    # ------------------------------------------------------------------ #
    # top_product                                                          #
    # ------------------------------------------------------------------ #

    def test_top_product_empty_tracker_returns_none(self):
        self.assertIsNone(self.tracker.top_product())

    def test_top_product_single_product(self):
        self.tracker.add_order("A", 7)
        self.assertEqual(self.tracker.top_product(), "A")

    def test_top_product_returns_product_with_most_pending(self):
        self.tracker.add_order("A", 5)
        self.tracker.add_order("B", 10)
        self.tracker.add_order("C", 3)
        self.assertEqual(self.tracker.top_product(), "B")

    def test_top_product_updates_after_process_order(self):
        self.tracker.add_order("A", 10)
        self.tracker.add_order("B", 6)
        # Process most of A's orders so B becomes the top.
        self.tracker.process_order("A", 8)
        self.assertEqual(self.tracker.top_product(), "B")

    def test_top_product_tie_returns_one_of_the_tied_products(self):
        self.tracker.add_order("X", 5)
        self.tracker.add_order("Y", 5)
        result = self.tracker.top_product()
        self.assertIn(result, {"X", "Y"})

    def test_top_product_after_all_processed_to_zero(self):
        self.tracker.add_order("A", 3)
        self.tracker.process_order("A", 3)
        # All pending counts are zero; any product (or None) is acceptable,
        # but if a product is returned its pending count must be 0.
        result = self.tracker.top_product()
        if result is not None:
            self.assertEqual(self.tracker.get_pending(result), 0)

    def test_top_product_consistent_after_many_updates(self):
        products = ["P1", "P2", "P3", "P4"]
        for p in products:
            self.tracker.add_order(p, 1)
        self.tracker.add_order("P3", 9)   # P3 now has 10
        self.tracker.add_order("P1", 4)   # P1 has 5
        self.tracker.process_order("P3", 7)  # P3 now has 3
        # P1 (5) should be the top.
        self.assertEqual(self.tracker.top_product(), "P1")


if __name__ == "__main__":
    unittest.main()
