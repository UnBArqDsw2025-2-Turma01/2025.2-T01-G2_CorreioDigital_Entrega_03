from observer.news_agency import NewsAgency
from observer.news_reader import NewsReader


def main() -> None:
    agency = NewsAgency()
    NewsReader(agency, "Leitor A")
    NewsReader(agency, "Leitor B")

    agency.set_news("Primeira edição: Padrão Observer em Python!")
    agency.set_news("Segunda edição: Atualização em Python.")


if __name__ == "__main__":
    main()
