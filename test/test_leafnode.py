import unittest
from src.htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        """Test rendering a simple paragraph tag"""
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        """Test rendering an anchor tag with href attribute"""
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        """Test rendering a leaf node with no tag (raw text)"""
        node = LeafNode(None, "Just plain text")
        self.assertEqual(node.to_html(), "Just plain text")

    def test_leaf_to_html_no_value_raises_error(self):
        """Test that a leaf node without a value raises ValueError"""
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_with_multiple_props(self):
        """Test rendering a tag with multiple attributes"""
        node = LeafNode("a", "Click here", {"href": "https://example.com", "class": "button"})
        result = node.to_html()
        # Check structure and that both attributes are present
        self.assertTrue(result.startswith("<a"))
        self.assertTrue(result.endswith("</a>"))
        self.assertIn('href="https://example.com"', result)
        self.assertIn('class="button"', result)
        self.assertIn("Click here", result)

    def test_leaf_to_html_bold_tag(self):
        """Test rendering a bold tag"""
        node = LeafNode("b", "Bold text")
        self.assertEqual(node.to_html(), "<b>Bold text</b>")

    def test_leaf_to_html_italic_tag(self):
        """Test rendering an italic tag"""
        node = LeafNode("i", "Italic text")
        self.assertEqual(node.to_html(), "<i>Italic text</i>")

    def test_leaf_to_html_code_tag(self):
        """Test rendering a code tag"""
        node = LeafNode("code", "print('Hello')")
        self.assertEqual(node.to_html(), "<code>print('Hello')</code>")

    def test_leaf_to_html_h1_tag(self):
        """Test rendering a heading tag"""
        node = LeafNode("h1", "This is a heading")
        self.assertEqual(node.to_html(), "<h1>This is a heading</h1>")

    def test_leaf_to_html_link_with_target(self):
        """Test rendering a link with multiple attributes"""
        node = LeafNode("a", "Open in new tab", {"href": "https://example.com", "target": "_blank"})
        result = node.to_html()
        self.assertIn('href="https://example.com"', result)
        self.assertIn('target="_blank"', result)
        self.assertIn("Open in new tab", result)

    def test_leaf_to_html_span_with_class(self):
        """Test rendering a span with class attribute"""
        node = LeafNode("span", "Highlighted", {"class": "highlight"})
        self.assertEqual(node.to_html(), '<span class="highlight">Highlighted</span>')

    def test_leaf_no_children(self):
        """Test that LeafNode has no children"""
        node = LeafNode("p", "Text")
        self.assertIsNone(node.children)

    def test_leaf_repr(self):
        """Test the string representation of LeafNode"""
        node = LeafNode("a", "Link text", {"href": "https://test.com"})
        repr_string = repr(node)
        # Should contain tag and value info, but not mention children
        self.assertIn("a", repr_string)
        self.assertIn("Link text", repr_string)

    def test_leaf_repr_no_tag(self):
        """Test repr for raw text (no tag)"""
        node = LeafNode(None, "Raw text")
        repr_string = repr(node)
        self.assertIn("Raw text", repr_string)

    def test_leaf_to_html_empty_string_value_raises_error(self):
        """Test that empty string value raises ValueError"""
        node = LeafNode("p", "")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_self_closing_tag(self):
        """Test rendering a self-closing tag like br"""
        node = LeafNode("br", "")
        # Even though br is typically self-closing, our implementation
        # should raise ValueError for empty value
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()