const url = 'http://127.0.0.1:8000/api/top_habr';
const articleTemplate = document.querySelector('#article-template').content;
const pageEl = document.querySelector('.content');
const loader = document.querySelector('.loader-container');

import '../pages/index.css';

function createArticle(article) {
    const articleEl = articleTemplate.querySelector('.article').cloneNode(true);
    const viewsEl = articleEl.querySelector('.article__views');
    const textEl = articleEl.querySelector('.article__text');
    const titleEl = articleEl.querySelector('.article__title');
    const linkEl = articleEl.querySelector('.article__link');

    viewsEl.textContent = article.views;
    textEl.innerHTML = article.text;
    titleEl.textContent = article.title;
    linkEl.textContent = article.url;
    linkEl.href = article.url;

    return articleEl;
}

fetch(url, {
    method: 'GET',
    headers: {
        'Content-type': 'application/json'
    }
})
.then(res => {
    if (res.ok) {
        res = res.json()
        return res;
    } else {
        return Promise.reject('Request to get articles failed');
    }
})
.then(data => {
    const articles = Array.from(data.data);
    Array.from(articles).forEach(article => {
        const articleEl = createArticle(article);
        pageEl.appendChild(articleEl);
    });
    loader.style.display = 'none';
})
.catch(err => {
    console.error(err);
    loader.style.display = 'none';
});
