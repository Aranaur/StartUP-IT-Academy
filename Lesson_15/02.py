from _02_tree import Node
import pytest

def test_list_insert_true():
    try:
        root_1 = Node(10)
        root_1.list_insert([8, 15])
        root_2 = Node(8)
        assert root_1.min_value() == root_2.min_value()
        print("test_list_insert_true PASSED")
    except:
        print("test_list_insert_true FAILED")


def test_min():
    try:
        root = Node(10)
        root.list_insert([70, 60, 40, 50])
        assert root.min_value() == "10"
        print("test_min PASSED")
    except:
        print("test_min FAILED")

def test_max():
    try:
        root = Node(10)
        root.list_insert([70, 60, 40, 50])
        assert root.max_value() == "70"
        print("test_max PASSED")
    except:
        print("test_max FAILED")


def test_delete_node():
    try:
        root_1 = Node(10)
        root_1.list_insert([70, 60, 40, 50])
        root_2 = Node(10)
        root_2.list_insert([70, 60, 40, 50])
        root_2.delete_node(70)
        assert root_1.max_value() != root_2.max_value()
        print("test_delete_node PASSED")
    except:
        print("test_delete_node FAILED")


test_list_insert_true()
test_min()
test_max()
test_delete_node()