import gradio as gr
from main import fetch_arxiv_papers, summarize_with_gpt, sanitize_filename, save_summary

def research_assistant(topic):
    papers = fetch_arxiv_papers(topic)
    if not papers:
        return "No papers found."

    results = []
    for idx, paper in enumerate(papers, 1):
        summary = summarize_with_gpt(paper['summary'])
        save_summary(topic, paper, summary, idx) 
        results.append(f"### Paper {idx}: {paper['title']}\n"
                       f"**Authors:** {', '.join(paper['authors'])}\n"
                       f"[Link to paper]({paper['link']})\n\n"
                       f"**Summary:**\n{summary}\n")
    return "\n---\n".join(results)

iface = gr.Interface(
    fn=research_assistant,
    inputs=gr.Textbox(label="Enter Research Topic"),
    outputs=gr.Markdown(label="Summaries"),
    title="AI Research Assistant",
    description="Enter a topic to fetch and summarize recent academic papers."
)

if __name__ == "__main__":
    iface.launch()