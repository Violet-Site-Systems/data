#!/usr/bin/env python3
"""
Show a few sample messages with minimal redaction for sarcasm analysis
"""

import pandas as pd
import json
import re

def minimal_redaction(text):
    """Very light redaction - just mask obvious personal info"""
    if pd.isna(text):
        return text
    
    # Only mask emails and phone numbers, keep everything else
    text = re.sub(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', '[EMAIL]', text)
    text = re.sub(r'\b\+?1?[\s.-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b', '[PHONE]', text)
    
    return text

def main():
    print("📋 Showing sample Pi.ai messages with minimal redaction...")
    print("(For sarcasm analysis - personal info like emails/phones removed)\n")
    
    # Load original data
    with open("Copy of pi-user-history.json", "r") as f:
        data = json.load(f)
    
    messages = pd.DataFrame(data['user_data']['messages'])
    ai_messages = messages[messages["sender"] == "AI"].copy()
    
    # Apply minimal redaction
    ai_messages["text_clean"] = ai_messages["text"].apply(minimal_redaction)
    
    # Filter to messages with emojis (our sarcasm candidates)
    import emoji
    ai_messages["has_emoji"] = ai_messages["text"].apply(
        lambda x: any(e in emoji.EMOJI_DATA for e in x) if pd.notna(x) else False
    )
    
    emoji_messages = ai_messages[ai_messages["has_emoji"]].copy()
    
    print(f"Found {len(emoji_messages)} Pi.ai messages with emojis\n")
    print("Sample messages (looking for potential sarcasm patterns):\n")
    
    # Show first 10 emoji messages
    for i, (_, row) in enumerate(emoji_messages.head(10).iterrows()):
        print(f"{i+1}. [{row['sent_at']}]")
        print(f"   {row['text_clean']}")
        print()
    
    # Save a readable version
    emoji_messages[['text_clean', 'sent_at']].to_csv('pi_emoji_messages_readable.csv', index=False)
    print(f"✅ Saved {len(emoji_messages)} emoji messages to 'pi_emoji_messages_readable.csv'")
    print("\nThis version has minimal redaction so you can analyze sarcasm patterns!")

if __name__ == "__main__":
    main()