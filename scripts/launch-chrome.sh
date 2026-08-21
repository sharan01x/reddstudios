#!/bin/bash
# Launch Chrome with the Redd XF profile for browser automation
# Usage: ./launch-chrome.sh
# Then connect browser_exec to http://127.0.0.1:9224

echo "Launching Chrome for Redd XF (port 9224)..."

"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --user-data-dir="/Users/sharan/Library/Application Support/Google/Chrome-reddxf" \
  --remote-debugging-port=9224 \
  --no-first-run \
  --no-default-browser-check \
  --remote-allow-origins="*" &

echo "Chrome launched with Redd XF profile."
echo "Connect browser_exec to: http://127.0.0.1:9224"
echo ""
echo "Accounts available:"
echo "  - LinkedIn (Redd XF company page, ID: 13380986)"
echo "  - Firefly (Twitter/X scheduling for @reddexperience)"
echo "  - Medium (@reddxf)"
echo "  - Substack (reddxf.substack.com)"
echo "  - YouTube (youtube.com/@reddxf)"