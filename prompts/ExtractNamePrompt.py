from langchain_core.prompts import ChatPromptTemplate


EXTRACT_PLACES_PROMPT = ChatPromptTemplate.from_template("""
Extract 3 to 4 well-known and visit-worthy travel destination names (cities, regions, or landmarks) from the following content. Only include places that are commonly recognized as good for tourism or travel.

Content:
---
{content}
---

Format:
["Place 1", "Place 2", ...]
""")

