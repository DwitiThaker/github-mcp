# 🤖 GitHub MCP Agent

A powerful AI-powered GitHub explorer built with **Streamlit**, **Agno**, and the **Model Context Protocol (MCP)**. This application allows you to chat with any GitHub repository using natural language to uncover bugs, analyze pull requests, and track development activity.

---

## 📖 About the Project

###  **What is this?**

This is not just a GitHub search tool; it is an **AI Agent** that understands the context of software development. Instead of manually clicking through tabs or writing complex API filters, you can simply ask: *"What are the most critical bugs in the login module?"* or *"Summarize the recent changes in the dev branch."* The AI analyzes the repository data and provides a human-readable synthesis.

###  **Why did we build it?**

* **The Problem:** Exploring large codebases is time-consuming. Finding "that one issue about the database" often involves endless scrolling and keyword guessing.

* **The Solution:** We needed a way to apply the reasoning capabilities of Large Language Models (LLMs) to live, dynamic data sources like GitHub, without hallucinations.

* **The Architecture:** We chose the **Model Context Protocol (MCP)** because it allows us to decouple the "Brain" (Python/Gemini) from the "Tools" (Node.js/GitHub API). This makes the system modular, secure, and extensible.

###  **How it Works**

1.  **User Input:** You ask a question in the Streamlit UI.

2.  **Agentic Reasoning:** The **Agno** framework sends your query to **Google Gemini 1.5 Flash**. The LLM decides *which* data it needs to answer you.

3.  **Tool Execution (MCP):**

    * Instead of writing custom API wrappers, the Python app connects to a standardized **MCP Server** (running locally via Node.js).

    * This server securely handles the GitHub API communication.

4.  **Synthesis:** The raw data (JSON) is sent back to Gemini, which interprets the technical details and generates a clear, Markdown-formatted answer.

---

## 🏗️ Architecture

This project demonstrates a "Hybrid Runtime" architecture:

1.  **Frontend (Python):** Streamlit manages the UI and the async event loop.

2.  **The Brain (Cloud):** Google Gemini 1.5 Flash provides high-speed reasoning and summarization.

3.  **The Bridge (MCP):** A standardized protocol that connects the Python client to the Node.js server.

4.  **The Tool (Node.js):** The `@modelcontextprotocol/server-github` runs as a subprocess, handling authentication and API calls to GitHub.

## ✨ Features

* **Natural Language Queries**: Ask questions like *"Show me the most recent bugs"* instead of manually filtering issues.

* **Deep Repository Analysis**:

    * **Issues**: Filter by labels, status, or content.

    * **Pull Requests**: Find PRs needing review or recently merged code.

    * **Activity**: Summarize commit trends and contributor health.

* **Secure**: Your GitHub Token is used only for the session and is not stored persistently.

* **Cross-Platform**: Works on Windows, macOS, and Linux (Streamlit Cloud ready).

---

## 🛠️ Tech Stack

* **UI Framework**: [Streamlit](https://streamlit.io/)

* **Agent Framework**: [Agno](https://github.com/agno-ai/agno) (formerly Phidata)

* **LLM**: Google Gemini 1.5 Flash

* **Protocol**: [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

* **MCP Server**: `@modelcontextprotocol/server-github` (Node.js)

---

## 🚀 Getting Started

### Prerequisites

1.  **Python 3.10+** installed.

2.  **Node.js & npm** installed (Required to run the MCP server).

    * Verify with `node -v` and `npm -v`.

3.  **API Keys**:

    * **GitHub Personal Access Token** (Classic or Fine-grained) with `repo` scope.

    * **Google Gemini API Key**.

### Installation

1.  **Clone the repository**:

    ```bash

    git clone [https://github.com/yourusername/github-mcp-agent.git](https://github.com/yourusername/github-mcp-agent.git)

    cd github-mcp-agent

    ```

2.  **Create a virtual environment**:

    ```bash

    python -m venv .venv

    # Windows

    .venv\Scripts\activate

    # Mac/Linux

    source .venv/bin/activate

    ```

3.  **Install dependencies**:

    ```bash

    pip install streamlit agno google-generativeai mcp python-dotenv

    ```

4.  **Set up environment variables**:

    Create a `.env` file in the root directory:

    ```env

    GEMINI_API_KEY=your_gemini_api_key_here

    # Optional: Pre-load GitHub token (or enter it in the UI)

    # GITHUB_TOKEN=your_github_token_here

    ```

### Running the App

```bash

streamlit  run  app.py
The application will open in your browser at `http://localhost:8501`.

* * * * *

🔧 Troubleshooting
------------------

**Error: `models/gemini-1.5-flash is not found`**

-   **Cause**: Outdated Google Generative AI library.

-   **Fix**: Run `pip install -U google-generativeai`.

**Error: `npx is not recognized`**

-   **Cause**: Node.js is not installed or not in your system PATH.

-   **Fix**: Install Node.js from [nodejs.org](https://nodejs.org/). Restart your terminal after installation.

**Error: `401 Bad Credentials`**

-   **Cause**: Your GitHub token is invalid or expired.

-   **Fix**: Generate a new token at GitHub Settings > Developer Settings > Personal Access Tokens. Ensure it has `repo` permissions.

📄 License
----------

MIT License.