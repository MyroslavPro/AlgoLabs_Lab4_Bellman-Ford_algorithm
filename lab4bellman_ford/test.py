import unittest
from lab4bellman_ford.bellman_ford import Graph


class TestBellmanFord(unittest.TestCase):
    def test_raise_exception(self):
        test_graph = Graph()
        test_graph.add_to_the_graph(1, 2, 3)
        test_graph.add_to_the_graph(2, 3, 5)
        test_graph.add_to_the_graph(3, 4, -2)
        test_graph.add_to_the_graph(4, 1, 4)
        test_graph.add_to_the_graph(1, 3, -7)
        test_graph.add_to_the_graph(2, 4, -5)
        with self.assertRaises(Exception) as context:
            test_graph.relaxation()
        self.assertTrue("Graph has a negative-weight cycle" in str(context.exception), "Exception isn't matching")

    def test_input1(self):
        test_graph = Graph()
        test_graph.add_to_the_graph(1, 2, 3)
        test_graph.add_to_the_graph(2, 3, 5)
        test_graph.add_to_the_graph(3, 4, -2)
        test_graph.add_to_the_graph(4, 1, -1)
        test_graph.relaxation()
        self.assertEqual(test_graph.print_all_distances(), {1: 0, 2: 3, 3: 8, 4: 6})

    def test_input2(self):
        test_graph = Graph()
        test_graph.add_to_the_graph(4, 2, 1)
        test_graph.add_to_the_graph(2, 5, 4)
        test_graph.add_to_the_graph(2, 11, 3)
        test_graph.add_to_the_graph(11, 7, -2)
        test_graph.add_to_the_graph(7, 5, -2)
        test_graph.relaxation()
        self.assertEqual(test_graph.print_all_distances(), {4: 0, 2: 1, 5: 0, 11: 4, 7: 2})

    def test_input3(self):
        test_graph = Graph()
        test_graph.add_to_the_graph(1, 2, 3)
        test_graph.add_to_the_graph(2, 3, 5)
        test_graph.add_to_the_graph(7, 4, -2)
        test_graph.add_to_the_graph(8, 4, 4)
        test_graph.add_to_the_graph(2, 7, -1)
        test_graph.relaxation()
        self.assertEqual(test_graph.print_all_distances(), {1: 0, 2: 3, 3: 8, 7: 2, 4: 0, 8: float("inf")})
