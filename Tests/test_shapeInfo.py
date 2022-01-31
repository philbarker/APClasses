import pytest
from AP import ShapeInfo

@pytest.fixture(scope="module")
def test_ShapeInfo():
    sh = ShapeInfo()
    return sh

def test_initShapeInfo(test_ShapeInfo):
    sh = test_ShapeInfo
    assert sh.id == ""
    assert sh.label == {}
    assert sh.comment == {}
    assert sh.targets == {}
    assert sh.closed == False
    assert sh.ignoreProps == []
    assert sh.mandatory == False
    assert sh.severity == ""
    assert sh.note == {}

def test_set_id(test_ShapeInfo):
    sh = test_ShapeInfo
    assert sh.id == ""
    sh.set_id("TestShape")
    assert sh.id == "TestShape"
    with pytest.raises(TypeError) as e:
        sh.set_id(1)
    assert str(e.value) == "Shape identifier must be a string."
    assert sh.id == "TestShape"

def test_add_label(test_ShapeInfo):
    sh = test_ShapeInfo
    assert sh.label == {}
    sh.add_label("en", "Test")
    assert sh.label == {"en": "Test"}
    sh.add_label("es", "Prueba")
    assert sh.label == {"en": "Test", "es": "Prueba"}
    with pytest.raises(TypeError) as e:
        sh.add_label("en", 2)
    assert str(e.value) == "Language identifier and label must be strings."
    assert sh.label == {"en": "Test", "es": "Prueba"}
    sh.add_label("en", "Probe")
    assert sh.label == {"en": "Probe", "es": "Prueba"}

def test_append_target(test_ShapeInfo):
    sh = test_ShapeInfo
    assert sh.targets == {}
    sh.append_target("dc:author", "objectsOf")
    assert sh.targets == {"objectsof": "dc:author"}
    sh.append_target("dc:Agent", "Class")
    assert sh.targets == {"objectsof": "dc:author", "class": "dc:Agent"}
    with pytest.raises(TypeError) as e:
        sh.append_target("instance", 2)
    assert str(e.value) == "Target and type must be strings."
    sh.append_target("dc:creator", "objectsOf")
    assert sh.targets == {"objectsof": "dc:creator", "class": "dc:Agent"}

def test_set_closed(test_ShapeInfo):
    sh = test_ShapeInfo
    assert sh.closed == False
    sh.set_closed(True)
    assert sh.closed == True
    sh.set_closed(False)
    assert sh.closed == False
    with pytest.raises(TypeError) as e:
        sh.set_closed("True")
    assert str(e.value) == "Value must be a boolean, True or False."

def test_append_ignoreProps(test_ShapeInfo):
    sh = test_ShapeInfo
    assert sh.ignoreProps == []
    sh.append_ignoreProps("rdf:type")
    assert sh.ignoreProps == ["rdf:type"]
    sh.append_ignoreProps("sdo:type")
    assert sh.ignoreProps == ["rdf:type", "sdo:type"]
    with pytest.raises(TypeError) as e:
        sh.append_ignoreProps(["dct:type"])
    assert str(e.value) == "Property id must be a string."
    assert sh.ignoreProps == ["rdf:type", "sdo:type"]

def test_set_mandatory(test_ShapeInfo):
    sh = test_ShapeInfo
    assert sh.mandatory == False
    sh.set_mandatory(True)
    assert sh.mandatory == True
    sh.set_mandatory(False)
    assert sh.mandatory == False
    with pytest.raises(TypeError) as e:
        sh.set_mandatory("True")
    assert str(e.value) == "Value must be a boolean, True or False."

def test_set_severity(test_ShapeInfo):
    sh = test_ShapeInfo
    assert sh.severity == ""
    sh.set_severity("Violation")
    assert sh.severity == "violation"
    sh.set_severity("3")
    assert sh.severity == "3"
    with pytest.raises(TypeError) as e:
        sh.set_severity(3)
    assert str(e.value) == "Severity must be a string."

def test_add_note(test_ShapeInfo):
    sh = test_ShapeInfo
    assert sh.note == {}
    sh.add_note("en", "A Test")
    assert sh.note == {"en": "A Test"}
    sh.add_note("es", "Una Prueba")
    assert sh.note == {"en": "A Test", "es": "Una Prueba"}
    with pytest.raises(TypeError) as e:
        sh.add_note("en", 2)
    assert str(e.value) == "Language identifier and note must be strings."
    assert sh.note == {"en": "A Test", "es": "Una Prueba"}
    sh.add_note("en", "A Probe")
    assert sh.note == {"en": "A Probe", "es": "Una Prueba"}
