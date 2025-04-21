import os
import feedparser
from datetime import datetime
import pytz

# 设置东八区时区
tz_cn = pytz.timezone('Asia/Shanghai')
today = datetime.now(tz=tz_cn).date()

# 保存目录
SAVE_DIR = "articleResources"
os.makedirs(SAVE_DIR, exist_ok=True)

# RSS 新闻源，每个抓取最多 2 篇
rss_sources = {
    "Synced": "https://syncedreview.com/feed/",
    "The Decoder": "https://the-decoder.com/feed/",
    "VentureBeat AI": "https://venturebeat.com/category/ai/feed/",
    "MIT Tech Review AI": "https://www.technologyreview.com/feed/",
    "TechCrunch AI": "https://techcrunch.com/tag/artificial-intelligence/feed/",
    "IEEE Spectrum AI": "https://spectrum.ieee.org/rss/artificial-intelligence",
    "Ars Technica AI": "http://feeds.arstechnica.com/arstechnica/index/",
    "ZDNet AI": "https://www.zdnet.com/topic/artificial-intelligence/rss.xml",
    "NewScientist AI": "https://www.newscientist.com/subject/artificial-intelligence/feed/",
    "AI Trends": "https://www.aitrends.com/feed/",
    "Google AI Blog": "https://ai.googleblog.com/feeds/posts/default",
    "OpenAI Blog": "https://openai.com/blog/rss.xml",
    "Anthropic Blog": "https://www.anthropic.com/news/rss.xml",
    "Meta AI Blog": "https://ai.facebook.com/blog/rss/",
    "NVIDIA AI Blog": "https://blogs.nvidia.com/blog/category/ai/feed/",
}

# 判断文章是否是今天发布的
def is_today(pub_date):
    try:
        pub_dt = datetime(*pub_date[:6], tzinfo=pytz.utc).astimezone(tz_cn)
        return pub_dt.date() == today
    except Exception:
        return False

# 抓取并保存文章
article_count = 0
max_articles_per_source = 2

for source_name, rss_url in rss_sources.items():
    feed = feedparser.parse(rss_url)
    count = 0

    for entry in feed.entries:
        if hasattr(entry, 'published_parsed') and is_today(entry.published_parsed):
            article_count += 1
            count += 1

            title = entry.title
            link = entry.link
            published = datetime(*entry.published_parsed[:6], tzinfo=pytz.utc).astimezone(tz_cn)
            pub_time_str = published.strftime("%Y-%m-%d %H:%M:%S")
            summary = entry.summary if hasattr(entry, 'summary') else '暂无摘要'

            filename = os.path.join(SAVE_DIR, f"{article_count:02}.md")
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"# {title}\n")
                f.write(f"- 📅 来源: {source_name}\n")
                f.write(f"- 🕒 发布时间（东八区）: {pub_time_str}\n")
                f.write(f"- 🔗 [原文链接]({link})\n\n")
                f.write(summary)

            if count >= max_articles_per_source:
                break

print(f"✅ 共保存 {article_count} 篇文章到 `{SAVE_DIR}` 目录。")
