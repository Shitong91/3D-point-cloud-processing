import unittest


class RandomSelfTestCase(unittest.TestCase):
    def testGettingItems(self):
        import hnswlib
        import numpy as np

        dim = 16
        num_elements = 10000

        # Generating sample data
        data = np.float32(np.random.random((num_elements, dim)))
        labels = np.arange(0, num_elements)

        # Declaring index
        p = hnswlib.Index(space='l2', dim=dim)  # possible options are l2, cosine or ip

        # Initing index
        # max_elements - the maximum number of elements, should be known beforehand
        #     (probably will be made optional in the future)
        #
        # ef_construction - controls index search speed/build speed tradeoff
        # M - is tightly connected with internal dimensionality of the data
        #     stronlgy affects the memory consumption

        p.init_index(max_elements=num_elements, ef_construction=100, M=16)

        # Controlling the recall by setting ef:
        # higher ef leads to better accuracy, but slower search
        p.set_ef(300)

        p.set_num_threads(4)  # by default using all available cores

        # Before adding anything, getting any labels should fail
        self.assertRaises(Exception, lambda: p.get_items(labels))

        print("Adding all elements (%d)" % (len(data)))
        p.add_items(data, labels)

        # After adding them, all labels should be retrievable
        returned_items = p.get_items(labels)
        self.assertSequenceEqual(data.tolist(), returned_items)

if __name__ == "__main__":
    unittest.main()