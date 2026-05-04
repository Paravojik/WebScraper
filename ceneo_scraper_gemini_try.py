from curl_cffi import requests
# import requests
from bs4 import BeautifulSoup
import json
import os


product_code=str(input("Enter product code: "))
page=1

next=True
headers={
    "Host":"www.ceneo.pl",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0",
    "Cookie":"__RequestVerificationToken=HTs45Lw1FK0_HawCvmy_dH_xF0OobzMQE4PFt-iNeHAoR3EhCcV1ovyX_czqtkM_e3Q2qEaOWzJv_ANqoze_joQ3ZCXk2H5sSciBYVf6nzk1; __utmf=7636197f9eda0d543ff32e8f54c2b10a_Dsgqi6QMc9CtX7buqOpcIw%3D%3D; sv3=2.0_519a1426-47b2-11f1-a437-5dc3532c656f_1777896662399; userCeneo=ID=fb1457c0-5073-422f-9722-74b363d1a7df; ai_user=refCO|2026-05-04T12:11:02.933Z; appType=%7B%22Value%22%3A1%7D; cProdCompare_v2=; __eoi=ID=d02ffe28235a02da:T=1777896663:RT=1777896663:S=AA-AfjYZqXuJ3aQAkX0uiPcwn1OO; cto_bundle=ZiA3NF9GRWNETnFyeFlVb2N4cll1c0U1UUppT0NvdVN3WlJVeSUyRnlOdSUyRklOWnclMkY5OSUyQkElMkI5WmRYSzlGcExmdjR2eWV2NThzTVRFaVlmS2FKQUJ6RGlvQnJ1akZZMVJmeEhGeiUyQiUyQktqWlpjWGt2MTBnVkU0ZzZSRlNNSmZmWndVaHQzUnVE; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%2C%22expiryDate%22%3A%222027-05-04T12%3A11%3A03.787Z%22%7D; __rtbh.aid=%7B%22eventType%22%3A%22aid%22%2C%22id%22%3A%22519a1426-47b2-11f1-a437-5dc3532c656f%22%2C%22expiryDate%22%3A%222027-05-04T12%3A11%3A03.787Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22srCP6qedK6KSKaUWii0o%22%2C%22expiryDate%22%3A%222027-05-04T12%3A11%3A03.787Z%22%7D; ai_session=ZfIHW|1777896663843.1|1777896663843.1; browserBlStatus=0; ga4_ga=GA1.2.519a1426-47b2-11f1-a437-5dc3532c656f; _gcl_au=1.1.220895263.1777896665; consentcookie=eyJBZ3JlZUFsbCI6dHJ1ZSwiQ29uc2VudHMiOlsxLDMsNCwyXSwiVENTdHJpbmciOiJDUWpyczhBUWpyczhBR3lBQkJQTENkRXNBUF9nQUFBQUFCNVlLTHREN0Q3ZExXRmd3SHhuWUtzUU1JMWY4ZUNBWW9RQUJBYUJBU0FCU0FLUUlJUUdra0FRSkFTZ0JBQUNBQUlBS0NSQklRQU1BQUNBQ0VBQVFJQUFJUUFFQUFDUUFRZ0tBQUFFaUFBUUFBQVlBQUFpQ0lBQUFRQUlnRUlFRUJFQW1RaEFBQUlBRUZBQWpBQUVJQUFBQUFBQUFBQUFBd0FBQUFBQ0FBSUFBQUFBZ0NBQUFJQUFBQUFBQUVBQVFCZ0lFQUFBQUFFQUFBQUFBQUFBQVFBQUFCQUFBQUFJS0xnQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUJZS0FEQUFFRkZ3a0FHQUFJS0xob0FNQUFRVVhFUUFZQUFnb3VLZ0F3QUJCUmNaQUJnQUNDaTQ2QURBQUVGRnlFQUdBQUlLTGtvQU1BQVFVWEtRQVlBQWdvdVdnQXdBQkJSY0EuSUtMdEQ3RDdkTFdGZ3dIeG5ZS3NRTUkxZjhlQ0FZb1FBQkFhQkFTQUJTQUtRSUlRR2trQVFKQVNnQkFBQ0FBSUFLQ1JCSVFBTUFBQ0FDRUFBUUlBQUlRQUVBQUNRQVFnS0FBQUVpQUFRQUFBWUFBQWlDSUFBQVFBSWdFSUVFQkVBbVFoQUFBSUFFRkFBakFBRUlBQUFBQUFBQUFBQUF3QUFBQUFDQUFJQUFBQUFnQ0FBQUlBQUFBQUFBRUFBUUJnSUVBQUFBQUVBQUFBQUFBQUFBUUFBQUJBQUFBQUlBIiwiVmVyc2lvbiI6InYzIn0=; FPID=FPID2.2.%2F36IMxGNfil01a5mNzMzvVWpeVWedrwUavxkMOLknU8%3D; ga4_ga_K2N2M0CBQ6=GS2.2.s1777896663$o1$g0$t1777896665$j60$l0$h1102236686; FPLC=Vu%2BuakVLLIhm2A7qN4ewb91KGEQTp%2BjYj6ldbLpFixzQABzK2uz4Tj%2F2I0om0xLEqYbcNHlmafkit3GBAUJjg8CQ1xy5nfvvXNl7sZmqiQ6EnFM%3D"

}
all_opinions=[]
session = requests.Session(impersonate="chrome")
while next:
    
    url= f"https://www.ceneo.pl/{product_code}/opinie-{page}"
    print(page,next,url)
    r=session.get(url,headers=headers)
    
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
    print(len(all_opinions))
    json.dump(all_opinions,f, indent=4, ensure_ascii=False)