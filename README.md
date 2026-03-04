# Semantic Scholar Crew – Project Overview                                      
                                                          
  Semantic Scholar Crew is a research‑driven, collaborative project that uses   
  the Semantic Scholar API to gather and analyse scientific literature.         
  The codebase is written in Python 3.12 (with optional pipenv/poetry) and is
  structured to be modular, testable, and easy to extend.                       
                  
  ⚠️  Note
  The repository contains a virtual‑environment folder (.venv/) and third‑party
  packages that are not part of the source code you should commit.
  Only the files in src/, tests/ and related configuration are meant to be
  version‑controlled.

  ---
  📁 Project Layout

  semantic_scholar_crew/
  ├── .venv/                     # Virtual environment (do NOT commit)
  ├── src/
  │   ├── __init__.py
  │   ├── config.py              # Environment / API‑key handling
  │   ├── api/
  │   │   └── semantic_scholar.py  # Wrapper around Semantic Scholar API
  │   ├── data/
  │   │   └── paper_fetcher.py     # Pulls papers based on query
  │   ├── analysis/
  │   │   └── citation_graph.py    # Builds citation network
  │   ├── utils/
  │   │   └── helpers.py           # Common utilities
  │   └── main.py                  # CLI entry‑point (argparse)
  ├── tests/
  │   ├── __init__.py
  │   └── test_api.py               # Unit tests for API wrapper
  ├── requirements.txt             # Pin dependencies (pip‑freeze)
  ├── README.md                    # This file
  └── .gitignore                   # Excludes .venv/ and other temp files

  Key Components

  ┌──────────────┬───────────────────────────────────────────────────────────┐
  │  Directory   │                          Purpose                          │
  ├──────────────┼───────────────────────────────────────────────────────────┤
  │ src/api      │ Handles HTTP requests to Semantic Scholar, pagination,    │
  │              │ rate‑limit handling.                                      │
  ├──────────────┼───────────────────────────────────────────────────────────┤
  │ src/data     │ Orchestrates data collection: query construction, file    │
  │              │ persistence (JSON/CSV).                                   │
  ├──────────────┼───────────────────────────────────────────────────────────┤
  │ src/analysis │ Builds graphs, calculates metrics (h‑index, citation      │
  │              │ counts), and visualises results.                          │
  ├──────────────┼───────────────────────────────────────────────────────────┤
  │ src/utils    │ Small helper functions (e.g., logging, retry decorators). │
  ├──────────────┼───────────────────────────────────────────────────────────┤
  │ src/main.py  │ CLI that accepts arguments such as --query, --limit,      │
  │              │ --output.                                                 │
  └──────────────┴───────────────────────────────────────────────────────────┘

  ---
  🚀 Getting Started

  Prerequisites

  - Python 3.12+ (tested on 3.12.0)
  - pip or a virtual‑environment manager (venv, poetry, etc.)

  Installation

  # Clone the repo
  git clone https://github.com/your‑org/semantic_scholar_crew.git
  cd semantic_scholar_crew

  # Create a virtual environment and activate it
  python3 -m venv .venv
  source .venv/bin/activate   # On Windows: .\.venv\Scripts\activate

  # Install dependencies
  pip install -r requirements.txt

  Tip: If you use poetry, run poetry install instead.

  Configuration

  The project expects an environment variable for the Semantic Scholar API key:

  export SEMANTIC_SCHOLAR_API_KEY="your_api_key_here"

  Alternatively, create a .env file in the project root:

  SEMANTIC_SCHOLAR_API_KEY=your_api_key_here

  The src/config.py module automatically loads the key from either source.

  Running the CLI

  python src/main.py --query "deep learning" --limit 50 --output results.json

  Options

  ┌──────────┬──────────────────────────────────────────┐
  │   Flag   │               Description                │
  ├──────────┼──────────────────────────────────────────┤
  │ --query  │ Search query (required).                 │
  ├──────────┼──────────────────────────────────────────┤
  │ --limit  │ Number of papers to fetch (default: 20). │
  ├──────────┼──────────────────────────────────────────┤
  │ --output │ Output file path (JSON by default).      │
  └──────────┴──────────────────────────────────────────┘

  Running Tests

  pytest tests/

  All unit tests are located in the tests/ directory and use unittest.mock to
  stub external calls.

  ---
  📚 Usage Example

  # Fetch 30 papers about "graph neural networks"
  python src/main.py --query "graph neural network" --limit 30 --output
  gnn_papers.json

  The script will:

  1. Query the Semantic Scholar API.
  2. Respect rate limits (max 10 req/s).
  3. Store the paper metadata in gnn_papers.json.
  4. Print a quick summary: total papers fetched, first paper title.

  You can then feed the JSON to src/analysis/citation_graph.py to build a
  citation network.

  ---
  🛠️  Extending the Project

  - New API endpoints – add a method to src/api/semantic_scholar.py and expose
  it via the CLI.
  - Different output formats – modify src/main.py to support CSV or TSV.
  - Custom analysis – create a new module under src/analysis/ and import it in
  main.py.

  All modules follow a simple dependency injection pattern: the API wrapper is
  passed to data and analysis layers, keeping code loosely coupled.

  ---
  📄 License

  This project is licensed under the MIT License – see the ./LICENSE file for
  details.

  ---
  🤝 Contributing

  1. Fork the repository.
  2. Create a feature branch (git checkout -b feat/new-feature).
  3. Write tests for your changes.
  4. Run pytest to ensure all tests pass.
  5. Submit a pull request.

  Please follow the existing coding style (PEP‑8) and include docstrings for new
   functions.

  ---
  📞 Support & Questions

  - Issues – File a GitHub issue for bugs or feature requests.
  - Discussion – Join the project discussion board on GitHub.
  - Email – Contact the maintainer at maintainer@example.com.

  Happy coding!