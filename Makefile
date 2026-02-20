# UltraBoost Dashboard Makefile
# Powered by BoostNova
ENV_NAME = ultraboost-dashboard
STREAMLIT_APP = main.py
.PHONY: install run clean uninstall
install:
	conda env create -f environment_conda.yml
run:
	streamlit run $(STREAMLIT_APP) --server.headless true
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
uninstall:
	conda env remove -n $(ENV_NAME) -y
update:
	conda env update -f environment_conda.yml --prune
docker-build:
	docker build -t ultraboost/dashboard:latest .
docker-run:
	docker-compose up -d
docker-stop:
	docker-compose down