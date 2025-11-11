#!/usr/bin/env python3
"""
Create a less aggressively redacted version for better sarcasm analysis
"""

import pandas as pd
import re

def light_redaction(text):
    """Apply lighter redaction - keep common words, mask only potential personal info"""
    if pd.isna(text):
        return text
    
    # Keep common words but mask potential names/places
    text = re.sub(r'\b[A-Z][a-z]{2,}\b', '[NAME]', text)  # Proper nouns
    text = re.sub(r'\b\d{3,}\b', '[NUMBER]', text)  # Long numbers
    text = re.sub(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', '[EMAIL]', text)  # Emails
    text = re.sub(r'\b\+?1?[\s.-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b', '[PHONE]', text)  # Phone numbers
    
    return text

def main():
    print("🔧 Creating lighter redaction version...")
    
    # Load the existing CSV and convert timestamp column properly
    df = pd.read_csv('pi_sarcasm_hybrid_review.csv')
    df["sent_at_utc"] = pd.to_datetime(df["sent_at_utc"])
    
    # Load original data to get unredacted text
    import json
    with open("Copy of pi-user-history.json", "r") as f:
        data = json.load(f)
    
    messages = pd.DataFrame(data['user_data']['messages'])
    ai_messages = messages[messages["sender"] == "AI"].copy()
    
    # Apply lighter redaction to original text
    ai_messages["text_light_redacted"] = ai_messages["text"].apply(light_redaction)
    
    # Convert timestamps for matching
    ai_messages["sent_at_dt"] = pd.to_datetime(ai_messages["sent_at"], format='mixed')
    
    # Create a mapping from timestamp to lightly redacted text
    timestamp_to_text = dict(zip(ai_messages["sent_at_dt"], ai_messages["text_light_redacted"]))
    
    # Add lighter redaction to our analysis by matching timestamps
    df["text_readable"] = df["sent_at_utc"].apply(lambda x: timestamp_to_text.get(x, ""))
    
    # Reorder columns to put readable text first
    cols = ["text_readable"] + [col for col in df.columns if col != "text_readable"]
    df_readable = df[cols]
    
    # Save the more readable version
    df_readable.to_csv("pi_sarcasm_readable_review.csv", index=False)
    
    print("✅ Created pi_sarcasm_readable_review.csv with lighter redaction")
    print("\nSample of readable text:")
    for i, text in enumerate(df_readable['text_readable'].head(3)):
        if text:
            print(f"{i+1}. {text[:150]}...")
        else:
            print(f"{i+1}. (No matching text found)")

if __name__ == "__main__":
    main()