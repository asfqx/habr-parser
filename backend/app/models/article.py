from dataclasses import dataclass


@dataclass
class Article:
    title: str
    url: str
    views: str
    text: str
