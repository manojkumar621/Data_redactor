import pytest


from assignment1.address_detector import detect_address, censor_address

@pytest.fixture
def sample_test_string():
    '''Provides a sample incident string to test detect_names method'''
    return '''Kevin O'Toole and james johnson
        Vice President -- Marketing
        Western Hub Properties L.L.C.
        14811 St. Marys Ln., Suite 150
        Houston, TX   77079-2908
        281-679-3591 V
        281-679-1564 F
        713-208-0153 M
        kotoole@westernhubs.com'''

def test_detect_address(sample_test_string):
    pyap_addresses, spacy_addresses = detect_address(sample_test_string)
    assert len(pyap_addresses)>0 or len(spacy_addresses)>0

def test_censor_address(sample_test_string):
    final_string = censor_address(sample_test_string)
    assert final_string is not sample_test_string