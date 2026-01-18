# 🤖 GitHub MCP Agent

A powerful AI-powered GitHub explorer built with **Streamlit**, **Agno**, and the **Model Context Protocol (MCP)**. This application allows you to chat with any GitHub repository using natural language to uncover bugs, analyze pull requests, and track development activity.

<div align="center">
  <img width="100%" alt="GitHub MCP Agent Interface - Main Dashboard" src="https://github.com/user-attachments/assets/bb146f9f-6b75-42a6-972a-20ccdb1eecc5" />
  <br>
  <em>Chat with your codebase: Ask questions and get real-time insights.</em>
</div>

---

## 📖 About the Project

### **What is this?**
This is not just a GitHub search tool; it is an **AI Agent** that understands the context of software development. Instead of manually clicking through tabs or writing complex API filters, you can simply ask: *"What are the most critical bugs in the login module?"* or *"Summarize the recent changes in the dev branch."* The AI analyzes the repository data and provides a human-readable synthesis.

### **Why did we build it?**
* **The Problem:** Exploring large codebases is time-consuming. Finding "that one issue about the database" often involves endless scrolling and keyword guessing.
* **The Solution:** We needed a way to apply the reasoning capabilities of Large Language Models (LLMs) to live, dynamic data sources like GitHub, without hallucinations.
* **The Architecture:** We chose the **Model Context Protocol (MCP)** because it allows us to decouple the "Brain" (Python/Gemini) from the "Tools" (Node.js/GitHub API). This makes the system modular, secure, and extensible.

### **How it Works**
1. **User Input:** You ask a question in the Streamlit UI.
2. **Agentic Reasoning:** The **Agno** framework sends your query to **Google Gemini 1.5 Flash**. The LLM decides *which* data it needs to answer you.
3. **Tool Execution (MCP):**
   * Instead of writing custom API wrappers, the Python app connects to a standardized **MCP Server** (running locally via Node.js).
   * This server securely handles the GitHub API communication.
4. **Synthesis:** The raw data (JSON) is sent back to Gemini, which interprets the technical details and generates a clear, Markdown-formatted answer.

<div align="center">
  <img width="100%" alt="Detailed Analysis Results" src="https://github.com/user-attachments/assets/5056f09d-f7c0-48d4-b1be-91a872a2be64" />
  <br><br>
  <img width="80%" alt="Features Breakdown" src="https://github.com/user-attachments/assets/b18b4bc6-5da0-4847-8394-aa182dca39c3" />
  <br>
  <em>The agent analyzes code, issues, and PRs to provide structured, synthesized answers.</em>
</div>

---

## 🏗️ Architecture

This project demonstrates a "Hybrid Runtime" architecture:

1. **Frontend (Python):** Streamlit manages the UI and the async event loop.
2. **The Brain (Cloud):** Google Gemini 1.5 Flash provides high-speed reasoning and summarization.
3. **The Bridge (MCP):** A standardized protocol that connects the Python client to the Node.js server.
4. **The Tool (Node.js):** The `@modelcontextprotocol/server-github` runs as a subprocess, handling authentication and API calls to GitHub.

---

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

## 🚀 How to Use

![How to use the app instructions](YOUR_IMAGE_URL_HERE)

1. **Authentication**: Enter your GitHub Token.
2. **Target**: Specify the repository URL (e.g., `https://github.com/owner/repo`).
3. **Query**: Select a template or type your own custom question.
4. **Run**: Click "Run Query" to get your insights.

---

## 📄 License

MIT License.
