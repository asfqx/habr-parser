from bs4 import BeautifulSoup
from httpx import AsyncClient
from app.core.config import settings
from app.models.article import Article
import time


async def get_html_from_habr(url) -> str:
    async with AsyncClient(follow_redirects=True) as client:
        response = await client.get(url)
        return response.text


def get_soup(html) -> BeautifulSoup:
    return BeautifulSoup(html, "lxml")


async def get_article_text(url) -> str:
    article_html = await get_html_from_habr(url)
    soup = get_soup(article_html)
    article_text = soup.find("article", class_="tm-article-presenter__content")
    if article_text:
        return str(article_text)


async def get_articles_from_habr() -> list[Article]:
    html = await get_html_from_habr(settings.URL)
    soup = get_soup(html)
    data: list[Article] = []
    all_articles = soup.find_all("article", class_="tm-articles-list__item")
    for article in all_articles:
        article_title: str = (
            article.find("a", class_="tm-title__link").find("span").text
        )
        article_url: str = article.find("a", class_="tm-title__link")["href"]
        article_url = "https://habr.com" + article_url
        article_reads: str = article.find("span", class_="tm-icon-counter__value").text
        article_text: str = await get_article_text(article_url)
        data.append(Article(article_title, article_url, article_reads, article_text))
        time.sleep(0.5)
    return data
