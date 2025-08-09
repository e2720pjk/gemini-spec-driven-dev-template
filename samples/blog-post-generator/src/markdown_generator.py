import datetime

def generate_markdown_header(title, author, date):
    return f"""
---
title: {title}
author: {author}
date: {date.strftime('%Y-%m-%d')}
---

"""

def generate_markdown_content(title, author, date, content):
    header = generate_markdown_header(title, author, date)
    return f"{header}{content}"
