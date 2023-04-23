class Coloring:
    def __init__(self, text):
        self.TORED = [
            "class",
            "def",
            "return",
            "from",
            "import",
            "as",
        ]

        self.TOBLUE = [
            "if",
            "else",
            "elif",
            "for",
            "while",
            "try",
            "except",
            "raise",
            "self",
        ]
        self.text = text

        #spaces and new lines:
        self.text = self.text.replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;")
        self.text = self.text.replace(" ", "&nbsp;")
        self.text = self.text.replace("\n", "<br>")

        #change to red:
        for r in self.TORED:
            self.text = self.text.replace(r, "<b style=\"color: red;\">" + r + "</b>")

        #change to blue:
        for b in self.TOBLUE:
            self.text = self.text.replace(b, "<b style=\"color: blue;\">" + b + "</b>")
    
    def color_bg(self, color):
        self.text = "<div style=\"background-color: " + color + ";\">" + self.text + "</div>"
    
    def color_tc(self, color):
        self.text = "<div style=\"color: " + color + ";\">" + self.text + "</div>"

    def colored(self):
        return self.text
  