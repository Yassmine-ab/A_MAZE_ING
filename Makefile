# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ LAYOUT ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DEFAULT			= \033[0m
GREEN			= \033[1;32m
CYAN			= \033[1;36m

define ANIMATION
				@for frame in ⠋ ⠙ ⠹ ⠸ ⠼ ⠴ ⠦ ⠧ ⠇ ⠏; do \
				printf "$$frame $(1)...\r"; \
				sleep 0.02; \
				done; \
				printf "\n"
endef


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ RULES ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

install:
				$(call ANIMATION,Installing activity dependencies)
 				@python3 -m pip install .
# 				&& python3 -m pip install build && python3 -m build

run:
				@python3 a_maze_ing.py config.txt

debug:
				@python3 -m pdb a_maze_ing.py config.txt

clean:
				$(call ANIMATION,Removing compiled files and caches)
				@rm -rf __pycache__ .mypy_cache *.pyc
				@printf "$(GREEN)✓$(DEFAULT) Cleaned\n"

lint:
				@flake8 . && mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
				@flake8 . && mypy . --strict

test:
				$(call ANIMATION,Running tests)
				@pytest tests

venv:
				@python3 -m venv venv && source venv/bin/activate

help:
				@printf "Usage: make [target]\n"
				@printf "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
				@printf "$(CYAN)install$(DEFAULT)		- Install project dependencies\n"
				@printf "$(CYAN)run$(DEFAULT)		- Run the main script with a config file argument\n"
				@printf "$(CYAN)debug$(DEFAULT)		- Run the main script in debug mode\n"
				@printf "$(CYAN)clean$(DEFAULT)		- Remove compiled Python files and caches\n"
				@printf "$(CYAN)lint$(DEFAULT)		- Run linter and type checker to ensure code quality\n"
				@printf "$(CYAN)lint-strict$(DEFAULT)		- Run linter and type checker with strict settings\n"
				@printf "$(CYAN)test$(DEFAULT)		- Run tests using pytest\n"
				@printf "$(CYAN)venv$(DEFAULT)		- Set up a virtual environment for dependency isolation\n"
				@printf "$(CYAN)help$(DEFAULT)		- Show this help message\n"

.PHONY:			install run debug clean lint lint-strict test venv help
