import pytest

from class_for_fixture import Company

def test_our_first_test()-> None:
    assert 1 == 2

def test_our_second_test()-> None:
    assert 1 == 1

@pytest.mark.skip
def test_test_to_be_skipped()-> None:
    assert True

@pytest.mark.skipif(4 > 1, reason="Skipped as 4>1")
def test_to_be_skipped_if()-> None:
    assert True

@pytest.mark.skipif(1 > 4, reason="Skipped as 4>1")
def test_to_be_skipped_if_2()-> None:
    assert True

@pytest.mark.xfail
def test_dont_care_if_it_fails()-> None:
    assert False

@pytest.mark.xfail
def test_dont_care_if_it_fails_2()-> None:
    assert True

@pytest.mark.slow
def test_with_custom_mark1()-> None:
    assert True

@pytest.fixture
def company()-> Company:
    return Company(name="Fiver", stock_symbol="FVRR")

def test_with_fixture(company: Company)-> None:
    print(f"Printing company details : {company}")

@pytest.mark.parametrize(
    "company_name", 
    ["tikTok","Instagram","Twitter"],
    )
def test_parametrized(company_name: str)-> None:
    print(f"\n Test with {company_name}")

@pytest.mark.parametrize(
    "company_name", 
    ["TikTok","Instagram","Twitter"],
    ids=["Marcus", "Corinna",'Livia']
    )
def test_parametrized_with_ids(company_name: str)-> None:
    print(f"\n Test with {company_name}")

def raise_covid19_exception()-> None:
    raise ValueError("Coronavirus Exception")

def test_raise_covid19_exception_should_pass()-> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()

    assert "Coronavirus Exception" == str(e.value)