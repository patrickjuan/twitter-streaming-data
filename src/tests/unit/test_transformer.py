from src.transformer.transform import identify_mentions


def test_identify_mentions_should_pass():
    input = {"id": "11111111", "text": "Some tweet about Hamilton"}
    expected_output = {
        "id": "11111111",
        "text": "Some tweet about Hamilton",
        "mention_driver": ["Lewis Hamilton"],
        "mention_team": ["Mercedes AMG Petronas F1 Team"],
        "mention_country": ["United Kingdom"],
    }
    output = identify_mentions(input)
    assert expected_output == output


def test_identify_mentions_should_fail():
    input = {"id": "11111111", "text": "Some tweet about Hamilton"}
    expected_output = {
        "id": "11111111",
        "text": "Some tweet about Hamilton",
        "mention_driver": "",
        "mention_team": ["Mercedes AMG Petronas F1 Team"],
        "mention_country": ["United Kingdom"],
    }
    output = identify_mentions(input)
    assert expected_output != output
