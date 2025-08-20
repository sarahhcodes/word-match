import project

def test_convert(): # test that project successfully converts csv to list
    cards = project.Cards("test_vocab.csv", 3)

    assert cards.vocab_list == [{'Japanese': '油 (abura)', 'English': 'oil'}, {'Japanese': '愛 (ai)', 'English': 'love, affection, care'}, {'Japanese': '愛情 (aijou)', 'English': 'love, affection'}, {'Japanese': '相変わらず (aikawarazu)', 'English': 'as ever, as usual, the same'}, {'Japanese': '生憎 (ainiku)', 'English': 'unfortunately; sorry, but…'}, {'Japanese': '愛する (aisuru)', 'English': 'to love'}]