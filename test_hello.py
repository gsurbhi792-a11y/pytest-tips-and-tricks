from hello import testing_helloValue, testing_ByeValue

def test_helloValue():
    assert "hi"== testing_helloValue()

def test_ByeValue():
    assert "bye"== testing_ByeValue()