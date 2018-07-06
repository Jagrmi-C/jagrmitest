def remove_html_markup(s):
    tag = False
    qoute = False
    out = ""
    for c in s:
        # start markup
        if c == "<" and not qoute:
            tag = True
        # end markup
        elif c == ">" and not qoute:
            tag = False
        elif c == '"' or c == "'" and tag:
            qoute = not qoute
        elif not tag:
            out = out + c
    return out


print(remove_html_markup("<b>foo</b>"))
print(remove_html_markup('<a href=">">foo</a>'))
print(remove_html_markup('<"b">foo</"b">'))
