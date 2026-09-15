# from src.tools.tools import web_search, scrape_url


# result1 = scrape_url.invoke("https://www.artificialintelligence-news.com")
# print(result1)

# result2 = web_search.invoke("Artificial Intelligence news")
# print(result2)


from src.pipelines.pipeline import run_research_pipeline


topic = "The impact of AI on the job market in 2026"
run_research_pipeline(topic)
