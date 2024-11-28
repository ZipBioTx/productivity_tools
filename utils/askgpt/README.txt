## Ask_gpt provides a simple interface to OpenAI's GPT-4o API directly from the terminal cmd.

## Installation
1. create a conda environment using the provided zipbio11_AI.yml file:
  >  conda env create -f zipbio11_AI.yml
  if you choose to use any other environemt, make sure to install the openai package and than update the CONDA_ENV_NAME variable in Ask_gpt.py and Ask_gpt.sh files.
  
2. Add an alias to the Ask_gpt.sh file in your .bashrc or .bash_profile file:
  >  alias askgpt='bash /path/to/Ask_gpt.sh'
  e.g. from the current project directory: 
  >echo "alias askgpt='$(pwd)/ask_gpt.sh'" >> ~/.bashrc 
  >  source ~/.bashrc

# usage examples:
  > askgpt What is the capital of France?

