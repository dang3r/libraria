from libraria import __version__, \
        limit, languages, held_at_locations, available_at_locations, audiences, \
        contents


def test_version():
    assert __version__ == '0.1.0'

def test_limit():
    lim = 13
    assert lim == len(list(limit(range(100), lim)))

def test_languages():
    assert set(["eng", "Any", "chi"]) <= set(languages())

def test_held_at_locations():
    assert set(["ANY", "College of San Mateo"]) <= set(held_at_locations())

def test_available_at_locations():
    assert set(["Belmont", "Brisbane", "County Central"]) <= set(available_at_locations())

def audiences():
    assert set(["Audience - Any", "adult", "children", "teen"]) <= set(audiences())

def contents():
    assert set(["FICTION", "GOVERNMENT_DOCUMENTS"]) <= set(contents())