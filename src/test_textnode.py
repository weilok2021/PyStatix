import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    

    def test_eq_same_nodes_with_url(self):
        """Test that two identical nodes with URLs are equal"""
        node1 = TextNode("Click here", TextType.LINK, "https://example.com")
        node2 = TextNode("Click here", TextType.LINK, "https://example.com")
        self.assertEqual(node1, node2)


    def test_eq_different_text(self):
        """Test that nodes with different text are not equal"""
        node1 = TextNode("Text one", TextType.BOLD)
        node2 = TextNode("Text two", TextType.BOLD)
        self.assertNotEqual(node1, node2)


    def test_eq_different_text_type(self):
        """Test that nodes with different text types are not equal"""
        node1 = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)


    def test_eq_different_url(self):
        """Test that nodes with different URLs are not equal"""
        node1 = TextNode("Link", TextType.LINK, "https://example.com")
        node2 = TextNode("Link", TextType.LINK, "https://different.com")
        self.assertNotEqual(node1, node2)


    def test_eq_url_none_vs_url_set(self):
        """Test that node with None URL is not equal to node with URL"""
        node1 = TextNode("Text", TextType.BOLD, None)
        node2 = TextNode("Text", TextType.BOLD, "https://example.com")
        self.assertNotEqual(node1, node2)


    def test_eq_both_urls_none(self):
        """Test that two nodes with None URLs are equal if other properties match"""
        node1 = TextNode("Text", TextType.CODE, None)
        node2 = TextNode("Text", TextType.CODE, None)
        self.assertEqual(node1, node2)


    def test_eq_both_urls_none_default(self):
        """Test that nodes with default None URL are equal"""
        node1 = TextNode("Code snippet", TextType.CODE)
        node2 = TextNode("Code snippet", TextType.CODE)
        self.assertEqual(node1, node2)


    def test_repr(self):
        """Test the string representation of TextNode"""
        node = TextNode("Test", TextType.BOLD, "https://test.com")
        expected = "TextNode(Test, **Bold text**, https://test.com)"
        self.assertEqual(repr(node), expected)


    def test_repr_no_url(self):
        """Test the string representation with None URL"""
        node = TextNode("Test", TextType.ITALIC)
        expected = "TextNode(Test, _Italic text_, None)"
        self.assertEqual(repr(node), expected)


if __name__ == "__main__":
    unittest.main()