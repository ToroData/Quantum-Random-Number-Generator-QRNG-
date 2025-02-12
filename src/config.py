"""
This module provides functions to load text and question data from JSON files.

Author: Ricard Santiago Raigada García
Date: 02-12-2025
"""
import json

def load_texts() -> dict:
    with open("src/markdown/texts.json", "r", encoding="utf-8") as file:
        return json.load(file)

def load_questions() -> dict:
    with open("src/markdown/qa.json", "r", encoding="utf-8") as file:
        return json.load(file)
