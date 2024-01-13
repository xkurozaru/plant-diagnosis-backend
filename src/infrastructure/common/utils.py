def list_to_text(array: list) -> str:
    return ",".join(array)


def text_to_list(text: str) -> list[str]:
    return text.split(",")
