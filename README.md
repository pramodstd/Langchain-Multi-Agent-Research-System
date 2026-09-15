# LangChain Multi-Agent Research System

An agentic research assistant that searches the web, reads the most relevant source, writes a structured report, and critiques the result. The project includes both a command-line workflow and a Streamlit interface.

## Features

- Search the web for recent information with Tavily.
- Select and scrape a relevant source for deeper context.
- Generate a structured report with findings, conclusions, and sources.
- Review the generated report with a separate critic chain.
- Run the workflow from Python or through a Streamlit web app.

## Architecture

The research workflow is implemented in `src/pipelines/pipeline.py`:

```text
User topic
	|
	v
Search agent  -- Tavily web search --> search results
	|
	v
Reader agent  -- URL scraping ------> detailed source content
	|
	v
Writer chain  -- LLM ----------------> structured research report
	|
	v
Critic chain  -- LLM ----------------> score, strengths, improvements
```

- `src/tools/tools.py` contains the Tavily search tool and multi-strategy web scraper.
- `src/agents/agents.py` creates the search and reader agents and defines the writer and critic chains.
- `src/pipelines/pipeline.py` coordinates the four-step workflow and returns the collected state.
- `app.py` provides the Streamlit user interface.
- `main.py` runs a sample topic from the command line.

## Technologies

- **Python 3.11+**
- **LangChain** for agents, prompts, tools, and output parsing
- **Groq** through `langchain-groq` for the default chat model
- **Tavily** for web search
- **Requests**, **Trafilatura**, **Readability**, **Beautiful Soup**, and **lxml** for web-page extraction
- **Streamlit** for the interactive web application
- **python-dotenv** for local environment configuration
- **Rich** for terminal output

## Requirements

- Python 3.11 or newer
- A Tavily API key
- A Groq API key

## Installation

### Using Conda

```bash
conda create -n langagent python=3.11 -y
conda activate langagent
pip install -r requirements.txt
```

### Using a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```env
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
```

The application loads these values with `python-dotenv`. Keep `.env` private and do not commit API keys to source control.

## Usage

### Streamlit app

Start the web interface with:

```bash
streamlit run app.py
```

### Command line

Run the sample workflow with:

```bash
python main.py
```

To research a different topic from Python:

```python
from src.pipelines.pipeline import run_research_pipeline

result = run_research_pipeline("The impact of AI on the job market in 2026")
print(result["report"])
print(result["feedback"])
```

The default model and its settings are configured in `src/agents/agents.py`.

## Project Structure

```text
.
├── app.py                  # Streamlit interface
├── main.py                 # CLI example
├── requirements.txt        # Python dependencies
└── src/
	├── agents/             # Search, reader, writer, and critic components
	├── pipelines/          # End-to-end research orchestration
	└── tools/              # Search and web-scraping tools
```

## Notes

- Search and scraping depend on external services and websites, so results can vary.
- The scraper limits extracted page content to keep prompts manageable.
- Always verify generated reports and sources before using them for high-stakes decisions.

## License

This project is licensed under the terms in [LICENSE](LICENSE).