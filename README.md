# 🔍 Smart Research Summarization Tool

A fast and intuitive AI-powered web application that generates high-quality summaries of research papers, abstracts, or any academic text using **Google's Gemini 1.5 Flash** model.

Built with **Streamlit** and **LangChain**, this tool allows users to paste text directly and customize the summary by type and length — perfect for researchers, students, and academics who want to quickly grasp key insights without reading full documents.

## 🌟 Key Features

- **Direct Text Input**: Paste abstracts, sections, or full research paper text into a spacious text area.
- **Customizable Summarization Types**:
  - General
  - Codebase
  - Contextual
  - Research (optimized for academic/scientific content)
  - Business
- **Adjustable Summary Length**:
  - Short
  - Medium
  - Long
- **Academic-Quality Output**: Prompt engineered to maintain objective tone, preserve technical terms, highlight methodology, key findings, and implications.
- **Simple & Clean Interface**: Powered by Streamlit for instant local deployment and ease of use.
- **Error Handling & Feedback**: Clear warnings and loading indicators.

## 🛠 Tech Stack

- **Python** 3.8+
- **Streamlit** – Interactive frontend
- **LangChain** – Prompt templating and LLM orchestration
- **Google Gemini 1.5 Flash** (`gemini-1.5-flash`) – Fast, capable, and cost-effective model
- **python-dotenv** – Secure API key management
- <img width="1024" height="1024" alt="Gemini_Generated_Image_s8j9vis8j9vis8j9" src="https://github.com/user-attachments/assets/612cf545-220c-49c4-9319-8df32b7cc3e5" />

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google API Key with access to Gemini (obtain from https://aistudio.google.com/)

### Installation & Setup

1. Clone the repository
   git clone https://github.com/Rashid-Shocho/Research_Paper_Summarizer.git
   cd Research_Paper_Summarizer

2. Create a .env file in the project root
   GOOGLE_API_KEY=your_actual_google_api_key_here

3. Install required packages
   pip install streamlit langchain-google-genai python-dotenv

4. Run the application
   streamlit run app.py

   Note: If your main script is named differently (e.g., prompt_ui.py), use:
   streamlit run prompt_ui.py

5. Open the app
   Open the provided local URL (usually http://localhost:8501) in your browser.

## 📝 How to Use

- Paste your research text (abstract, introduction, full paper content, etc.) into the text area.
- Select the summarization type — choose Research for best results with academic papers.
- Choose your preferred summary length.
- Click Generate Summary.
- View the polished, structured summary in the output box.

## ⚙️ Important Notes

- This version works with pasted text only (no PDF upload support).
- Performs best with well-structured academic content.
- Uses gemini-1.5-flash for speed and efficiency.
- Keep input text reasonable in length to stay within model token limits.

## 📄 License

MIT License — free to use, modify, and distribute.
