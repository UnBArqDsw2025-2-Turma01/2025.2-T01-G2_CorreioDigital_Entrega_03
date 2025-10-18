from observer.news_agency import NewsAgency
from observer.news_reader import NewsReader


def test_observer_notification(capsys):
    agency = NewsAgency()
    NewsReader(agency, "T1")
    NewsReader(agency, "T2")

    agency.set_news("Teste")

    captured = capsys.readouterr()
    assert "[T1] Nova notícia: Teste" in captured.out
    assert "[T2] Nova notícia: Teste" in captured.out
