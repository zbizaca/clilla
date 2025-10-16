# clilla

`Warning: the name of this project should not b pronounced under any circumstances.`

Purpose of this application is to use locally installed Ollama tool tol list and execute prompts on local foundation models.

## Prerequisites

1. [Python](https://docs.python.org/3/) 3.9 or higher.
2. [Ollama](https://docs.ollama.com/quickstart) installed on your machine/container.

## Installation
 
 Copy the file [`ollama_cli.py`](ollama_cli.py) somewhere in your Python path.
 
 ## Running
 
 Run from Python:
 ```bash
 python ollama_cli.py run llama2 "Tell me a story about a dragon."
 ```
or
```bash
python ollama_cli.py list
```

