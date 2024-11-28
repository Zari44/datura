import tempfile
import contextlib

from src.main import word_count


@contextlib.contextmanager
def create_file(content: str):
    with tempfile.NamedTemporaryFile(delete=True, mode="w") as tmp_file:
        tmp_file.write(content)
        tmp_file.flush()
        yield tmp_file
def test_word_count_returns_correct_values():
    content = """content"""
    with create_file(content) as tmp_file:
        count = word_count(tmp_file.name)
        assert dict(count) == {"content": 1}

    content = """Hello world!
This is a sample text file.
Hello Python world."""
    with create_file(content) as tmp_file:
        count = word_count(tmp_file.name)
        assert dict(count) == {
    'hello': 2,
    'world': 2,
    'this': 1,
    'is': 1,
    'a': 1,
    'sample': 1,
    'text': 1,
    'file': 1,
    'python': 1
}