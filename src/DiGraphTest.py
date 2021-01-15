import unittest
from DiGraph import DiGraph


class DiGraphTest(unittest.TestCase):
    def test_v_size(self):
        g = DiGraph()
        pos = 4.1, 5.4, 6.2
        for n in range(5):
            g.add_node(n, pos)
        self.assertEqual(g.v_size(), 5)
        g.remove_node(1)
        self.assertEqual(g.v_size(), 4)

    def test_e_size(self):
        g = DiGraph()
        pos = 4.1, 5.4, 6.2
        for n in range(5):
            g.add_node(n, pos)
        g.add_edge(0, 4, 1)
        g.add_edge(2, 0, 3.2)
        g.add_edge(3, 2, 4.2)
        g.add_edge(1, 4, 5.2)
        self.assertEqual(g.e_size(),4)
        g.remove_edge(1, 4)
        self.assertEqual(g.e_size(),3)

    def test_get_mc(self):
        g = DiGraph()
        pos = 4.1, 5.4, 6.2
        for n in range(5):
            g.add_node(n, pos)
        g.add_edge(0, 4, 1)
        g.add_edge(2, 0, 3.2)
        g.add_edge(3, 2, 4.2)
        g.add_edge(1, 4, 5.2)
        self.assertEqual(g.get_mc(), 9)
        g.remove_edge(1, 4)
        self.assertEqual(g.get_mc(), 10)
        g.remove_node(0)
        self.assertEqual(g.get_mc(),11)

    def test_add_node(self):
        g = DiGraph()
        pos = 4.1, 5.4, 6.2
        for n in range(5):
            g.add_node(n, pos)
        self.assertEqual(g.v_size(), 5)
        g.remove_node(3)
        self.assertEqual(g.v_size(), 4)
        b = g.__contains__(2)
        self.assertTrue(b)

    def test_remove_node(self):
        g = DiGraph()
        pos = 4.1, 5.4, 6.2
        for n in range(5):
            g.add_node(n, pos)
        self.assertEqual(g.v_size(), 5)
        g.remove_node(2)
        self.assertEqual(g.v_size(), 4)
        b = g.__contains__(2)
        self.assertFalse(b)


if __name__ == '__main__':
    unittest.main()
