INSIGHT_PROMPT = """
You are a senior market intelligence analyst.

Using the following web-sourced content related to **"{query}"**, extract exactly **3 key market insights**. Your analysis should reflect expert-level understanding, avoiding surface-level commentary.

Focus on:
- Emerging market trends or disruptions
- Strategic initiatives or pivots by the company or competitors
- Competitive positioning, product differentiation, or ecosystem changes
- Notable shifts in consumer behavior or regulatory landscape

**Instructions:**
- Present insights as **numbered bullet points**
- Each insight should be **concise, analytical, and action-oriented**
- Do not repeat content from the input verbatim — synthesize and interpret

**Web Content:**
{content}
"""

CONTENT_IDEAS_PROMPT = """
Based on the insights above, generate **three distinct content ideas**, each tailored to a different format and marketing objective.

**Output Format:**
1. 📰 **Blog Post**  
   - **Title**: (Engaging, SEO-optimized, 8–12 words)  
   - **Summary**: One-sentence overview that teases value and insight  

2. 📱 **Social Media Post**  
   - **Text**: Sharp, attention-grabbing (max 280 characters)  
   - Use tone: authoritative + engaging  
   - Include 1 relevant hashtag  

3. 📘 **Whitepaper/Report**  
   - **Title**: Strategic and research-oriented  
   - **Target Audience**: (e.g., CMOs, investors, product leads)  
   - **Objective**: Clarify the goal or value of the whitepaper

**Instructions:**
- Ensure each idea reflects at least one core market insight
- Use professional language appropriate for B2B content marketing
- Avoid generic phrasing — make ideas feel fresh and relevant
"""
