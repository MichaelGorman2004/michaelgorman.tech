import markdown2


def render_markdown(content: str) -> str:
    return markdown2.markdown(content)
