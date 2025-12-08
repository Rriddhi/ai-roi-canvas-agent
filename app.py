"""
AI ROI & Roadmap Canvas Agent - Conversational AI Application

An intelligent agent that conducts interviews to build AI portfolios.
"""

import streamlit as st
import json
import re
import os
import pandas as pd
from datetime import datetime
from src.agent_prompt import AGENT_SYSTEM_PROMPT
from src.roi_calculations import compute_all_roi
from src.portfolio_logic import select_portfolio
from src.canvas_builder import build_canvas, canvas_to_markdown
from src.visual_canvas import generate_visual_canvas_html
from src.png_export import get_png_bytes

# Page configuration
st.set_page_config(
    page_title="AI ROI Canvas Agent - Conversational AI",
    page_icon="🤖",
    layout="wide"
)


def initialize_session_state():
    """Initialize session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "use_cases" not in st.session_state:
        st.session_state.use_cases = []
    if "org_info" not in st.session_state:
        st.session_state.org_info = {}
    if "roi_computed" not in st.session_state:
        st.session_state.roi_computed = False
    if "portfolio" not in st.session_state:
        st.session_state.portfolio = None
    if "canvas" not in st.session_state:
        st.session_state.canvas = None
    if "phase" not in st.session_state:
        st.session_state.phase = "interview"
    if "api_key" not in st.session_state:
        # Check environment variables for API key (for deployed apps)
        st.session_state.api_key = (
            os.environ.get("ANTHROPIC_API_KEY") or 
            os.environ.get("anthropic_api_key") or
            ""
        )
    if "api_enabled" not in st.session_state:
        st.session_state.api_enabled = False
    
    # Initialize widget keys for form inputs
    if "quick_title" not in st.session_state:
        st.session_state.quick_title = ""
    if "quick_problem" not in st.session_state:
        st.session_state.quick_problem = ""
    if "quick_near_b" not in st.session_state:
        st.session_state.quick_near_b = 0
    if "quick_long_b" not in st.session_state:
        st.session_state.quick_long_b = 0
    if "quick_init" not in st.session_state:
        st.session_state.quick_init = 0
    if "quick_effort" not in st.session_state:
        st.session_state.quick_effort = 3


def call_claude(messages, api_key):
    """Call Claude API for conversational responses."""
    if not api_key:
        return """⚠️ **API Key Required for Conversational Intelligence**

I need an Anthropic API key to have intelligent conversations with you.

**Option 1: Set Environment Variable (Recommended)**
```bash
export ANTHROPIC_API_KEY='your-key-here'
```

**Option 2: Enter in Sidebar**
Enter your API key in the sidebar text box.

**Option 3: Use Manual Entry**
You can still use the "Quick Add Use Case" feature in the sidebar to manually enter data without an API key.

Get your API key from: https://console.anthropic.com/"""
    
    try:
        from anthropic import Anthropic
        
        client = Anthropic(api_key=api_key)
        
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4000,
            system=AGENT_SYSTEM_PROMPT,
            messages=messages
        )
        
        # Mark API as enabled on successful call
        st.session_state.api_enabled = True
        
        return response.content[0].text
        
    except ImportError:
        return """⚠️ **Anthropic SDK Not Installed**

Please install it with:
```bash
pip install anthropic
```

Then restart the app."""
        
    except TypeError as e:
        if "proxies" in str(e):
            return """⚠️ **SDK Version Mismatch**

The Anthropic library is being redeployed. Please wait 2-3 minutes and refresh the page.

If this persists, the app may need to clear its cache on Streamlit Cloud."""
        else:
            raise
        
    except Exception as e:
        error_msg = str(e)
        if "api_key" in error_msg.lower() or "authentication" in error_msg.lower():
            return f"""⚠️ **Invalid API Key**

Your API key appears to be invalid or expired.

Error: {error_msg}

Please check your key at: https://console.anthropic.com/"""
        else:
            return f"""⚠️ **API Error**

Error: {error_msg}

If this persists, try:
1. Check your internet connection
2. Verify your API key is valid
3. Check you have API credits available"""


