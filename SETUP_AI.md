# Enabling Full AI Intelligence

This app is designed to use Claude AI for intelligent conversations. Here's how to enable it:

## Step 1: Get Your Anthropic API Key

1. Go to https://console.anthropic.com/
2. Sign up or log in
3. Navigate to "API Keys"
4. Create a new key
5. Copy the key (starts with `sk-ant-...`)

## Step 2: Configure the API Key

### Option A: Environment Variable (Recommended for local development)

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
streamlit run app.py
```

### Option B: Streamlit Secrets (Recommended for deployment)

Create `.streamlit/secrets.toml`:

```toml
ANTHROPIC_API_KEY = "your-api-key-here"
```

### Option C: Enter in App (Quick testing)

The app will prompt you to enter your API key when you first run it.

## Step 3: Enable Claude API Calls in Code

In `app.py`, the `call_claude()` function has the actual API code commented out.

**Uncomment these lines** (around line 48-56):

```python
from anthropic import Anthropic
client = Anthropic(api_key=api_key)
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4000,
    system=AGENT_SYSTEM_PROMPT,
    messages=messages
)
return response.content[0].text
```

**Comment out or remove the demo response** (lines 58-70).

## Step 4: Test the Conversational Agent

Run the app and start chatting:

```bash
streamlit run app.py
```

The agent will now:
- ✅ Understand natural language
- ✅ Ask follow-up questions based on your responses
- ✅ Remember context from the entire conversation
- ✅ Help estimate costs and benefits
- ✅ Extract structured data from your responses
- ✅ Guide you through all 4 phases intelligently

## What the Agent Does

The agent uses the system prompt in `src/agent_prompt.py` which instructs it to:

1. **Phase 1** - Conduct a natural interview to collect use cases
2. **Phase 2** - Present ROI analysis conversationally
3. **Phase 3** - Discuss portfolio selection with recommendations
4. **Phase 4** - Generate the final canvas

## Demo Mode (Without API Key)

If you want to test the app structure without an API key:
- Use the "Quick Add Use Case" feature in the sidebar
- Manually progress through phases using sidebar buttons
- The computational logic (ROI, portfolio, canvas) works without API calls

## API Costs

Claude API pricing (as of 2024):
- Input: ~$3 per million tokens
- Output: ~$15 per million tokens

A typical canvas session uses ~10-20K tokens total = ~$0.30-0.60

## Troubleshooting

**"Error calling AI"**
- Check your API key is valid
- Ensure you have credits in your Anthropic account
- Verify internet connection

**"Module 'anthropic' not found"**
- Run: `pip install anthropic`
- Check requirements.txt is installed

**Agent not extracting data**
- The agent should output special XML tags like `<USE_CASE_DATA>`
- Check the system prompt is being used
- Verify the extraction regex in `extract_data_blocks()`

## Advanced: Customizing the Agent

Edit `src/agent_prompt.py` to:
- Change the conversation style
- Modify what questions are asked
- Adjust data extraction format
- Add industry-specific guidance
