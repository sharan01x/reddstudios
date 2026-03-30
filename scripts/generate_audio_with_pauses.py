#!/usr/bin/env python3
"""
Generate audio from markdown article using Kokoro TTS with proper pauses between segments.
Each paragraph/heading is generated separately and concatenated with silence gaps.
"""
import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

FISH_TTS_DIR = Path("~/Documents/Code/fish-tts").expanduser()
OUTPUT_DIR = Path(tempfile.mkdtemp(prefix="audio_segments_"))

def generate_segment(text: str, voice: str, output_path: Path) -> Path:
    """Generate a single segment using Kokoro."""
    cmd = [
        str(FISH_TTS_DIR / ".venv" / "bin" / "python"),
        str(FISH_TTS_DIR / "generate.py"),
        text,
        "--voice", voice,
        "--format", "wav",
        "--output", str(output_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error generating segment: {result.stderr}", file=sys.stderr)
        return None
    return output_path

def create_silence(duration: float, output_path: Path) -> Path:
    """Create a silence WAV file using ffmpeg."""
    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi",
        "-i", f"anullsrc=r=24000:cl=mono",
        "-t", str(duration),
        str(output_path),
    ]
    subprocess.run(cmd, capture_output=True)
    return output_path

def concatenate_audio(files: list[Path], output_path: Path):
    """Concatenate audio files with ffmpeg."""
    # Create concat file
    concat_file = OUTPUT_DIR / "concat.txt"
    with open(concat_file, "w") as f:
        for file in files:
            f.write(f"file '{file}'\n")
    
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_file),
        "-c", "copy",
        str(output_path),
    ]
    subprocess.run(cmd, capture_output=True)

def transform_markdown_to_segments(md_content: str) -> list[str]:
    """Split markdown into speech segments."""
    import re
    
    # Remove frontmatter
    content = re.sub(r'^---\n.*?\n---\n', '', md_content, flags=re.DOTALL)
    # Remove images
    content = re.sub(r'!\[.*?\]\(.*?\)', '', content)
    # Keep link text, remove URL
    content = re.sub(r'\[(.+?)\]\(.*?\)', r'\1', content)
    
    # Split by paragraphs
    paragraphs = re.split(r'\n\n+', content.strip())
    
    segments = []
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        
        # Handle headings
        heading_match = re.match(r'^#+ (.+)$', para, re.MULTILINE)
        if heading_match:
            segments.append(heading_match.group(1).strip())
            continue
        
        # Handle numbered lists
        if re.match(r'^\d+\.', para):
            para = re.sub(r'^\d+\.\s*', '', para, flags=re.MULTILINE)
        
        # Handle bullet points
        if re.match(r'^[-*]', para):
            para = re.sub(r'^[-*]\s*', '', para, flags=re.MULTILINE)
        
        # Remove markdown emphasis (keep text)
        para = re.sub(r'\*\*(.+?)\*\*', r'\1', para)
        para = re.sub(r'(?<!\w)\*(.+?)\*(?!\w)', r'\1', para)
        
        if para.strip():
            segments.append(para.strip())
    
    return segments

def main():
    parser = argparse.ArgumentParser(description="Generate audio from markdown with pauses")
    parser.add_argument("input", type=Path, help="Input markdown file")
    parser.add_argument("--voice", default="bm_fable", help="Kokoro voice name")
    parser.add_argument("--output", type=Path, help="Output audio file")
    parser.add_argument("--pause-duration", type=float, default=0.8, help="Pause duration in seconds")
    parser.add_argument("--heading-pause", type=float, default=1.2, help="Pause after headings in seconds")
    args = parser.parse_args()
    
    md_content = args.input.read_text()
    segments = transform_markdown_to_segments(md_content)
    
    print(f"Generating {len(segments)} segments with voice '{args.voice}'...")
    
    audio_files = []
    for i, segment in enumerate(segments):
        print(f"  [{i+1}/{len(segments)}] {segment[:50]}...")
        
        # Generate segment audio
        seg_output = OUTPUT_DIR / f"seg_{i:03d}.wav"
        audio_path = generate_segment(segment, args.voice, seg_output)
        if not audio_path:
            continue
        audio_files.append(audio_path)
        
        # Add pause after segment (longer after headings)
        is_heading = segment.endswith(':') or len(segment) < 50
        pause_duration = args.heading_pause if is_heading else args.pause_duration
        
        if i < len(segments) - 1:  # No pause after last segment
            pause_file = OUTPUT_DIR / f"pause_{i:03d}.wav"
            create_silence(pause_duration, pause_file)
            audio_files.append(pause_file)
    
    # Concatenate all segments
    if args.output:
        final_output = args.output
    else:
        final_output = args.input.with_suffix(".mp3")
    
    print(f"Concatenating {len(audio_files)} files...")
    
    # First convert to MP3-compatible format
    temp_final = OUTPUT_DIR / "final.wav"
    concatenate_audio(audio_files, temp_final)
    
    # Convert to MP3
    cmd = [
        "ffmpeg", "-y",
        "-i", str(temp_final),
        "-c:a", "libmp3lame",
        "-b:a", "128k",
        str(final_output),
    ]
    subprocess.run(cmd, capture_output=True)
    
    print(f"Done! Output: {final_output}")
    return final_output

if __name__ == "__main__":
    main()
