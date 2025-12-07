# 🚀 Deployment Guide - Streamlit Cloud

This guide shows how to deploy your AI ROI Canvas Agent to Streamlit Cloud with the API key configured in the backend (no UI prompt).

## Prerequisites

1. **GitHub repository** - Already set up at: https://github.com/Rriddhi/ai-roi-canvas-agent
2. **Streamlit Cloud account** - Free at https://streamlit.io/cloud
3. **Anthropic API key** - Get from https://console.anthropic.com/

## Step 1: Deploy to Streamlit Cloud

1. Go to **https://share.streamlit.io/**
2. Click **"New app"**
3. Select:
   - **Repository:** `Rriddhi/ai-roi-canvas-agent`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Click **"Deploy"**

Streamlit will deploy your app and assign a URL like:
```
https://ai-roi-canvas-agent.streamlit.app
```

## Step 2: Configure API Key (Backend)

### Option A: Using Streamlit Secrets (Recommended for Cloud)

1. Go to your app on Streamlit Cloud: https://share.streamlit.io/
2. Click on your app → **Settings** (gear icon)
3. Select **"Secrets"** tab
4. Add your API key:

```toml
ANTHROPIC_API_KEY = "sk-ant-your-actual-key-here"
```

5. Click **"Save"**
6. Streamlit will automatically redeploy

### Option B: Using Environment Variables (For Self-Hosted)

If deploying to your own server, set the environment variable:

```bash
export ANTHROPIC_API_KEY='sk-ant-your-key-here'
streamlit run app.py
```

### Option C: Docker Container (For Self-Hosted)

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}

CMD streamlit run app.py --server.port=8501 --server.address=0.0.0.0
```

Deploy with:
```bash
docker build -t ai-roi-canvas .
docker run -e ANTHROPIC_API_KEY='sk-ant-your-key' -p 8501:8501 ai-roi-canvas
```

## Step 3: Verify Backend Configuration

1. **Go to your deployed app:** https://ai-roi-canvas-agent.streamlit.app (or your URL)
2. **Check the sidebar:**
   - Should show **"🔑 API Key Configured (Backend)"** ✅
   - Should NOT show an input field for API key
   - Only shows "Change API Key" in expandable section

3. **Test the app:**
   - Start a conversation
   - Agent should respond with questions
   - No API key should be visible anywhere

## How It Works

**On Local Development:**
```bash
export ANTHROPIC_API_KEY='sk-ant-...'
streamlit run app.py
```
- App reads from environment variable
- Shows "🔑 API Key Configured (Backend)"
- No UI input needed

**On Streamlit Cloud:**
1. Secrets stored in `.streamlit/secrets.toml` (secure)
2. App auto-reads from `st.secrets` (or environment)
3. No API key shown in interface
4. No API key in repository

**For Users:**
- Interface shows ✅ API Connected & Working
- No need to enter API key
- Fully automated backend authentication

## Security Best Practices

✅ **DO:**
- Store API key in Streamlit Secrets (Streamlit Cloud)
- Store API key in environment variables (self-hosted)
- Never commit `.env` file to GitHub
- Use `.gitignore` to exclude sensitive files

❌ **DON'T:**
- Put API key in code
- Put API key in `app.py`
- Commit `ANTHROPIC_API_KEY` to GitHub
- Share API key in URLs or logs

## Troubleshooting Deployment

### "API Key not configured" message appears

**Solution:** 
1. Check Streamlit Cloud Secrets are saved
2. Wait 1-2 minutes for Streamlit to redeploy
3. Click "Rerun" in the app
4. If still not working, check the logs:
   - Click your app name on https://share.streamlit.io/
   - View deployment logs

### "API request failed / Authentication error"

**Causes & Solutions:**
- **Invalid key:** Verify the key is correct in Secrets
- **Key expired:** Get a fresh one from console.anthropic.com
- **Wrong key format:** Should start with `sk-ant-`

## Updating the Code

When you push changes to GitHub:

1. Update code locally
2. Commit and push:
   ```bash
   git add .
   git commit -m "Update: [description]"
   git push origin main
   ```
3. Streamlit Cloud auto-detects changes
4. App redeploys automatically (check logs)

## Checking Deployment Status

1. Go to https://share.streamlit.io/
2. Find your app in the list
3. Check status:
   - 🟢 Green = Deployed successfully
   - 🟡 Yellow = Deploying
   - 🔴 Red = Deployment failed (check logs)

## Example Deployed App

Your app is live at:
```
https://ai-roi-canvas-agent.streamlit.app
```

The interface will:
- ✅ Load instantly
- ✅ Show "API Key Configured (Backend)"
- ✅ No API key input field
- ✅ Agent ready to chat

## Support

- **Streamlit Cloud docs:** https://docs.streamlit.io/streamlit-cloud
- **Streamlit Secrets:** https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app#use-secrets-management
- **Anthropic API:** https://docs.anthropic.com/

---

**Your deployment is ready!** The app will use the backend API key automatically without prompting users.
