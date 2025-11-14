#!/usr/bin/env python3
import markdown

# Read the markdown file
with open('HAI-Partnership-Agreement.md', 'r') as f:
    content = f.read()

# Convert to HTML
html = markdown.markdown(content)

# Create a complete HTML file
html_page = f'''<!DOCTYPE html>
<html>
<head>
    <title>H+AI Partnership Agreement</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }}
        h1, h2, h3 {{ color: #333; }}
        code {{ background-color: #f4f4f4; padding: 2px 4px; }}
        pre {{ background-color: #f4f4f4; padding: 10px; }}
    </style>
</head>
<body>
    {html}
</body>
</html>'''

with open('HAI-Partnership-Agreement.html', 'w') as f:
    f.write(html_page)

print('✅ Created HAI-Partnership-Agreement.html')
print('You can open this in any web browser!')