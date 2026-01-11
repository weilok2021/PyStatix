import unittest
from src.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single_attribute(self):
        """Test props_to_html with a single attribute"""
        node = HTMLNode("a", "Click here", None, {"href": "https://www.google.com"})
        expected = ' href="https://www.google.com"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_multiple_attributes(self):
        """Test props_to_html with multiple attributes"""
        node = HTMLNode(
            "a",
            "Click here",
            None,
            {"href": "https://www.google.com", "target": "_blank"}
        )
        result = node.props_to_html()
        # Check that both attributes are present with leading space
        self.assertIn('href="https://www.google.com"', result)
        self.assertIn('target="_blank"', result)
        self.assertTrue(result.startswith(" "))

    def test_props_to_html_no_props(self):
        """Test props_to_html when props is None"""
        node = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_empty_props(self):
        """Test props_to_html when props is an empty dictionary"""
        node = HTMLNode("div", "Content", None, {})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_various_attributes(self):
        """Test props_to_html with various HTML attributes"""
        node = HTMLNode(
            "img",
            None,
            None,
            {"src": "image.jpg", "alt": "A beautiful image", "width": "500"}
        )
        result = node.props_to_html()
        self.assertIn('src="image.jpg"', result)
        self.assertIn('alt="A beautiful image"', result)
        self.assertIn('width="500"', result)
        self.assertTrue(result.startswith(" "))

    def test_to_html_not_implemented(self):
        """Test that to_html raises NotImplementedError"""
        node = HTMLNode("p", "Test")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_repr(self):
        """Test the string representation of HTMLNode"""
        node = HTMLNode("a", "Link", None, {"href": "https://example.com"})
        repr_string = repr(node)
        # Check that important information is in the repr
        self.assertIn("a", repr_string)
        self.assertIn("Link", repr_string)
        self.assertIn("href", repr_string)

    def test_node_with_children(self):
        """Test creating a node with children"""
        child1 = HTMLNode("span", "Child 1")
        child2 = HTMLNode("span", "Child 2")
        parent = HTMLNode("div", None, [child1, child2])
        self.assertEqual(len(parent.children), 2)
        self.assertEqual(parent.value, None)

    def test_node_defaults_to_none(self):
        """Test that all parameters default to None"""
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)


if __name__ == "__main__":
    unittest.main()