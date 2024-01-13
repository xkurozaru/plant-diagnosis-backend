from nanoid import generate


def new_nano_id() -> str:
    return generate(size=21)
