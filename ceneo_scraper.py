import requests
from bs4 import BeautifulSoup
import json
import os


product_code=str(input("Enter product code: "))
page=1

next=True
headers={
    "Host":"www.ceneo.pl",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0",
    "Cookie":"sv3=1.0_5d2c42dc-3cbb-11f1-be91-3b6797ee5501; urdsc=2; userCeneo=ID=fd01e1b9-036f-4fe9-a79d-f504fcad8403; __RequestVerificationToken=cbcYw-Q-uW7vDGz-ckKFWDjwR62fthsjAgecHAp6BMkpiKYY4Z6j9An4Hv9OFBiIh2a4ET3dn65yA8tvlLJk33CoycAkxdYOdxULqjzS6pI1; st2=sref%3dhttps%3a%2f%2fwww.bing.com%2f%2c_t%3d63912295084%2cencode%3dtrue; ai_user=dJbZV|2026-04-20T13:18:05.733Z; __utmf=364726cdbe2e8437518b57e7b5f0d525_Dsgqi6QMc9CtX7buqOpcIw%3D%3D; ai_session=UFT16|1776691086272|1776691086272; appType=%7B%22Value%22%3A1%7D; cProdCompare_v2=; browserBlStatus=0; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%2C%22expiryDate%22%3A%222027-04-20T13%3A18%3A07.548Z%22%7D; __rtbh.aid=%7B%22eventType%22%3A%22aid%22%2C%22id%22%3A%225d2c42dc-3cbb-11f1-be91-3b6797ee5501%22%2C%22expiryDate%22%3A%222027-04-20T13%3A18%3A07.548Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22oyN6XOjctxS85o4w3yup%22%2C%22expiryDate%22%3A%222027-04-20T13%3A18%3A07.549Z%22%7D; consentcookie=eyJBZ3JlZUFsbCI6bnVsbCwiQ29uc2VudHMiOlsxXSwiVENGQ29uc2VudERhdGEiOnsiPFB1cnBvc2VzPmtfX0JhY2tpbmdGaWVsZCI6W10sIjxTcGVjaWFsRmVhdHVyZXM+a19fQmFja2luZ0ZpZWxkIjpbXSwiPFZlbmRvcnM+a19fQmFja2luZ0ZpZWxkIjp7IjxDb25zZW50cz5rX19CYWNraW5nRmllbGQiOltdLCI8RGlzY2xvc2VkVmVuZG9ycz5rX19CYWNraW5nRmllbGQiOlsxLDQsOSwxMCwxMSwxMiwxMywxNSwxNiwyMiwyNCwyNSwyNywyOCwzMiwzNCwzNywzOSw0MCw0Miw0NCw1MCw1Miw1OSw2MCw2OCw3MCw3MSw3Niw3Nyw4MSw4Miw4NCw4NSw5MSw5Myw5NSw5Nyw5OCwxMDIsMTA5LDExMCwxMTUsMTIyLDEyNiwxMjksMTMwLDEzMiwxMzQsMTM5LDE0MCwxNDcsMTYxLDE2MywxNjgsMTkyLDE5MywxOTUsMjAyLDIxMywyMjYsMjI4LDI0MSwyNDMsMjQ2LDI1MywyNjQsMjczLDI3NSwyNzgsMjgxLDI4NCwyOTQsMzA0LDMxMiwzMTUsMzE3LDMyOCwzNDUsMzczLDM4MSwzODQsMzg4LDM5NCwzOTcsNDAyLDQxNSw0MTYsNDQ3LDQ1Miw0NjgsNDkzLDUxMiw1MzEsNTM0LDU0Niw1NTksNTg3LDYwNiw2MzAsNjMxLDY1Myw2NTcsNjY3LDcwMyw3MDcsNzIxLDczNCw3NTUsNzU4LDc1OSw3NjIsNzY3LDc3Miw3OTMsODA2LDgxMiw4MjcsODMyLDg0OCw4NTMsOTI5LDk2OSw5ODUsMTAyOSwxMDUxLDExMjZdLCI8TGVnaXRpbWF0ZUludGVyZXN0cz5rX19CYWNraW5nRmllbGQiOltdfX0sIlRDU3RyaW5nIjoiQ1FpOWowQVFpOWowQUd5QUJDUExDYkVnQUFBQUFBQUFBQjVZQUFBQUFBQUEuSUl6SkQ3QmJGTFVGQXdGaGpZS3NRTUlFVFVNQ0FBb1FBQUFhQkFDQUJRQUtRSUFRQ2trQVFCQVNnQkFBQ0FBQUFJQ1JCSVFBTUFBQUFDRUFBUUFBQUlBQUVBQUNRQVFBSUFBQUFnQUFRQUFBWUFBQWlBSUFBQUFBSWdBSUFFQUFBbVFoQUFBSUFFRUFBaEFBRUlBQUFBQUFBQUFBQUFnQUFBQUFDQUFJQUFBQUFBQ0FBQUlBQUFBQUFBQUFBQUJBIiwiVHJ1c3RlZFBhcnRuZXJzIjpbXSwiVmVyc2lvbiI6InYzIn0="

}
all_opinions=[]
while next:
    
    url= f"https://www.ceneo.pl/{product_code}/opinie-{page}"
    print(page,next,url)
    r=requests.get(url,headers=headers)
    print(r.status_code)

    page_dom=BeautifulSoup(r.text, 'html.parser')

    # product_name=page_dom.select_one('h1').get_text()

    opinions=page_dom.select('div.js_product-review:not(.user-post--highlight)')



    for opinion in opinions:
        single_opinion={
            "opinion_id":opinion.get('data-entry-id'),
            "author":opinion.select_one(".user-post__author-name").get_text().strip(),
            "recommendation":opinion.select_one(".user-post__author-recomendation").get_text().strip() if opinion.select_one(".user-post__author-recomendation") else None,
            "score":opinion.select_one(".user-post__score-count").get_text().strip(),
            "content":opinion.select_one(".user-post__text").get_text().strip(),
            "pros":[opinion.get_text().strip() for opinion in opinion.select(".review-feature__item--positive")],
            "cons":[opinion.get_text().strip() for opinion in opinion.select(".review-feature__item--negative")],
            "helpful":opinion.select_one(".vote-yes").get('data-vote'),
            "unhelpful":opinion.select_one(".vote-no").get('data-vote'),
            "publish_date":opinion.select_one(".user-post__published time:nth-child(1)").get('datetime').strip() if opinion.select_one(".user-post__published time:nth-child(1)").get('datetime') else None,
            "purchase_date":opinion.select_one(".user-post__published time:nth-child(1)").get('datetime').strip() if opinion.select_one(".user-post__published time:nth-child(1)").get('datetime') else None,

        }
        # print(single_opinion)
        all_opinions.append(single_opinion)


    next = True if page_dom.select_one("button.pagination__next") else False
    if next: page+=1

if not os.path.exists("./opinions"):
    os.mkdir("./opinions")

with open(f"./opinions/{product_code}.json", "w", encoding="utf-8") as f:
    json.dump(all_opinions,f, indent=4, ensure_ascii=False)