from paa191t1.dijkstra.datastructs.fibonacci_heap import FibHeap
from paa191t1.tests.dijkstra.test_dijkstra import TestDijkstraBase


class TestDijkstraFibHeap(TestDijkstraBase):

    def setUp(self):
        self.struct = FibHeap()
