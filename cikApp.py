import requests


class secEdgar():

    def __init__(self, file_url) -> None:
        self.file_url = file_url
        self.named_dict = {}
        self.ticker_dict = {}

        headers = {'user-agent': 'MLT BF bflo2857@gmail.com'}
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

    def name_to_cik(self) -> list[tuple[str, int]]:
        return [self.named_dict.items()]

    def ticker_to_cik(self) -> list[tuple[str, int]]:
        return [self.ticker_dict.items()]


if __name__ == "__main__":
    url = "https://www.sec.gov/files/company_tickers.json"
    edgar = secEdgar(file_url=url)
