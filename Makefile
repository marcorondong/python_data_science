# ===== Python Configuration ===== #
PYTHON ?= python3
POST_PROCESS = | cat -e
VENV_DIR ?= .venv
NORMINETTE = $(VENV_DIR)/bin/flake8

# Auto-detect: use venv if available, otherwise fallback to virtualenv
# VENV_CMD := $(shell $(PYTHON) -m venv --help >/dev/null 2>&1 && echo "$(PYTHON) -m venv" || echo "$(PYTHON) -m virtualenv")
# Auto-detect:
# - Prefer venv ONLY if ensurepip is available (otherwise venv creation will fail on Debian/Ubuntu)
# - Else fallback to virtualenv (command or module)
VENV_CMD := $(shell \
	$(PYTHON) -c "import venv, ensurepip" >/dev/null 2>&1 && echo "$(PYTHON) -m venv" || \
	( command -v virtualenv >/dev/null 2>&1 && echo "virtualenv" ) || \
	( $(PYTHON) -c "import virtualenv" >/dev/null 2>&1 && echo "$(PYTHON) -m virtualenv" ) \
)

PIP = $(VENV_DIR)/bin/pip
VENV_PYTHON = $(VENV_DIR)/bin/python
REQUIREMENTS ?= requirements.txt

# ===== Exercises definitions ===== #
EX00 = ex00/Hello.py
EX01 = ex01/format_ft_time.py
EX02A = ex02/tester.py
EX02B = ex02/find_ft_type.py
EX03A = ex03/tester.py
EX03B = ex03/NULL_not_found.py
EX04 = ex04/whatis.py
EX05 = ex05/building.py
EX06 = ex06/filterstring.py
EX07 = ex07/sos.py
EX08 = ex08/tester.py
EX09 = ex09/tester.py

EXERCISES = ex00 ex01 ex02 ex03 ex04 ex05 ex06 ex07 ex08 ex09
LINT_DIRS ?= ex05 ex06 ex07 ex08 ex09
SEPARATOR = \n========== $@ ==========\n

#------------------------------------ CODE ------------------------------------#
.PHONY: all $(EXERCISES) clean venv install norminette clean fclean check-doc

all: $(EXERCISES)

ex00:
	@printf "$(SEPARATOR)"
	$(PYTHON) $(EX00) $(POST_PROCESS)

ex01:
	@printf "$(SEPARATOR)"
	$(PYTHON) $(EX01) $(POST_PROCESS)

ex02:
	@printf "$(SEPARATOR)"
	$(PYTHON) $(EX02A) $(POST_PROCESS)
	@printf "$(SEPARATOR)"
	$(PYTHON) $(EX02B) $(POST_PROCESS)

ex03:
	@printf "$(SEPARATOR)"
	$(PYTHON) $(EX03A) $(POST_PROCESS)
	@printf "$(SEPARATOR)"
	$(PYTHON) $(EX03B) $(POST_PROCESS)

ex04:
	@printf "$(SEPARATOR)"
	$(PYTHON) $(EX04) 14
	$(PYTHON) $(EX04) -5
	$(PYTHON) $(EX04)
	$(PYTHON) $(EX04) 0
	$(PYTHON) $(EX04) Hi!
	$(PYTHON) $(EX04) 13 5

ex05:
	@printf "$(SEPARATOR)"
	$(PYTHON) $(EX05) "Python 3.0, released in 2008, was a major revision that is not completely backward compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
	$(PYTHON) $(EX05) wrong input

ex06:
	@printf "$(SEPARATOR)"
	$(PYTHON) $(EX06) 'Hello the World' 4
	$(PYTHON) $(EX06) 'Hello the World' 99
	$(PYTHON) $(EX06) 3 'Hello the World'
	$(PYTHON) $(EX06)

ex07:
	@printf "$(SEPARATOR)"
	$(PYTHON) $(EX07) "sos" $(POST_PROCESS)
	$(PYTHON) $(EX07) 'h$$llo' $(POST_PROCESS)

ex08:
	@printf "$(SEPARATOR)"
	$(PYTHON) $(EX08)

ex09: venv
	@printf "$(SEPARATOR)"
	rm -rf ex09/build ex09/dist ex09/*.egg-info
	$(PIP) install --upgrade build
	cd ex09 && ../$(VENV_PYTHON) -m build
	$(PIP) install --force-reinstall ex09/dist/*.whl
	$(PIP) show -v ft_package
	@printf "$(SEPARATOR)"
	$(VENV_PYTHON) $(EX09)

# venv:
# 	@if [ ! -d "$(VENV_DIR)" ]; then \
# 		echo "Creating virtual environment in $(VENV_DIR)"; \
# 		$(VENV_CMD) $(VENV_DIR); \
# 	else \
# 		echo "Virtual environment already exists"; \
# 	fi
venv:
	@if [ ! -x "$(PIP)" ]; then \
		echo "Creating virtual environment in $(VENV_DIR)"; \
		rm -rf "$(VENV_DIR)"; \
		if [ -z "$(VENV_CMD)" ]; then \
			echo "Error: cannot create venv. Need either:"; \
			echo "  - python venv with ensurepip (Debian/Ubuntu: install python3-venv)"; \
			echo "  - or virtualenv installed"; \
			exit 1; \
		fi; \
		$(VENV_CMD) "$(VENV_DIR)"; \
	else \
		echo "Virtual environment already exists"; \
	fi

install: venv
	$(PIP) install -r $(REQUIREMENTS)

norminette: venv
	$(NORMINETTE) $(LINT_DIRS)

clean:
	@echo "Cleaning Python cache files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@echo "Cleaning build artifacts..."
	@find . -path "./$(VENV_DIR)" -prune -o -type d -name "build" -exec rm -rf {} +
	@find . -path "./$(VENV_DIR)" -prune -o -type d -name "dist" -exec rm -rf {} +
	@find . -path "./$(VENV_DIR)" -prune -o -type d -name "*.egg-info" -exec rm -rf {} +
	@echo "Done."

fclean: clean
	@if [ -d "$(VENV_DIR)" ]; then \
		echo "Removing virtual environment"; \
		rm -rf $(VENV_DIR); \
	else \
		echo "No virtual environment to remove"; \
	fi

check-doc:
	$(PYTHON) tools/check_docstrings.py .