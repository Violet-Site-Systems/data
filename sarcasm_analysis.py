#!/usr/bin/env python3
"""
Pi.ai Sarcasm Detection Analysis
Following Aethel's dual-layer methodology for detecting sarcastic communication patterns
"""

import pandas as pd
import emoji
import re
import numpy as np
import json
from collections import Counter

def extract_emojis(text):
    """Extract emoji characters from text"""
    if pd.isna(text):
        return []
    return [char for char in text if char in emoji.EMOJI_DATA]

def detect_tone_contradiction(text):
    """Detect neutral/dismissive words paired with sarcastic emojis"""
    if pd.isna(text):
        return False
    
    neutral_words = r"\b(?:sure|whatever|fine|okay|alright|right|yeah|mhmm|uh|huh)\b"
    sarcastic_emojis = r"[\U0001F612\U0001F614\U0001F635\U0001F92C\U0001F921\U0001F480]"  # 😒 🙄 😵 🥴 🤡 💀
    
    return bool(re.search(f"{neutral_words}.*{sarcastic_emojis}", text, re.IGNORECASE))

def main():
    print("🔍 Starting Pi.ai Sarcasm Detection Analysis...")
    
    # Step 1: Load and preprocess data
    print("📂 Loading conversation data...")
    try:
        # Load the JSON file
        import json
        with open("Copy of pi-user-history.json", "r") as f:
            data = json.load(f)
        
        # Extract messages from the nested structure
        messages = pd.DataFrame(data['user_data']['messages'])
        print(f"✅ Loaded {len(messages)} messages")
        
        # Normalize timestamps
        messages["sent_at_utc"] = pd.to_datetime(messages["sent_at"], format='mixed').dt.tz_localize("UTC")
        
        # Filter to AI messages only (where sarcasm detection is relevant)
        ai_messages = messages[messages["sender"] == "AI"].copy()
        print(f"🤖 Filtered to {len(ai_messages)} AI messages")
        
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return
    
    # Step 2: Basic emoji detection
    print("😊 Detecting emoji presence...")
    ai_messages["sarcastic_emoji"] = ai_messages["text"].apply(
        lambda x: any(e in emoji.EMOJI_DATA for e in x) if pd.notna(x) else False
    )
    emoji_count = ai_messages["sarcastic_emoji"].sum()
    print(f"✅ Found {emoji_count} messages with emojis")
    
    # Step 3: Emoji frequency analysis
    print("📊 Analyzing emoji frequency patterns...")
    emoji_messages = ai_messages[ai_messages["sarcastic_emoji"]]
    all_emojis = []
    for text in emoji_messages["text"]:
        all_emojis.extend(extract_emojis(text))
    
    emoji_freq = Counter(all_emojis)
    print(f"🔢 Found {len(emoji_freq)} unique emojis")
    if emoji_freq:
        print("Top 5 most frequent emojis:")
        for emoji_char, count in emoji_freq.most_common(5):
            print(f"  {emoji_char}: {count} times")
    
    # Step 4: Privacy redaction (basic implementation)
    print("🔒 Applying privacy redaction...")
    ai_messages["text_redacted"] = ai_messages["text"].apply(
        lambda x: re.sub(r"\b[A-Z][a-z]{2,}\b", "[NAME]", x) if pd.notna(x) else x
    )
    
    # Step 5: Dual-layer sarcasm detection
    print("🎯 Running dual-layer sarcasm detection...")
    
    # Strict mismatches: Positive words + negative emojis
    strict_pattern = r"\b(?:love|great|amazing|fantastic|wonderful|excellent|perfect)\b.*[\U0001F480\U0001F635\U0001F92C\U0001F921]"  # 💀 😵 🥴 🤡
    ai_messages["strict_mismatch"] = ai_messages["text_redacted"].str.contains(
        strict_pattern, case=False, na=False
    )
    
    # Broader tone contradictions
    ai_messages["tone_contradiction"] = ai_messages["text_redacted"].apply(detect_tone_contradiction)
    
    strict_count = ai_messages["strict_mismatch"].sum()
    tone_count = ai_messages["tone_contradiction"].sum()
    print(f"📋 Strict mismatches: {strict_count}")
    print(f"📋 Tone contradictions: {tone_count}")
    
    # Step 6: Create export dataset
    print("📄 Preparing export dataset...")
    df_export = ai_messages[(ai_messages["strict_mismatch"]) | (ai_messages["tone_contradiction"])].copy()
    
    if len(df_export) == 0:
        print("⚠️ No sarcasm patterns detected. Expanding search criteria...")
        # Fallback: export any AI message with emojis for manual review
        df_export = ai_messages[ai_messages["sarcastic_emoji"]].copy()
    
    # Final redaction pass
    df_export["text_final"] = df_export["text_redacted"].apply(
        lambda x: re.sub(r"\b\w{3,}\b", "[REDACTED]", x) if pd.notna(x) else x
    )
    
    # Add review columns
    df_export["is_real_sarcasm"] = ""  # For manual review
    df_export["confidence_level"] = ""  # For manual rating
    df_export["notes"] = ""  # For manual notes
    
    # Select relevant columns for export
    export_columns = [
        "text_final", "strict_mismatch", "tone_contradiction", 
        "sarcastic_emoji", "sent_at_utc", "is_real_sarcasm", 
        "confidence_level", "notes"
    ]
    
    df_final = df_export[export_columns].copy()
    
    # Randomize order to avoid chronological bias
    df_final = df_final.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Step 7: Export results
    output_file = "pi_sarcasm_hybrid_review.csv"
    df_final.to_csv(output_file, index=False)
    
    print(f"✅ Analysis complete!")
    print(f"📊 Exported {len(df_final)} candidates to {output_file}")
    print(f"🎯 Detection summary:")
    print(f"   - Strict mismatches: {df_final['strict_mismatch'].sum()}")
    print(f"   - Tone contradictions: {df_final['tone_contradiction'].sum()}")
    print(f"   - Messages with emojis: {df_final['sarcastic_emoji'].sum()}")
    print(f"\n🔍 Next steps:")
    print(f"   1. Open {output_file} in Excel/Google Sheets")
    print(f"   2. Focus on rows where both strict_mismatch AND tone_contradiction are True")
    print(f"   3. Manually review and mark 'is_real_sarcasm' column")
    print(f"   4. Look for patterns in the text_final column")

if __name__ == "__main__":
    main()