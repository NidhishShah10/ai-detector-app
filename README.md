# AI Essay Detector & Humanizer

## 📌 Problem Statement

With the rapid advancement of AI writing tools such as ChatGPT and Claude, it has become increasingly difficult to distinguish between human-written and AI-generated academic content. This creates challenges in educational environments where originality, authenticity, and critical thinking are essential.

There is a growing need for a system that can:

- Detect AI-generated text with a measurable confidence score  
- Help transform AI-like writing into more natural, human-sounding language  
- Provide iterative feedback showing measurable improvement  

This project aims to address these challenges through a full-stack web application.

---
- ## 🚀 Project Goals

- Build a functional full-stack AI-powered web application
- Provide measurable AI detection results
- Implement meaningful text transformation while preserving semantic content
- Evaluate system performance using real test data

## 💡 Proposed Method

The system provides two core features:

### 1. AI Detection
- Users paste an essay into the application.
- The text is analyzed using the Sapling AI Detection API.
- The system returns a score (0–100%) indicating the likelihood that the text is AI-generated.

### 2. Humanization
- If the text is flagged as likely AI-generated:
  - It is sent to the Anthropic Claude API.
  - The essay is rewritten to sound more natural and human-like while preserving the original meaning.
- The rewritten version is re-evaluated to verify that the AI detection score has improved.

This creates an iterative workflow:

Detect → Rewrite → Re-detect → Compare results

---

## 📊 Data Sources

This project uses the following data sources:
### APIs
- Sapling AI API – AI-generated text detection
- Anthropic Claude API – Natural language rephrasing
-
- ## 🛠️ Tech Stack

### Frontend
- React.js

### Backend
- Python Flask
