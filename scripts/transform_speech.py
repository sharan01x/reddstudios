#!/usr/bin/env python3
"""
Transform markdown article to speech-ready script with [pause] and [emphasis] tags.
"""
import re
import sys
from pathlib import Path

def transform_markdown_to_speech(md_content: str) -> str:
    """
    Convert markdown to speech script:
    - Remove frontmatter
    - Add [pause] between paragraphs
    - Add [pause] for list items
    - Add [emphasis] for **bold** and *italic*
    - Handle headings with slight pause
    """
    # Remove frontmatter (--- ... ---)
    content = re.sub(r'^---\n.*?\n---\n', '', md_content, flags=re.DOTALL)
    
    # Process headings - add pause before, keep text
    content = re.sub(r'^# (.+)$', r'[pause]\1', content, flags=re.MULTILINE)
    content = re.sub(r'^## (.+)$', r'[pause]\1', content, flags=re.MULTILINE)
    content = re.sub(r'^### (.+)$', r'[pause]\1', content, flags=re.MULTILINE)
    
    # Convert **bold** and *italic* to [emphasis]...[/emphasis]
    # Handle **bold** first (more specific)
    content = re.sub(r'\*\*(.+?)\*\*', r'[emphasis]\1[/emphasis]', content)
    # Handle *italic* (but not inside words)
    content = re.sub(r'(?<!\w)\*(.+?)\*(?!\w)', r'[emphasis]\1[/emphasis]', content)
    
    # Handle numbered lists - add pause before each item
    content = re.sub(r'^(\d+)\. (.+)$', r'[pause]\2', content, flags=re.MULTILINE)
    
    # Handle bullet points - add pause before each
    content = re.sub(r'^[-*] (.+)$', r'[pause]\1', content, flags=re.MULTILINE)
    
    # Add [pause] between paragraphs (double newlines)
    content = re.sub(r'\n\n+', '\n[pause]\n', content)
    
    # Clean up multiple consecutive pauses
    content = re.sub(r'(\[pause\])\s*(\[pause\])+', r'\1', content)
    
    # Remove any remaining markdown that shouldn't be spoken
    content = re.sub(r'!\[.*?\]\(.*?\)', '', content)  # Remove images
    content = re.sub(r'\[(.+?)\]\(.*?\)', r'\1', content)  # Keep link text, remove URL
    
    # Clean up extra whitespace
    content = re.sub(r'\n\s*\n', '\n', content)
    content = content.strip()
    
    return content

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transform_speech.py <article.md>")
        sys.exit(1)
    
    md_path = Path(sys.argv[1])
    md_content = md_path.read_text()
    speech_script = transform_markdown_to_speech(md_content)
    print(speech_script)
