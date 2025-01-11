from markitdown import MarkItDown
import os

md = MarkItDown()
result = md.convert("/Users/tan/Documents/Documentation-in-Markdown/Checkpointing.pdf")

# Get current working directory and create output path
output_path = os.path.join(os.getcwd(), "output.md")

# Write markdown content to output.md
with open(output_path, "w", encoding="utf-8") as f:
    f.write(result.text_content)