# main.py

import re
import requests
import openai
import os
from dotenv import load_dotenv
from xml.etree import ElementTree

# Load OpenAI API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function: Fetch papers from arXiv
def fetch_arxiv_papers(query, max_results=5):
    print(f"🔍 Searching arXiv for: {query}")
    base_url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code != 200:
        print("❌ Failed to fetch from arXiv.")
        return []

    root = ElementTree.fromstring(response.content)
    entries = root.findall('{http://www.w3.org/2005/Atom}entry')

    papers = []
    for entry in entries:
        title = entry.find('{http://www.w3.org/2005/Atom}title').text.strip()
        summary = entry.find('{http://www.w3.org/2005/Atom}summary').text.strip()
        link = entry.find('{http://www.w3.org/2005/Atom}id').text.strip()
        authors = [author.find('{http://www.w3.org/2005/Atom}name').text
                   for author in entry.findall('{http://www.w3.org/2005/Atom}author')]
        
        papers.append({
            "title": title,
            "summary": summary,
            "authors": authors,
            "link": link
        })

    return papers

# Function: Use OpenAI to summarize abstract
from openai import OpenAI

client = OpenAI()  # creates a default client using your API key from environment

def summarize_with_gpt(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert academic summarizer."},
                {"role": "user", "content": f"Summarize this academic abstract:\n{text}"}
            ],
            temperature=0.5,
            max_tokens=300
        )
        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        print(f"❌ Error: {e}")
        return "❌ Error generating summary."

# Function to create folders and save summaries
def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "_", name)

def save_summary(topic, paper, summary, index):
    folder_name = sanitize_filename(topic.strip())
    os.makedirs(folder_name, exist_ok=True)

    filename = f"{folder_name}/paper_{index}_{sanitize_filename(paper['title'][:40])}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Title: {paper['title']}\n")
        f.write(f"Authors: {', '.join(paper['authors'])}\n")
        f.write(f"Link: {paper['link']}\n\n")
        f.write("Summary:\n")
        f.write(summary)
    print(f"📁 Saved to: {filename}")

# Main agent function
def run_agent(research_topic):
    print(f"\n🧠 Researching topic: {research_topic}")
    
    papers = fetch_arxiv_papers(research_topic)

    if not papers:
        print("No papers found.")
        return

    for idx, paper in enumerate(papers, 1):
        print(f"\n📄 Paper {idx}")
        print(f"Title: {paper['title']}")
        print(f"Authors: {', '.join(paper['authors'])}")
        print(f"Link: {paper['link']}")
        
        print("📝 Generating AI summary...")
        ai_summary = summarize_with_gpt(paper['summary'])
        print(f"Summary: {ai_summary}")
       
        save_summary(research_topic, paper, ai_summary, idx)

# Entry point
if __name__ == "__main__":
    topic = input("Enter a research topic: ")
    run_agent(topic)


