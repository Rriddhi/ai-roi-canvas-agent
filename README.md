# AI ROI & Roadmap Canvas Agent

An **intelligent conversational AI agent** that interviews you to build an AI portfolio and generates a comprehensive AI ROI & Roadmap Canvas with **professional visual layouts**.

## 🎨 Visual Canvas Generation!

The agent now creates **beautiful, professional visual canvases** that match the standard AI ROI & Roadmap Canvas format - not just JSON, but actual visual layouts you can view, print, and present!

## 🤖 What Makes This Intelligent?

Unlike static forms, this agent:
- **Conducts natural conversations** - Asks follow-up questions based on your responses
- **Understands context** - Remembers what you said and builds upon it
- **Guides you through phases** - Walks you through 4 structured phases conversationally
- **Helps with estimates** - Assists when you're uncertain about costs or benefits
- **Validates inputs** - Ensures data quality through intelligent questioning

## Features

- **Phase 1**: Conversational interview to collect use cases
- **Phase 2**: Automatic ROI computation with intelligent analysis
- **Phase 3**: AI-guided portfolio selection with recommendations
- **Phase 4**: Automated roadmap & canvas generation

## 📊 Output Formats

Your canvas can be exported in multiple formats:

1. **Visual HTML Canvas** - Professional layout matching industry standards (new!)
   - Beautiful, print-ready format
   - Matches the reference canvas layout
   - Can be opened in any browser
   - Perfect for presentations and reports

2. **JSON** - Structured data for integration with other tools

3. **Markdown** - Human-readable text format for documentation

## Installation & Running Locally

### Prerequisites
- Python 3.8 or higher
- Anthropic API key (the app uses Claude for conversations)

### Steps

1. **Extract the zip file**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   
   The app will prompt you to enter your Anthropic API key when you first run it.
   
   Alternatively, set it as an environment variable:
   ```bash
   export ANTHROPIC_API_KEY='your-api-key-here'
   ```
   
   Get your API key from: https://console.anthropic.com/

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   - The app will automatically open at `http://localhost:8501`

## How It Works

1. **Start a conversation** - The agent introduces itself and asks about your organization
2. **Natural dialogue** - Chat naturally about your AI use cases
3. **Guided process** - The agent ensures all necessary information is collected
4. **Automatic computation** - ROI metrics are calculated from your conversation
5. **Interactive refinement** - Discuss and adjust the portfolio selection
6. **Canvas generation** - Get your complete roadmap in JSON or Markdown

## Deployment

### Streamlit Community Cloud

1. Push this code to a GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository, branch, and `app.py`
6. Add your `ANTHROPIC_API_KEY` in the Secrets section
7. Click "Deploy"

### Replit

1. Go to [replit.com](https://replit.com)
2. Create a new Repl and import from GitHub
3. Add your API key to Secrets (key: `ANTHROPIC_API_KEY`)
4. Click "Run"

## Usage Tips

- **Be conversational** - Talk naturally, the agent understands context
- **Ask for help** - If unsure about estimates, ask the agent for guidance
- **Iterate** - You can refine your use cases through conversation
- **Review suggestions** - The agent provides intelligent recommendations
- **Choose your format** - View your canvas visually, as JSON, or as Markdown

### Generating Visual Canvas from JSON

You can also generate a visual canvas from an existing JSON file:

```bash
python generate_visual_canvas.py my_canvas.json
```

This will create `my_canvas_visual.html` that you can open in any browser!

## Technical Details

- **Conversational AI**: Uses Claude (Anthropic) for natural language understanding
- **Exact ROI Formulas**: All calculations follow the specification precisely
- **Context retention**: Agent remembers the entire conversation
- **Intelligent parsing**: Extracts structured data from natural language

## Privacy & Security

- Conversations are stored only in your browser session
- API calls go directly to Anthropic's servers
- No data is stored on any server
- Your API key is never logged or shared

## Author

Built for AI Strategy & Implementation Assignment
