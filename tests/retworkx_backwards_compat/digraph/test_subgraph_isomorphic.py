# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import unittest

import retworkx


class TestSubgraphIsomorphic(unittest.TestCase):
    def test_empty_subgraph_isomorphic_identical(self):
        g_a = retworkx.PyDiGraph()
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                self.assertTrue(retworkx.is_subgraph_isomorphic(g_a, g_a, id_order=id_order))

    def test_empty_subgraph_isomorphic(self):
        g_a = retworkx.PyDiGraph()
        g_b = retworkx.PyDiGraph()
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                self.assertTrue(retworkx.is_subgraph_isomorphic(g_a, g_b, id_order=id_order))

    def test_empty_subgraph_isomorphic_compare_nodes(self):
        g_a = retworkx.PyDiGraph()
        g_b = retworkx.PyDiGraph()
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                self.assertTrue(
                    retworkx.is_subgraph_isomorphic(
                        g_a, g_b, lambda x, y: x == y, id_order=id_order
                    )
                )

    def test_subgraph_isomorphic_identical(self):
        g_a = retworkx.PyDiGraph()
        nodes = g_a.add_nodes_from(["a_1", "a_2", "a_3"])
        g_a.add_edges_from([(nodes[0], nodes[1], "a_1"), (nodes[1], nodes[2], "a_2")])
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                self.assertTrue(retworkx.is_subgraph_isomorphic(g_a, g_a, id_order=id_order))

    def test_subgraph_isomorphic_mismatch_node_data(self):
        g_a = retworkx.PyDiGraph()
        g_b = retworkx.PyDiGraph()

        nodes = g_a.add_nodes_from(["a_1", "a_2", "a_3", "a_4"])
        g_a.add_edges_from(
            [
                (nodes[0], nodes[1], "a_1"),
                (nodes[1], nodes[2], "a_2"),
                (nodes[0], nodes[3], "a_3"),
            ]
        )

        nodes = g_b.add_nodes_from(["b_1", "b_2", "b_3"])
        g_b.add_edges_from([(nodes[0], nodes[1], "b_1"), (nodes[1], nodes[2], "b_2")])
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                self.assertTrue(retworkx.is_subgraph_isomorphic(g_a, g_b, id_order=id_order))

    def test_subgraph_isomorphic_compare_nodes_mismatch_node_data(self):
        g_a = retworkx.PyDiGraph()
        g_b = retworkx.PyDiGraph()

        nodes = g_a.add_nodes_from(["a_1", "a_2", "a_3", "a_4"])
        g_a.add_edges_from(
            [
                (nodes[0], nodes[1], "a_1"),
                (nodes[1], nodes[2], "a_2"),
                (nodes[0], nodes[3], "a_3"),
            ]
        )

        nodes = g_b.add_nodes_from(["b_1", "b_2", "b_3"])
        g_b.add_edges_from([(nodes[0], nodes[1], "b_1"), (nodes[1], nodes[2], "b_2")])
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                self.assertFalse(
                    retworkx.is_subgraph_isomorphic(
                        g_a, g_b, lambda x, y: x == y, id_order=id_order
                    )
                )

    def test_subgraph_isomorphic_compare_nodes_identical(self):
        g_a = retworkx.PyDiGraph()
        g_b = retworkx.PyDiGraph()

        nodes = g_a.add_nodes_from(["a_1", "a_2", "a_3", "a_4"])
        g_a.add_edges_from(
            [
                (nodes[0], nodes[1], "a_1"),
                (nodes[1], nodes[2], "a_2"),
                (nodes[0], nodes[3], "a_3"),
            ]
        )

        nodes = g_b.add_nodes_from(["a_1", "a_2", "a_3"])
        g_b.add_edges_from([(nodes[0], nodes[1], "a_1"), (nodes[1], nodes[2], "a_2")])
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                self.assertTrue(
                    retworkx.is_subgraph_isomorphic(
                        g_a, g_b, lambda x, y: x == y, id_order=id_order
                    )
                )

    def test_is_subgraph_isomorphic_nodes_compare_raises(self):
        g_a = retworkx.PyDiGraph()
        nodes = g_a.add_nodes_from(["a_1", "a_2", "a_3"])
        g_a.add_edges_from([(nodes[0], nodes[1], "a_1"), (nodes[1], nodes[2], "a_2")])

        def compare_nodes(a, b):
            raise TypeError("Failure")

        self.assertRaises(
            TypeError,
            retworkx.is_subgraph_isomorphic,
            (g_a, g_a, compare_nodes),
        )

    def test_subgraph_isomorphic_compare_edges_identical(self):
        g_a = retworkx.PyDiGraph()
        g_b = retworkx.PyDiGraph()

        nodes = g_a.add_nodes_from(["a_1", "a_2", "a_3", "a_4"])
        g_a.add_edges_from(
            [
                (nodes[0], nodes[1], "a_1"),
                (nodes[1], nodes[2], "a_2"),
                (nodes[0], nodes[3], "a_3"),
            ]
        )

        nodes = g_b.add_nodes_from(["a_1", "a_2", "a_3"])
        g_b.add_edges_from([(nodes[0], nodes[1], "a_1"), (nodes[1], nodes[2], "a_2")])
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                self.assertTrue(
                    retworkx.is_subgraph_isomorphic(
                        g_a,
                        g_b,
                        edge_matcher=lambda x, y: x == y,
                        id_order=id_order,
                    )
                )

    def test_subgraph_isomorphic_node_count_not_ge(self):
        g_a = retworkx.PyDiGraph()
        g_b = retworkx.PyDiGraph()

        nodes = g_a.add_nodes_from(["a_1", "a_2"])
        g_a.add_edges_from([(nodes[0], nodes[1], "a_1")])

        nodes = g_b.add_nodes_from(["a_0", "a_1", "a_3"])
        g_b.add_edges_from([(nodes[0], nodes[1], "a_1")])
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                self.assertFalse(retworkx.is_subgraph_isomorphic(g_a, g_b, id_order=id_order))

    def test_subgraph_isomorphic_edge_matcher(self):
        first = retworkx.PyDiGraph()
        first.extend_from_weighted_edge_list([(0, 1, "a"), (1, 2, "b"), (2, 0, "c")])
        second = retworkx.PyDiGraph()
        second.extend_from_weighted_edge_list([(0, 1, "a"), (1, 2, "b")])

        self.assertTrue(
            retworkx.is_subgraph_isomorphic(
                first, second, induced=False, edge_matcher=lambda x, y: x == y
            )
        )

    def test_subgraph_isomorphic_mismatch_edge_data_parallel_edges(self):
        first = retworkx.PyDiGraph()
        first.extend_from_weighted_edge_list([(0, 1, "a"), (0, 1, "f"), (1, 2, "b"), (2, 0, "c")])
        second = retworkx.PyDiGraph()
        second.extend_from_weighted_edge_list([(0, 1, "a"), (0, 1, "a"), (1, 2, "b")])

        self.assertFalse(
            retworkx.is_subgraph_isomorphic(
                first, second, id_order=True, edge_matcher=lambda x, y: x == y
            )
        )

    def test_non_induced_subgraph_isomorphic(self):
        g_a = retworkx.PyDiGraph()
        g_b = retworkx.PyDiGraph()

        nodes = g_a.add_nodes_from(["a_1", "a_2", "a_3"])
        g_a.add_edges_from(
            [
                (nodes[0], nodes[1], "a_1"),
                (nodes[1], nodes[2], "a_2"),
                (nodes[2], nodes[0], "a_3"),
            ]
        )

        nodes = g_b.add_nodes_from(["a_1", "a_2", "a_3"])
        g_b.add_edges_from([(nodes[0], nodes[1], "a_1"), (nodes[1], nodes[2], "a_2")])
        for id_order in [False, True]:
            with self.subTest(id_order=id_order, induced=True):
                self.assertFalse(
                    retworkx.is_subgraph_isomorphic(g_a, g_b, id_order=id_order, induced=True)
                )
            with self.subTest(id_order=id_order, induced=False):
                self.assertTrue(
                    retworkx.is_subgraph_isomorphic(g_a, g_b, id_order=id_order, induced=False)
                )

    def test_non_induced_grid_subgraph_isomorphic(self):
        g_a = retworkx.generators.directed_grid_graph(2, 2)
        g_b = retworkx.PyDiGraph()
        g_b.add_nodes_from([0, 1, 2, 3])
        g_b.add_edges_from_no_data([(0, 1), (2, 3)])

        self.assertFalse(retworkx.is_subgraph_isomorphic(g_a, g_b, induced=True))

        self.assertTrue(retworkx.is_subgraph_isomorphic(g_a, g_b, induced=False))

    def test_subgraph_vf2_mapping(self):
        graph = retworkx.generators.directed_grid_graph(10, 10)
        second_graph = retworkx.generators.directed_grid_graph(2, 2)
        mapping = retworkx.digraph_vf2_mapping(graph, second_graph, subgraph=True)
        self.assertEqual(next(mapping), {0: 0, 1: 1, 10: 2, 11: 3})

    def test_subgraph_vf2_all_mappings(self):
        graph = retworkx.generators.directed_path_graph(3)
        second_graph = retworkx.generators.directed_path_graph(2)
        mapping = retworkx.digraph_vf2_mapping(graph, second_graph, subgraph=True, id_order=True)
        self.assertEqual(next(mapping), {0: 0, 1: 1})
        self.assertEqual(next(mapping), {2: 1, 1: 0})

    def test_subgraph_vf2_mapping_vf2pp(self):
        graph = retworkx.generators.directed_grid_graph(3, 3)
        second_graph = retworkx.generators.directed_grid_graph(2, 2)
        mapping = retworkx.digraph_vf2_mapping(graph, second_graph, subgraph=True, id_order=False)
        self.assertEqual(next(mapping), {4: 0, 5: 1, 7: 2, 8: 3})

    def test_vf2pp_remapping(self):
        temp = retworkx.generators.directed_grid_graph(3, 3)

        graph = retworkx.PyDiGraph()
        dummy = graph.add_node(0)

        graph.compose(temp, dict())
        graph.remove_node(dummy)

        second_graph = retworkx.generators.directed_grid_graph(2, 2)
        mapping = retworkx.digraph_vf2_mapping(graph, second_graph, subgraph=True, id_order=False)
        self.assertEqual(next(mapping), {5: 0, 6: 1, 8: 2, 9: 3})

    def test_empty_digraph_subgraph_vf2_mapping(self):
        g_a = retworkx.PyDiGraph()
        g_b = retworkx.PyDiGraph()
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                mapping = retworkx.digraph_vf2_mapping(g_a, g_b, id_order=id_order, subgraph=True)
                self.assertEqual({}, next(mapping))
