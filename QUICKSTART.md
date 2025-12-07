# 🚀 Quick Start Guide - AI ROI Canvas Agent

## Two Ways to Use This App

### 🎯 Method 1: Manual Mode (No API Key - Start Immediately!)

**Best for:** Quick testing, no API setup needed

1. **Install and run:**
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```

2. **In the sidebar, expand "➕ Quick Add Use Case (Demo)"**

3. **Add 5+ use cases:**
   - Title: e.g., "Customer Service Chatbot"
   - Problem: Brief description
   - Near Benefit: e.g., 150000
   - Long Benefit: e.g., 250000
   - Initial Cost: e.g., 50000
   - Effort: 1-10 scale
   - Click "Add Use Case"

4. **Progress through phases using sidebar buttons:**
   - ✅ Add 5+ use cases
   - 💰 Click "Compute ROI"
   - 🎯 Set effort budget, click "Select Portfolio"
   - 🗺️ Click "Generate Canvas"

5. **View your visual canvas!**
   - Go to Canvas tab
   - Select "📊 Visual Canvas" view

---

### 🤖 Method 2: Conversational AI Mode (With API Key)

**Best for:** Natural conversation, intelligent guidance

#### Step 1: Get API Key

1. Visit: https://console.anthropic.com/
2. Sign up (free tier available)
3. Create an API key
4. Copy the key (starts with `sk-ant-...`)

#### Step 2: Configure API Key

**Option A: Environment Variable (Recommended)**
```bash
# Mac/Linux:
export ANTHROPIC_API_KEY='sk-ant-your-key-here'

# Windows PowerShell:
$env:ANTHROPIC_API_KEY='sk-ant-your-key-here'

# Windows CMD:
set ANTHROPIC_API_KEY=sk-ant-your-key-here
```

**Option B: Streamlit Secrets** (for deployment)

Create `.streamlit/secrets.toml`:
```toml
ANTHROPIC_API_KEY = "sk-ant-your-key-here"
```

**Option C: In the App** (quick testing)

Just enter it in the sidebar when the app asks for it.

#### Step 3: Run the App

```bash
streamlit run app.py
```

#### Step 4: Chat Naturally!

The app will detect your API key automatically. Just start chatting:

```
You: "Hi, I work at TechCorp in manufacturing"

Agent: "Great to meet you! What are your main goals 
        for implementing AI at TechCorp?"

You: "We want to reduce operational costs"

Agent: "Perfect! Let's identify some AI use cases. 
        What's your biggest cost driver right now?"
```

The agent will:
- ✅ Ask intelligent follow-up questions
- ✅ Help you estimate costs if unsure
- ✅ Extract structured data automatically
- ✅ Guide you through all 4 phases
- ✅ Generate your canvas at the end

---

## 🔧 Troubleshooting

### "No API key configured" even though I set it

**Solution:**
```bash
# Make sure you set it BEFORE running the app:
export ANTHROPIC_API_KEY='your-key'
streamlit run app.py

# Verify it's set:
echo $ANTHROPIC_API_KEY
```

### "Module 'anthropic' not found"

**Solution:**
```bash
pip install anthropic
# or
pip install -r requirements.txt
```

### Agent not responding intelligently

**Check:**
1. ✅ API key is valid (test at console.anthropic.com)
2. ✅ You have credits in your Anthropic account
3. ✅ The app shows "✅ API Connected & Working" in sidebar
4. ✅ Internet connection is working

### Chat input not appearing

**Solution:** Make sure Streamlit is up to date:
```bash
pip install --upgrade streamlit
```

---

## 📊 See Example Output

Want to see what the final canvas looks like before starting?

```bash
# Open the example visual canvas:
open example_visual_canvas.html  # Mac
start example_visual_canvas.html  # Windows
xdg-open example_visual_canvas.html  # Linux
```

---

## 🎯 Recommended First-Time Workflow

1. **Start with Manual Mode** to understand the flow
   - Use "Quick Add Use Case" 
   - See how phases progress
   - Generate your first canvas

2. **Then Try Conversational Mode** for the full experience
   - Add your API key
   - Experience the intelligent interview
   - See how the agent extracts data

3. **Export Your Canvas**
   - Visual HTML (for presentations)
   - JSON (for integration)
   - Markdown (for documentation)

---

## 💡 Pro Tips

### For Quick Testing (No API)
- Use the manual mode with the sidebar
- Add fictional use cases to see the workflow
- Great for demos and understanding the structure

### For Real Projects (With API)
- Set the API key as environment variable
- Have your cost estimates ready (agent can help if not)
- Let the agent guide you conversationally
- Take your time - the agent remembers context

### For Best Results
- Be specific about your use cases
- Provide realistic cost estimates
- Think about both hard and soft benefits
- Consider dependencies between use cases

---

## 🆘 Still Need Help?

1. Check if API key is working:
   - Sidebar should show "✅ API Connected & Working"
   
2. Check console for errors:
   - Look at terminal where you ran `streamlit run app.py`
   
3. Try manual mode first:
   - Verify the app works without API
   - Then add API for conversational features

4. Verify installation:
   ```bash
   pip list | grep -E "streamlit|anthropic"
   # Should show both packages
   ```

---

## 📖 What Happens in Each Mode

### Manual Mode Flow:
1. You manually enter use case data in sidebar
2. App computes ROI using exact formulas
3. You set effort budget
4. App selects optimal portfolio
5. App generates visual canvas
6. You download HTML/JSON/Markdown

### Conversational Mode Flow:
1. Agent asks about your organization
2. You chat naturally about your needs
3. Agent asks questions about each use case
4. Agent extracts data as you talk
5. Agent guides you through ROI review
6. Agent helps select portfolio
7. Agent generates canvas
8. You download in your preferred format

---

**Ready to start?** 

Run: `streamlit run app.py` and choose your mode! 🚀
