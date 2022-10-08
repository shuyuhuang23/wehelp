const PROMOTION_NUM = 2;
const PAGINATION = 8;
const URL = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'

var currentIdx = 0;

function renderPromotion() {
    fetch(URL, { method: 'GET' })
        .then(res => {
            return res.json();
        }).then(result => {

            var parsedResult = result['result']['results']
            var promotionList = document.getElementById('promotion-list');

            for (let i = 0; i < PROMOTION_NUM; i++) {

                let promotionItem = document.createElement('div');
                promotionItem.className = "promotion-item";

                let promotionImg = document.createElement('img');
                promotionImg.className = "promotion-img";
                promotionImg.src = 'http' + parsedResult[i]['file'].split('http')[1];

                let promotionTitle = document.createElement('p');
                promotionTitle.className = "promotion-title";
                let promotionTitleText = document.createTextNode(parsedResult[i]['stitle']);
                promotionTitle.appendChild(promotionTitleText);

                promotionItem.appendChild(promotionImg);
                promotionItem.appendChild(promotionTitle);

                promotionList.appendChild(promotionItem);

                currentIdx += 1;
            }

        });
}

function renderContent() {
    fetch(URL, { method: 'GET' })
        .then(res => {
            return res.json();
        }).then(result => {

            let parsedResult = result['result']['results']
            let contentList = document.getElementById('content-list');

            console.log(parsedResult.length);
            let endIdx = currentIdx + PAGINATION
            while (currentIdx < Math.min(parsedResult.length, endIdx)) {
                let contentItem = document.createElement('div');
                contentItem.className = "content-item";

                let contentImg = document.createElement('img');
                contentImg.className = "content-img";
                contentImg.src = 'http' + parsedResult[currentIdx]['file'].split('http')[1];

                let contentTitle = document.createElement('div');
                contentTitle.className = "content-title";
                let contentTitleText = document.createTextNode(parsedResult[currentIdx]['stitle']);
                contentTitle.appendChild(contentTitleText);

                contentItem.appendChild(contentImg);
                contentItem.appendChild(contentTitle);

                contentList.appendChild(contentItem);

                currentIdx += 1;
            }
            // for (let i = PROMOTION_NUM; i < PAGINATION + PROMOTION_NUM; i++) {

            //     let contentItem = document.createElement('div');
            //     contentItem.className = "content-item";

            //     let contentImg = document.createElement('img');
            //     contentImg.className = "content-img";
            //     contentImg.src = 'http' + parsedResult[i]['file'].split('http')[1];

            //     let contentTitle = document.createElement('div');
            //     contentTitle.className = "content-title";
            //     let contentTitleText = document.createTextNode(parsedResult[i]['stitle']);
            //     contentTitle.appendChild(contentTitleText);

            //     contentItem.appendChild(contentImg);
            //     contentItem.appendChild(contentTitle);

            //     contentList.appendChild(contentItem);

            //     page_cnt += 1;
            // }

        });
}

document.getElementById("more-btn").addEventListener("click", renderContent);

renderPromotion();
renderContent();