from testbook import testbook


@testbook("./notebooks/notebook.ipynb", execute=True)
def test_hello_world(tb):
    assert tb.cell_output_text(0) == "Hello world"
