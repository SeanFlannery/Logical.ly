import requests
from lxml import etree
import pandas as pd
from fake_useragent import UserAgent
from tqdm import tqdm

ARGUMAN_ROOT_URL = "https://en.arguman.org"
FALLACIES_PAGE_URL = ARGUMAN_ROOT_URL + "/fallacies"

HTML_PARSER = etree.HTMLParser()

ua = UserAgent()
user_agent_header = {"User-Agent": ua.chrome}


def load_reports(offset=0):
    res = requests.get(
        FALLACIES_PAGE_URL, headers=user_agent_header, params={"offset": offset}
    )

    res.raise_for_status()  # make sure request is successful
    root = etree.fromstring(res.text, HTML_PARSER)
    return root.xpath('//*[@class="fallacy-report"]')


def parse_report(report):
    title = report.xpath("div/h2/a/text()")[0].strip()
    url = ARGUMAN_ROOT_URL + report.xpath("div/h2/a/@href")[0]
    premise_content = report.xpath("div/div[1]/text()")[0].strip()

    try:
        premise_type = next(
            filter(
                lambda x: x in {"but", "because", "however"},
                report.xpath("div/div[1]/@class")[0].split(),
            )
        )
    except StopIteration:
        premise_type = None

    fallacy_type = report.xpath("div/div[2]/h4/text()")[0]
    fallacy_reason = report.xpath("div/div[2]/text()")[1].strip()

    return {
        "title": title,
        "url": url,
        "premise_content": premise_content,
        "premise_type": premise_type,
        "fallacy_type": fallacy_type,
        "fallacy_reason": fallacy_reason,
    }


def main():
    print("Loading fallacy reports...")
    reports = []
    for offset in tqdm(range(0, 1000, 10)):
        for raw_report in load_reports(offset=offset):
            reports.append(parse_report(raw_report))

    df = pd.DataFrame(reports)
    print("Finished loading fallacy reports")

    path = "./data/fallacies.csv"
    df.to_csv(path)
    print(f"Saved reports to {path}")


if __name__ == "__main__":
    main()
