.PHONY: run install clean

# Default target
run:
ifdef INPUT
	poetry run python -m src.main $(INPUT)
else
	@echo "Usage: make run INPUT=<input_filename>"
endif

# Install dependencies
install:
	poetry install

# Clean up
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

