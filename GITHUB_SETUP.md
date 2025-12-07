# 📤 GitHub Upload Instructions

## Prerequisites
- GitHub account (create one at https://github.com if needed)
- Git installed on your Mac (check: `git --version`)

## Step 1: Create Repository on GitHub

1. **Go to GitHub.com**
   - Click "+" in top right → "New repository"

2. **Configure Repository:**
   - **Repository name:** `ai-roi-canvas-agent`
   - **Description:** "Intelligent conversational AI agent for building AI ROI & Roadmap Canvases"
   - **Visibility:** Public (so professors can view it)
   - **Initialize repository:** Leave unchecked (we'll push existing code)
   - Click **"Create repository"**

3. **Copy the HTTPS URL** from the page (looks like: `https://github.com/YOUR-USERNAME/ai-roi-canvas-agent.git`)

## Step 2: Initialize Git in Your Project

```bash
cd "/Users/smridhipatwari/Desktop/AIM Carnegie Mellon/Courses /Operationalizing AI/Assignments/ai_roi_canvas_app_v3"

# Initialize git
git init

# Configure git (if first time)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: AI ROI Canvas Agent with conversational AI, financial modeling, and visual canvas generation"

# Add remote repository (replace URL with yours)
git remote add origin https://github.com/YOUR-USERNAME/ai-roi-canvas-agent.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

## Step 3: Verify Upload

1. **Go to your GitHub repository URL** (https://github.com/YOUR-USERNAME/ai-roi-canvas-agent)
2. **Verify these files are present:**
   - ✅ `app.py`
   - ✅ `requirements.txt` (updated)
   - ✅ `DESIGN_REPORT.md` (your assignment document)
   - ✅ `README.md`
   - ✅ `QUICKSTART.md`
   - ✅ `src/` folder with all modules
   - ✅ `.gitignore`
   - ✅ `.env.example`

## Step 4: Add GitHub-Specific Files (Optional but Recommended)

Create `LICENSE` file for academic/open-source project:

```bash
cd "/Users/smridhipatwari/Desktop/AIM Carnegie Mellon/Courses /Operationalizing AI/Assignments/ai_roi_canvas_app_v3"
```

Then create a file named `LICENSE` with MIT license text (or Apache 2.0).

## Full Commands - Copy & Paste Ready

```bash
#!/bin/bash
cd "/Users/smridhipatwari/Desktop/AIM Carnegie Mellon/Courses /Operationalizing AI/Assignments/ai_roi_canvas_app_v3"

# Initialize git
git init
git config --global user.name "Smridhi Patwari"
git config --global user.email "your.email@andrew.cmu.edu"

# Add all files
git add .

# Create commit
git commit -m "Initial commit: AI ROI Canvas Agent - Intelligent conversational agent for AI portfolio planning and visual canvas generation"

# Add remote (REPLACE WITH YOUR GITHUB URL)
git remote add origin https://github.com/YOUR-USERNAME/ai-roi-canvas-agent.git

# Rename to main and push
git branch -M main
git push -u origin main
```

## Troubleshooting

### "fatal: not a git repository"
```bash
# Make sure you're in the correct directory
cd "/Users/smridhipatwari/Desktop/AIM Carnegie Mellon/Courses /Operationalizing AI/Assignments/ai_roi_canvas_app_v3"
pwd  # Verify you're in the right place
git init
```

### "authentication failed" when pushing
```bash
# Use GitHub token instead of password
# 1. Go to https://github.com/settings/tokens
# 2. Create "Personal access token" (classic)
# 3. Give it "repo" permissions
# 4. Copy the token
# 5. When prompted for password, paste the token instead
```

### "origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/YOUR-USERNAME/ai-roi-canvas-agent.git
```

## What Gets Uploaded

✅ **Included:**
- All Python source code
- Documentation (README, QUICKSTART, DESIGN_REPORT)
- Requirements.txt
- Examples (JSON, HTML canvas)
- Configuration files

❌ **Excluded (by .gitignore):**
- `__pycache__/` (Python cache)
- `.venv/` (Virtual environment)
- `.env` (API keys - never commit these!)
- `.streamlit/secrets.toml` (Credentials)
- IDE files (`.vscode/`, `.idea/`)

## GitHub README Tips

Your `README.md` is perfect - it will display automatically on your GitHub page. Make sure it includes:
- ✅ What the project does (conversational AI agent)
- ✅ Features (discovery, ROI, portfolio, canvas)
- ✅ How to install and run
- ✅ Example usage
- ✅ Export formats supported

## For Assignment Submission

When submitting to your professor:

1. **Provide the GitHub URL:**
   ```
   https://github.com/YOUR-USERNAME/ai-roi-canvas-agent
   ```

2. **Mention key files:**
   - `DESIGN_REPORT.md` - Your system design document
   - `README.md` - Project overview
   - `app.py` - Main application
   - `src/` - All modules (agent, canvas, ROI, portfolio)

3. **Point to documentation:**
   - QUICKSTART.md for running instructions
   - SETUP_AI.md for API configuration

---

**Ready?** Run the commands above to push your project to GitHub! 🚀
