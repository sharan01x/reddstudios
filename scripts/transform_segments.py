#!/usr/bin/env python3
"""
Transform markdown article to speech-ready segments with proper pauses.
Splits text at paragraph boundaries for segment-based generation with silence gaps.
"""
import re
import sys
from pathlib import Path

def transform_markdown_to_segments(md_content: str) -> list[str]:
    """
    Convert markdown to speech segments:
    - Remove frontmatter
    - Split at paragraph boundaries
    - Handle headings as separate segments
    - Handle list items as separate segments
    - Convert **bold** and *italic* to spoken emphasis (remove markup, keep text)
    """
    segments = []
    
    # Remove frontmatter (--- ... ---)
    content = re.sub(r'^---\n.*?\n---\n', '', md_content, flags=re.DOTALL)
    
    # Remove images
    content = re.sub(r'!\[.*?\]\(.*?\)', '', content)
    # Keep link text, remove URL
    content = re.sub(r'\[(.+?)\]\(.*?\)', r'\1', content)
    
    # Split by double newlines (paragraphs)
    paragraphs = re.split(r'\n\n+', content.strip())
    
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        
        # Handle headings - strip markdown, keep as segment
        heading_match = re.match(r'^#+ (.+)$', para, re.MULTILINE)
        if heading_match:
            segments.append(heading_match.group(1).strip())
            continue
        
        # Handle numbered lists - strip numbers, keep text
        if re.match(r'^\d+\.', para):
            para = re.sub(r'^\d+\.\s*', '', para, flags=re.MULTILINE)
        
        # Handle bullet points - strip markers
        if re.match(r'^[-*]', para):
            para = re.sub(r'^[-*]\s*', '', para, flags=re.MULTILINE)
        
        # Remove **bold** and *italic* markup (keep the text)
        para = re.sub(r'\*\*(.+?)\*\*', r'\1', para)
        para = re.sub(r'(?<!\w)\*(.+?)\*(?!\w)', r'\1', para)
        
        if para.strip():
            segments.append(para.strip())
    
    return segments

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transform_segments.py <article.md>", file=sys.stderr)
        sys.exit(1)
    
    md_path = Path(sys.argv[1])
    md_content = md_path.read_text()
    segments = transform_markdown_to_segments(md_content)
    
    # Output segments with delimiter for shell processing
    for i, seg in enumerate(segments):
        print(f"###SEGMENT_{i}###")
        print(seg)
