"""
Simplified AutoGen Demo - Interview Platform Product Planning

This is a lightweight version for quick testing and understanding the workflow.
It demonstrates multi-agent collaboration by having each agent generate responses.
"""

from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from autogen.config import Config, WorkflowConfig
import json

# Import the OpenAI client
from openai import OpenAI

class SimpleInterviewPlatformWorkflow:
    """Simplified workflow for interview platform planning"""

    def __init__(self):
        """Initialize the workflow"""
        if not Config.validate_setup():
            print("ERROR: Configuration validation failed!")
            exit(1)
            
        # Initialize the appropriate client based on configuration
        self.client = OpenAI(
            api_key=Config.API_KEY,
            base_url=Config.API_BASE
        )
        
        if Config.VERBOSE:
            print(f"Using {'Groq' if Config.USE_GROQ else 'OpenAI'} API with model: {Config.DEFAULT_MODEL}")
        self.outputs = {}
        self.model = Config.OPENAI_MODEL

    def run(self):
        """Execute the complete workflow"""
        print("\n" + "="*80)
        print("AUTOGEN INTERVIEW PLATFORM WORKFLOW - SIMPLIFIED DEMO")
        print("="*80)
        print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Model: {self.model}\n")

        # Phase 1: Research
        self.phase_research()

        # Phase 2: Analysis
        self.phase_analysis()

        # Phase 3: Blueprint
        self.phase_blueprint()

        # Phase 4: Go-to-Market Launch Plan
        self.phase_launch()

        # Phase 5: Review
        self.phase_review()

        # Summary
        self.print_summary()

    def phase_research(self):
        """Phase 1: Market Research"""
        print("\n" + "="*80)
        print("PHASE 1: MARKET RESEARCH")
        print("="*80)
        print("[ResearchAgent is analyzing the market...]")

        system_prompt = """You are a market research analyst. Provide a brief analysis of
3 competitors in AI interview platforms (HireVue, Pymetrics, Codility).
List their key features and identify market gaps in 150 words."""

        user_message = "Analyze the current market for AI-powered interview platforms."

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=Config.AGENT_TEMPERATURE,
            max_tokens=Config.AGENT_MAX_TOKENS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        self.outputs["research"] = response.choices[0].message.content
        print("\n[ResearchAgent Output]")
        print(self.outputs["research"])

    def phase_analysis(self):
        """Phase 2: Opportunity Analysis"""
        print("\n" + "="*80)
        print("PHASE 2: OPPORTUNITY ANALYSIS")
        print("="*80)
        print("[AnalysisAgent is identifying opportunities...]")

        system_prompt = """You are a product analyst. Based on the market research provided,
identify 3 key market opportunities or gaps for a new AI interview platform.
Be concise in 150 words."""

        user_message = f"""Market research findings:
{self.outputs['research']}

Now identify market opportunities and gaps."""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=Config.AGENT_TEMPERATURE,
            max_tokens=Config.AGENT_MAX_TOKENS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        self.outputs["analysis"] = response.choices[0].message.content
        print("\n[AnalysisAgent Output]")
        print(self.outputs["analysis"])

    def phase_blueprint(self):
        """Phase 3: Product Blueprint"""
        print("\n" + "="*80)
        print("PHASE 3: PRODUCT BLUEPRINT")
        print("="*80)
        print("[BlueprintAgent is designing the product...]")

        system_prompt = """You are a product designer. Based on the market analysis and opportunities,
create a brief product blueprint including:
- Key features (3-5)
- User journey (2-3 steps)
Keep it concise - 150 words."""

        user_message = f"""Market Analysis:
{self.outputs['analysis']}

Create a product blueprint for our platform."""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=Config.AGENT_TEMPERATURE,
            max_tokens=Config.AGENT_MAX_TOKENS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        self.outputs["blueprint"] = response.choices[0].message.content
        print("\n[BlueprintAgent Output]")
        print(self.outputs["blueprint"])

    def phase_launch(self):
        """Phase 4: Go-to-Market Strategy"""
        print("\n" + "="*80)
        print("PHASE 4: GO-TO-MARKET STRATEGY")
        print("="*80)
        print("[LaunchAgent is planning the go-to-market strategy...]")

        system_prompt = """You are a go-to-market strategist. Using the product blueprint,
outline a concise launch plan including marketing channels, launch milestones,
success metrics, and partnerships in under 180 words."""

        user_message = f"""Product Blueprint:
{self.outputs['blueprint']}

Create a go-to-market plan for launch."""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=Config.AGENT_TEMPERATURE,
            max_tokens=Config.AGENT_MAX_TOKENS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        self.outputs["launch"] = response.choices[0].message.content
        print("\n[LaunchAgent Output]")
        print(self.outputs["launch"])

    def phase_review(self):
        """Phase 5: Strategic Review"""
        print("\n" + "="*80)
        print("PHASE 5: STRATEGIC REVIEW")
        print("="*80)
        print("[ReviewerAgent is providing recommendations...]")

        system_prompt = """You are a product reviewer and strategist. Review the product blueprint
and provide 3 strategic recommendations for success.
Be concise - 150 words."""

        user_message = f"""Product Blueprint:
{self.outputs['blueprint']}

Launch Plan:
{self.outputs['launch']}

Provide strategic review and recommendations."""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=Config.AGENT_TEMPERATURE,
            max_tokens=Config.AGENT_MAX_TOKENS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        self.outputs["review"] = response.choices[0].message.content
        print("\n[ReviewerAgent Output]")
        print(self.outputs["review"])

    def print_summary(self):
        """Print final summary"""
        print("\n" + "="*80)
        print("FINAL SUMMARY")
        print("="*80)

        print("""
This workflow demonstrated a 5-agent collaboration:
1. ResearchAgent - Analyzed the market
2. AnalysisAgent - Identified opportunities
3. BlueprintAgent - Designed the product
4. LaunchAgent - Built the go-to-market strategy
5. ReviewerAgent - Provided strategic recommendations

Each agent received context from the previous agent's output,
demonstrating the sequential workflow pattern of AutoGen.
""")

        # Print full results
        print("\n" + "="*80)
        print("FULL RESULTS - ALL PHASES")
        print("="*80)
        
        print("\n" + "-"*80)
        print("PHASE 1: MARKET RESEARCH (Full Output)")
        print("-"*80)
        print(self.outputs["research"])
        
        print("\n" + "-"*80)
        print("PHASE 2: OPPORTUNITY ANALYSIS (Full Output)")
        print("-"*80)
        print(self.outputs["analysis"])

        print("\n" + "-"*80)
        print("PHASE 3: PRODUCT BLUEPRINT (Full Output)")
        print("-"*80)
        print(self.outputs["blueprint"])

        print("\n" + "-"*80)
        print("PHASE 4: GO-TO-MARKET STRATEGY (Full Output)")
        print("-"*80)
        print(self.outputs["launch"])

        print("\n" + "-"*80)
        print("PHASE 5: STRATEGIC REVIEW (Full Output)")
        print("-"*80)
        print(self.outputs["review"])

        # Save to file
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f"workflow_outputs_{timestamp}.txt"
        with open(output_file, 'w') as f:
            f.write("="*80 + "\n")
            f.write("AUTOGEN INTERVIEW PLATFORM WORKFLOW - FULL RESULTS\n")
            f.write("="*80 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Model: {self.model}\n\n")
            
            f.write("\n" + "-"*80 + "\n")
            f.write("PHASE 1: MARKET RESEARCH\n")
            f.write("-"*80 + "\n")
            f.write(self.outputs["research"] + "\n")
            
            f.write("\n" + "-"*80 + "\n")
            f.write("PHASE 2: OPPORTUNITY ANALYSIS\n")
            f.write("-"*80 + "\n")
            f.write(self.outputs["analysis"] + "\n")
            
            f.write("\n" + "-"*80 + "\n")
            f.write("PHASE 3: PRODUCT BLUEPRINT\n")
            f.write("-"*80 + "\n")
            f.write(self.outputs["blueprint"] + "\n")
            
            f.write("\n" + "-"*80 + "\n")
            f.write("PHASE 4: GO-TO-MARKET STRATEGY\n")
            f.write("-"*80 + "\n")
            f.write(self.outputs["launch"] + "\n")

            f.write("\n" + "-"*80 + "\n")
            f.write("PHASE 5: STRATEGIC REVIEW\n")
            f.write("-"*80 + "\n")
            f.write(self.outputs["review"] + "\n")
        
        print(f"\n💾 Full results saved to: {output_file}")

        print(f"\nEnd Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80)


if __name__ == "__main__":
    try:
        workflow = SimpleInterviewPlatformWorkflow()
        workflow.run()
        print("\n✅ Workflow completed successfully!")
    except Exception as e:
        print(f"\n❌ Error during workflow execution: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Verify OPENAI_API_KEY is set in parent directory .env (../.env)")
        print("2. Check your API key has sufficient credits")
        print("3. Verify internet connection")
        print("4. Ensure config.py can access shared_config from parent directory")
        print("5. Check OpenAI API status at https://status.openai.com")
        import traceback
        traceback.print_exc()
