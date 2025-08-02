🧠 AI Research Assistant

An autonomous research assistant powered by OpenAI and arXiv.  
It fetches academic papers based on a user-provided topic, summarizes their content using GPT, organizes the notes into local folders, and provides a user-friendly web interface via Gradio.

---

🚀 Features

- 🔎 Search recent academic papers from **arXiv**
- 🤖 Summarize abstracts using **OpenAI GPT (gpt-3.5-turbo)**
- 🗂️ Automatically save each summary as a `.txt` file in topic-based folders
- 🌐 Use via a **Gradio browser interface**

---


🛠️ Tech Stack

- Python 3
- OpenAI API (GPT-3.5)
- arXiv API (via RSS/XML)
- Gradio for UI
- `.env` for secret management

---


📂 Folder Structure

ai-research-assistant/ ├── app.py # Gradio web app ├── main.py # Core agent logic ├── .env # API key (not uploaded to GitHub) ├── .gitignore ├── README.md ├── research-topic-name/ # Auto-created folder for each topic │ ├── paper_1_title.txt │ ├── paper_2_title.txt
---


🧪 How to Run Locally

1. Clone the repo
```bash
git clone https://github.com/YOUR-USERNAME/ai-research-assistant.git
cd ai-research-assistant
2. Install dependencies
pip install -r requirements.txt
Or manually:
pip install openai gradio python-dotenv requests
3. Add your API key
Create a .env file with your OpenAI API key:
OPENAI_API_KEY=sk-...
4. Launch the Gradio app
python app.py


📦 Example Output
Inside a folder like graph neural networks/, you’ll find .txt files like:
Title: Graph Representation Learning with GNNs
Authors: John Doe, Jane Smith
Link: https://arxiv.org/abs/1234.5678

Summary:
This paper introduces...


💡 Future Improvements
	•	PDF export or ZIP download
	•	Support Semantic Scholar or PubMed
	•	Multi-layer summaries (e.g., key points, pros/cons, etc.)
	•	Asynchronous summarization for speed

🧑‍💻 Author
Built with ❤️ using OpenAI by Bhanu Pratap.

🛡️ Disclaimer
This project is for educational purposes. Always verify summaries against the original papers for accuracy.
---

