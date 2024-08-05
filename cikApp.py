import requests
from collections import namedtuple
import os

Sec = namedtuple('Sec', ['name', 'ticker', 'cik_id'])


class secEdgar():

    def __init__(self, file_url) -> None:
        self.file_url = file_url
        self.named_dict = {}
        self.ticker_dict = {}
        self.cik_dict = {}

        headers = {'user-agent': os.environ["USER_AGENT"]}
        response = requests.get(url=self.file_url, headers=headers)

        self.response_json = response.json()
        self.populate_dicts()

    def populate_dicts(self):
        for _, value in self.response_json.items():
            cik_id = value["cik_str"]
            company_name = value["title"]
            ticker = value["ticker"]

            self.named_dict[company_name] = cik_id
            self.ticker_dict[ticker] = cik_id
            self.cik_dict[cik_id] = (company_name, ticker)

    def name_to_cik(self, name: str) -> list[tuple[str, int]]:
        if name not in self.named_dict:
            raise BaseException("Cant find name in dictionary")

        cik_id = self.named_dict[name]
        _, ticker = self.cik_dict[cik_id]

        return Sec(name=name, ticker=ticker, cik_id=cik_id)

    def ticker_to_cik(self, ticker) -> list[tuple[str, int]]:
        if ticker not in self.ticker_dict:
            raise BaseException("Cant find ticker in dictionary")

        cik_id = self.ticker_dict[ticker]
        company_name, _ = self.cik_dict[cik_id]

        return Sec(name=company_name, ticker=ticker, cik_id=cik_id)


if __name__ == "__main__":
    url = "https://www.sec.gov/files/company_tickers.json"
    edgar = secEdgar(file_url=url)

    print(edgar.name_to_cik('United Maritime Corp'))
    # Sec(name='United Maritime Corp', ticker='USEA', cik_id=1912847)
    print(edgar.ticker_to_cik('USEA'))
    # Sec(name='United Maritime Corp', ticker='USEA', cik_id=1912847)
    # print(edgar.name_to_cik('ap'))