def extract_data_blocks(text):
    """Extract structured data from agent responses."""
    use_case_pattern = r'<USE_CASE_DATA>(.*?)</USE_CASE_DATA>'
    org_pattern = r'<ORG_DATA>(.*?)</ORG_DATA>'
    budget_pattern = r'<EFFORT_BUDGET>(.*?)</EFFORT_BUDGET>'
    canvas_pattern = r'<GENERATE_CANVAS>(.*?)</GENERATE_CANVAS>'
    
    use_cases = re.findall(use_case_pattern, text, re.DOTALL)
    org_data = re.findall(org_pattern, text, re.DOTALL)
    budget_data = re.findall(budget_pattern, text, re.DOTALL)
    canvas_trigger = re.findall(canvas_pattern, text, re.DOTALL)
    
    return {
        'use_cases': [json.loads(uc) for uc in use_cases],
        'org_data': json.loads(org_data[0]) if org_data else None,
        'effort_budget': json.loads(budget_data[0]) if budget_data else None,
        'generate_canvas': len(canvas_trigger) > 0
    }


def render_sidebar():
    """Render sidebar with progress and controls."""
    with st.sidebar:
        st.title("🤖 AI Canvas Agent")
        st.markdown("---")
        
        # API Key status - Check environment first, then session
        env_api_key = os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("anthropic_api_key")
        
        if env_api_key or st.session_state.api_key:
            # API key is configured (from environment or session)
            if st.session_state.api_enabled:
                st.success("✅ API Connected & Working")
            else:
                st.info("🔑 API Key Configured (Backend)")
            
            # Option to change key (hidden by default)
            with st.expander("🔧 Change API Key"):
                new_key = st.text_input(
                    "New API Key",
                    type="password",
                    help="Enter a new API key to replace the current one"
                )
                if new_key and st.button("Update Key"):
                    st.session_state.api_key = new_key
                    st.session_state.api_enabled = False
                    st.success("Key updated! Send a message to test it.")
                    st.rerun()
        else:
            # No API key in environment or session - show input only as fallback
            st.warning("⚠️ No API Key Configured")
            st.caption("Enter your Anthropic API key to enable conversational intelligence")
            
            api_key_input = st.text_input(
                "Anthropic API Key",
                type="password",
                help="Get your key at console.anthropic.com",
                placeholder="sk-ant-..."
            )
            if api_key_input:
                st.session_state.api_key = api_key_input
                st.session_state.api_enabled = False
                st.success("✅ Key saved! Try sending a message.")
                st.rerun()
            
            st.caption("💡 Or set ANTHROPIC_API_KEY environment variable")
        
        st.markdown("---")
        
        # Progress
        st.markdown("### Progress")
        st.markdown(f"**Phase:** {st.session_state.phase.title()}")
        st.markdown(f"**Use Cases:** {len(st.session_state.use_cases)}")
        st.markdown(f"**ROI Computed:** {'✅' if st.session_state.roi_computed else '⬜'}")
        st.markdown(f"**Portfolio Selected:** {'✅' if st.session_state.portfolio else '⬜'}")
        st.markdown(f"**Canvas Generated:** {'✅' if st.session_state.canvas else '⬜'}")
        
        st.markdown("---")
        
        # Quick add use case (for demo/testing)
        with st.expander("➕ Quick Add Use Case (Demo)"):
            st.caption("For testing without full conversation")
            
            uc_title = st.text_input("Title", key="quick_title")
            uc_problem = st.text_area("Problem", key="quick_problem", height=100)
            
            col1, col2 = st.columns(2)
            with col1:
                near_benefit = st.number_input("Near Benefit ($)", 0, key="quick_near_b")
                initial_cost = st.number_input("Initial Cost ($)", 0, key="quick_init")
            with col2:
                long_benefit = st.number_input("Long Benefit ($)", 0, key="quick_long_b")
                effort = st.slider("Effort", 1, 10, 3, key="quick_effort")
            
            if st.button("Add Use Case"):
                new_uc = {
                    "id": f"UC{len(st.session_state.use_cases) + 1:03d}",
                    "title": uc_title,
                    "problem": uc_problem,
                    "kpis": ["Efficiency", "Cost savings"],
                    "expected_benefits": {
                        "near_term_annual_benefit": float(near_benefit),
                        "long_term_annual_benefit": float(long_benefit),
                        "soft_benefits": ["Improved operations"]
                    },
                    "costs": {
                        "initial_cost": float(initial_cost),
                        "near_term_annual_cost": initial_cost * 0.2,
                        "long_term_annual_cost": initial_cost * 0.15
                    },
                    "effort_score_1_to_10": effort,
                    "risk": {
                        "probability_0_to_1": 0.2,
                        "impact_0_to_1": 0.3,
                        "risks_list": ["Implementation risk", "Adoption risk"]
                    },
                    "dependencies": []
                }
                st.session_state.use_cases.append(new_uc)
                st.success(f"Added {uc_title}!")
                st.rerun()
        
        st.markdown("---")
        
        # Phase controls
        if len(st.session_state.use_cases) >= 5 and not st.session_state.roi_computed:
            if st.button("💰 Compute ROI", use_container_width=True):
                st.session_state.use_cases = compute_all_roi(st.session_state.use_cases)
                st.session_state.roi_computed = True
                st.session_state.phase = "roi"
                st.rerun()
        
        if st.session_state.roi_computed and not st.session_state.portfolio:
            budget = st.number_input("Effort Budget", 1, 100, 20, key="budget_input")
            if st.button("🎯 Select Portfolio", use_container_width=True):
                st.session_state.portfolio = select_portfolio(
                    st.session_state.use_cases,
                    budget
                )
                st.session_state.phase = "portfolio"
                st.rerun()
        
        if st.session_state.portfolio and not st.session_state.canvas:
            if st.button("🗺️ Generate Canvas", use_container_width=True):
                org = st.session_state.org_info or {}
                st.session_state.canvas = build_canvas(
                    st.session_state.use_cases,
                    st.session_state.portfolio,
                    org_name=org.get("organization_name", org.get("name", "")),
                    org_team=org.get("team_name", org.get("team", "")),
                    designed_by=org.get("designed_by", ""),
                    designed_for=org.get("designed_for", ""),
                    primary_goal=org.get("primary_goal", ""),
                    strategic_focus=org.get("strategic_focus", "")
                )
                st.session_state.phase = "canvas"
                st.rerun()
        
        st.markdown("---")
        
        if st.button("🔄 Start Over"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()


def render_chat_interface():
    """Render the main chat interface."""
    st.title("🤖 AI ROI & Roadmap Canvas Agent")
    st.caption("Your intelligent AI strategy consultant")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            # Clean XML tags from assistant messages before displaying
            content = message["content"]
            if message["role"] == "assistant":
                content = re.sub(r'<USE_CASE_DATA>.*?</USE_CASE_DATA>', '', content, flags=re.DOTALL)
                content = re.sub(r'<ORG_DATA>.*?</ORG_DATA>', '', content, flags=re.DOTALL)
                content = re.sub(r'<EFFORT_BUDGET>.*?</EFFORT_BUDGET>', '', content, flags=re.DOTALL)
                content = re.sub(r'<GENERATE_CANVAS>.*?</GENERATE_CANVAS>', '', content, flags=re.DOTALL)
            st.markdown(content)
    
    # Chat input
    if prompt := st.chat_input("Type your message..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get agent response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # Prepare messages for API
                api_messages = [
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ]
                
                response = call_claude(api_messages, st.session_state.api_key)
                
                # Extract any data blocks before displaying
                extracted = extract_data_blocks(response)
                
                # Remove XML data blocks from display text
                display_text = response
                display_text = re.sub(r'<USE_CASE_DATA>.*?</USE_CASE_DATA>', '', display_text, flags=re.DOTALL)
                display_text = re.sub(r'<ORG_DATA>.*?</ORG_DATA>', '', display_text, flags=re.DOTALL)
                display_text = re.sub(r'<EFFORT_BUDGET>.*?</EFFORT_BUDGET>', '', display_text, flags=re.DOTALL)
                display_text = re.sub(r'<GENERATE_CANVAS>.*?</GENERATE_CANVAS>', '', display_text, flags=re.DOTALL)
                
                st.markdown(display_text)
        
        # Add assistant response
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        if extracted['use_cases']:
            st.session_state.use_cases.extend(extracted['use_cases'])
        
        if extracted['org_data']:
            st.session_state.org_info = extracted['org_data']
        
        if extracted['effort_budget']:
            # Compute ROI first if not already done
            if not st.session_state.roi_computed:
                st.session_state.use_cases = compute_all_roi(st.session_state.use_cases)
                st.session_state.roi_computed = True
            
            budget = extracted['effort_budget']['budget']
            st.session_state.portfolio = select_portfolio(
                st.session_state.use_cases,
                budget
            )
        
        if extracted['generate_canvas']:
            # Ensure ROI is computed before generating canvas
            if not st.session_state.roi_computed:
                st.session_state.use_cases = compute_all_roi(st.session_state.use_cases)
                st.session_state.roi_computed = True
            
            # Ensure portfolio is selected before generating canvas
            if not st.session_state.portfolio:
                st.error("Portfolio must be selected before generating canvas")
                st.rerun()
                return
            
            org = st.session_state.org_info or {}
            st.session_state.canvas = build_canvas(
                st.session_state.use_cases,
                st.session_state.portfolio,
                org_name=org.get("organization_name", org.get("name", "")),
                org_team=org.get("team_name", org.get("team", "")),
                designed_by=org.get("designed_by", ""),
                designed_for=org.get("designed_for", ""),
                primary_goal=org.get("primary_goal", ""),
                strategic_focus=org.get("strategic_focus", "")
            )
        
        st.rerun()
    
    # Initial greeting if no messages
    if not st.session_state.messages:
        with st.chat_message("assistant"):
            if st.session_state.api_key:
                greeting = """👋 Hi! I'm your AI ROI & Roadmap Canvas Agent.

I'll guide you through building your AI portfolio in 4 phases:
1. **Interview** - We'll discuss your organization and AI use cases
2. **ROI Analysis** - I'll compute financial metrics
3. **Portfolio Selection** - We'll pick the best use cases
4. **Canvas Generation** - I'll create your complete roadmap

Let's start! Tell me about your organization:
- What's your company name?
- What industry are you in?
- What are your goals for AI implementation?"""
            else:
                greeting = """👋 Hi! I'm your AI ROI & Roadmap Canvas Agent.

⚠️ **API Key Required**: I need an Anthropic API key to have intelligent conversations.

**Quick Options:**
1. 🔑 **Enter API key** in the sidebar to enable conversational mode
2. ➕ **Use "Quick Add Use Case"** in the sidebar to manually enter data (no API needed)
3. 🌐 **Set environment variable**: `export ANTHROPIC_API_KEY='your-key'`

Get your free API key at: https://console.anthropic.com/

Once you have a key, I can guide you through an intelligent interview process!"""
            
            st.markdown(greeting)
            st.session_state.messages.append({
                "role": "assistant",
                "content": greeting
            })


def render_results_tabs():
    """Render tabs showing current progress and results."""
    if st.session_state.use_cases or st.session_state.roi_computed or st.session_state.portfolio or st.session_state.canvas:
        st.markdown("---")
        
        tabs = []
        if st.session_state.use_cases:
            tabs.append("📋 Use Cases")
        if st.session_state.roi_computed:
            tabs.append("💰 ROI Analysis")
        if st.session_state.portfolio:
            tabs.append("🎯 Portfolio")
        if st.session_state.canvas:
            tabs.append("🗺️ Canvas")
        
        if tabs:
            tab_objects = st.tabs(tabs)
            tab_idx = 0
            
            # Use Cases Tab
            if "📋 Use Cases" in tabs:
                with tab_objects[tab_idx]:
                    st.subheader(f"Collected Use Cases ({len(st.session_state.use_cases)})")
                    for uc in st.session_state.use_cases:
                        with st.expander(f"**{uc.get('id', 'UC')}: {uc.get('title', 'Untitled')}**"):
                            st.write(f"**Problem:** {uc.get('problem', 'N/A')}")
                            st.write(f"**Effort:** {uc.get('effort_score_1_to_10', 'N/A')}/10")
                            benefits = uc.get('expected_benefits', {}) or {}
                            near_benefit = benefits.get('near_term_annual_benefit', 0) or 0
                            long_benefit = benefits.get('long_term_annual_benefit', 0) or 0
                            st.write(f"**Near-term Benefit:** ${near_benefit:,.0f}")
                            st.write(f"**Long-term Benefit:** ${long_benefit:,.0f}")
                tab_idx += 1
            
            # ROI Tab
            if "💰 ROI Analysis" in tabs:
                with tab_objects[tab_idx]:
                    st.subheader("ROI Analysis Results")
                    df_data = []
                    for uc in st.session_state.use_cases:
                        df_data.append({
                            "Use Case": uc.get("title", "Untitled"),
                            "Near-term ROI": f"{uc.get('near_term_roi_percent', 0):.1f}%",
                            "Long-term ROI": f"{uc.get('long_term_roi_percent', 0):.1f}%",
                            "NPV": f"${uc.get('npv_10_percent', 0):,.0f}",
                            "Payback": uc.get('payback_period_years', 'N/A'),
                            "Risk-Adj Value": f"${uc.get('risk_adjusted_value', 0):,.0f}"
                        })
                    st.dataframe(pd.DataFrame(df_data), use_container_width=True, hide_index=True)
                tab_idx += 1
            
            # Portfolio Tab
            if "🎯 Portfolio" in tabs:
                with tab_objects[tab_idx]:
                    st.subheader("Selected Portfolio")
                    portfolio = st.session_state.portfolio
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Selected", len(portfolio["selected_use_cases"]))
                    with col2:
                        st.metric("Total Effort", portfolio["total_effort"])
                    with col3:
                        st.metric("Budget", portfolio["effort_budget"])
                    
                    st.info(portfolio["selection_rationale"])
                    
                    st.markdown("**Selected Use Cases:**")
                    for uc in portfolio["selected_use_cases"]:
                        st.write(f"✅ {uc.get('title', 'Untitled')} ({uc.get('category', 'N/A')}) - Effort: {uc.get('effort_score_1_to_10', 'N/A')}")
                tab_idx += 1
            
            # Canvas Tab
            if "🗺️ Canvas" in tabs:
                with tab_objects[tab_idx]:
                    st.subheader("AI ROI & Roadmap Canvas")
                    
                    canvas = st.session_state.canvas
                    
                    # View options
                    view_mode = st.radio(
                        "View Mode",
                        ["📊 Visual Canvas", "📋 Summary", "📄 JSON", "📝 Markdown"],
                        horizontal=True
                    )
                    
                    st.markdown("---")
                    
                    if view_mode == "📊 Visual Canvas":
                        # Generate and display visual HTML canvas
                        st.markdown("### Professional Canvas Layout")
                        st.caption("This matches the format from your reference image")
                        
                        visual_html = generate_visual_canvas_html(canvas)
                        
                        # Display in iframe
                        st.components.v1.html(visual_html, height=1200, scrolling=True)
                        
                        # Export options
                        st.markdown("---")
                        st.markdown("### Export Formats")
                        st.info("💡 Download your canvas in multiple formats")
                        
                        # Row 1: HTML, JSON, Markdown, PNG
                        col1, col2, col3, col4 = st.columns(4)
                        with col1:
                            st.download_button(
                                "📄 Download as HTML",
                                data=visual_html,
                                file_name=f"ai_canvas_visual_{datetime.now().strftime('%Y%m%d')}.html",
                                mime="text/html",
                                use_container_width=True
                            )
                        with col2:
                            json_str = json.dumps(canvas, indent=2)
                            st.download_button(
                                "📊 Download as JSON",
                                data=json_str,
                                file_name=f"ai_canvas_{datetime.now().strftime('%Y%m%d')}.json",
                                mime="application/json",
                                use_container_width=True
                            )
                        with col3:
                            markdown_content = canvas_to_markdown(canvas)
                            st.download_button(
                                "📝 Download as Markdown",
                                data=markdown_content,
                                file_name=f"ai_canvas_{datetime.now().strftime('%Y%m%d')}.md",
                                mime="text/markdown",
                                use_container_width=True
                            )
                        with col4:
                            if st.button("📸 Generate PNG", use_container_width=True, key="png_gen"):
                                with st.spinner("Converting canvas to PNG..."):
                                    png_bytes = get_png_bytes(visual_html)
                                    if png_bytes:
                                        st.download_button(
                                            "📸 Download as PNG",
                                            data=png_bytes,
                                            file_name=f"ai_canvas_{datetime.now().strftime('%Y%m%d')}.png",
                                            mime="image/png",
                                            use_container_width=True,
                                            key="png_download"
                                        )
                                        st.success("✅ PNG ready!")
                                    else:
                                        st.error("❌ PNG not available. Use HTML instead.")


                    
                    elif view_mode == "📋 Summary":
                        # Summary view
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("Near-Term ROI", canvas['PortfolioROI']['NearTermROIPercent'])
                            st.write(f"**Costs:** {canvas['Costs']['NearTerm']}")
                        with col2:
                            st.metric("Long-Term ROI", canvas['PortfolioROI']['LongTermROIPercent'])
                            st.write(f"**Benefits:** {canvas['Benefits']['NearTerm']}")
                        
                        # Timeline
                        st.markdown("### Timeline")
                        timeline_data = []
                        for item in canvas['Timeline']:
                            item_copy = item.copy()
                            # Convert phases list to string representation
                            if 'Phases' in item_copy and isinstance(item_copy['Phases'], list):
                                phases_str = ', '.join([p.get('name', 'Unknown') for p in item_copy['Phases']])
                                item_copy['Phases'] = phases_str
                            timeline_data.append(item_copy)
                        timeline_df = pd.DataFrame(timeline_data)
                        st.dataframe(timeline_df, use_container_width=True, hide_index=True)
                    
                    elif view_mode == "📄 JSON":
                        # JSON view
                        st.json(canvas)
                    
                    elif view_mode == "📝 Markdown":
                        # Markdown view
                        md_str = canvas_to_markdown(canvas)
                        st.markdown(md_str)


def main():
    """Main application entry point."""
    initialize_session_state()
    
    # Render sidebar
    render_sidebar()
    
    # Render main chat interface
    render_chat_interface()
    
    # Render results tabs
    render_results_tabs()


if __name__ == "__main__":
    main()
                        
