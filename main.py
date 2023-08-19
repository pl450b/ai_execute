# this is a test
from config import API_KEY
import os
import openai

openai.organization = "org-LdSlWbJ9mw5Y4EqwxL2bRZaj"
openai.api_key = API_KEY
print(openai.Model.list())