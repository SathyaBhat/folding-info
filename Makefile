.PHONY: build
.DEFAULT_GOAL := build

build:
	@pip3 install --target ./package -r requirements.txt
	cd package && zip -r9 ../function.zip .
	@zip -q -g function.zip lambda_function.py folding_stats.py
	aws lambda update-function-code --function-name folding_at_home_stats --zip-file fileb://function.zip