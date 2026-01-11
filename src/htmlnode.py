class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        # will be overridden by child class
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None or self.props == "":
            return ""
        html_attributes = ""
        for k, v in self.props.items():
            html_attributes += f" {k}=\"{v}\""
        
        return html_attributes

    def __repr__(self):
        if not self.tag:
            return "Raw text, not HTML"
        message = f"<{self.tag}>"
        if not self.children:
            message += f"{self.value}\n"
        elif not self.value:
            message += "has child HTML nodes\n"
        if self.props:
            message += self.props_to_html()
        message += f"</{self.tag}>"
        return message


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return self.to_html()
    

node = LeafNode(
    tag = 'p',
    value = "This is a paragarph!",
    props={
    "href": "https://www.google.com",
    "target": "_blank",
})

print(node)
