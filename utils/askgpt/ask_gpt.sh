# ask_gpt.sh
#!/bin/bash

# Configuration
CONDA_ENV_NAME="zipbio11_AI"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PYTHON_SCRIPT="$SCRIPT_DIR/ask_gpt.py"

# Function to check if conda environment exists
check_env() {
    conda env list | grep -q "^$CONDA_ENV_NAME "
    return $?
}

# Activate conda environment and run script
if ! check_env; then
    echo "Error: Conda environment '$CONDA_ENV_NAME' not found"
    exit 1
fi

# Activate environment and run python script
eval "$(conda shell.bash hook)"
conda activate $CONDA_ENV_NAME
python "$PYTHON_SCRIPT" "$@"