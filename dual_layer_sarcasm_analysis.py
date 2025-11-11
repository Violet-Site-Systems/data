#!/usr/bin/env python3
"""
Dual-layer sarcasm detection on readable Pi.ai messages
Following Aethel's methodology with minimal redaction for actual analysis
"""

import pandas as pd
import json
import re
import emoji
from collections import Counter

def minimal_redaction(text):
    """Very light redaction - just mask obvious personal info"""
    if pd.isna(text):
        return text
    
    # Only mask emails and phone numbers, keep everything else
    text = re.sub(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', '[EMAIL]', text)
    text = re.sub(r'\b\+?1?[\s.-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b', '[PHONE]', text)
    
    return text

def detect_tone_contradiction(text):
    """Detect neutral/dismissive words paired with sarcastic emojis"""
    if pd.isna(text):
        return False
    
    neutral_words = r"\b(?:sure|whatever|fine|okay|alright|right|yeah|mhmm|uh|huh|oh|well)\b"
    sarcastic_emojis = r"[\U0001F612\U0001F614\U0001F635\U0001F92C\U0001F921\U0001F480]"  # 😒 🙄 😵 🥴 🤡 💀
    
    return bool(re.search(f"{neutral_words}.*{sarcastic_emojis}", text, re.IGNORECASE))

def main():
    print("🎯 Running dual-layer sarcasm detection on readable Pi.ai messages...")
    
    # Load original data
    with open("Copy of pi-user-history.json", "r") as f:
        data = json.load(f)
    
    messages = pd.DataFrame(data['user_data']['messages'])
    ai_messages = messages[messages["sender"] == "AI"].copy()
    
    # Apply minimal redaction
    ai_messages["text_readable"] = ai_messages["text"].apply(minimal_redaction)
    
    # Basic emoji detection
    ai_messages["has_emoji"] = ai_messages["text"].apply(
        lambda x: any(e in emoji.EMOJI_DATA for e in x) if pd.notna(x) else False
    )
    
    emoji_messages = ai_messages[ai_messages["has_emoji"]].copy()
    print(f"📊 Analyzing {len(emoji_messages)} Pi.ai messages with emojis...")
    
    # Emoji frequency analysis
    all_emojis = []
    for text in emoji_messages["text"]:
        all_emojis.extend([char for char in text if char in emoji.EMOJI_DATA])
    
    emoji_freq = Counter(all_emojis)
    print(f"\n📈 Emoji frequency analysis:")
    print("Top 10 most used emojis by Pi.ai:")
    for emoji_char, count in emoji_freq.most_common(10):
        print(f"  {emoji_char}: {count} times")
    
    # Dual-layer sarcasm detection
    print(f"\n🔍 Running dual-layer sarcasm detection...")
    
    # Layer 1: Strict mismatches (positive words + negative emojis)
    strict_pattern = r"\b(?:love|great|amazing|fantastic|wonderful|excellent|perfect|awesome|brilliant)\b.*[\U0001F480\U0001F635\U0001F92C\U0001F921\U0001F612]"  # 💀 😵 🥴 🤡 😒
    emoji_messages["strict_mismatch"] = emoji_messages["text_readable"].str.contains(
        strict_pattern, case=False, na=False
    )
    
    # Layer 2: Tone contradictions (neutral/dismissive + sarcastic emojis)
    emoji_messages["tone_contradiction"] = emoji_messages["text_readable"].apply(detect_tone_contradiction)
    
    strict_count = emoji_messages["strict_mismatch"].sum()
    tone_count = emoji_messages["tone_contradiction"].sum()
    
    print(f"📋 Strict mismatches (positive word + negative emoji): {strict_count}")
    print(f"📋 Tone contradictions (neutral word + sarcastic emoji): {tone_count}")
    
    # Look for potential sarcastic emojis beyond the core set
    sarcastic_emoji_candidates = ['🤡', '😒', '🙄', '🥴', '💀', '🐛', '😏', '🤭', '😅']
    
    print(f"\n🕵️ Analyzing potential sarcastic emoji usage...")
    for candidate in sarcastic_emoji_candidates:
        count = emoji_freq.get(candidate, 0)
        if count > 0:
            print(f"  {candidate}: {count} times - POTENTIAL SARCASM INDICATOR")
            # Show examples
            examples = emoji_messages[emoji_messages["text_readable"].str.contains(re.escape(candidate), na=False)]
            if len(examples) > 0:
                print(f"    Example: \"{examples.iloc[0]['text_readable'][:100]}...\"")
    
    # Combine detection results
    sarcasm_candidates = emoji_messages[
        (emoji_messages["strict_mismatch"]) | 
        (emoji_messages["tone_contradiction"])
    ].copy()
    
    if len(sarcasm_candidates) == 0:
        print(f"\n⚠️ No strict sarcasm patterns detected using Aethel's criteria.")
        print(f"Let's expand the search to look for subtler patterns...")
        
        # Broader search for potentially sarcastic patterns
        expanded_patterns = [
            r"oh.*[😒🙄🥴💀]",  # "Oh" with sarcastic emoji
            r"really.*[😒🙄🤭]",  # "Really" with sarcastic emoji  
            r"interesting.*[🤔😏]",  # "Interesting" which can be sarcastic
            r"[😅🤭].*indeed",  # Nervous laugh with "indeed"
        ]
        
        emoji_messages["broader_sarcasm"] = False
        for pattern in expanded_patterns:
            emoji_messages["broader_sarcasm"] |= emoji_messages["text_readable"].str.contains(
                pattern, case=False, na=False
            )
        
        broader_candidates = emoji_messages[emoji_messages["broader_sarcasm"]]
        print(f"🔍 Found {len(broader_candidates)} messages with broader sarcasm patterns")
        
        if len(broader_candidates) > 0:
            sarcasm_candidates = broader_candidates.copy()
            sarcasm_candidates["detection_type"] = "broader_pattern"
        else:
            # If still no results, show some examples with potentially ambiguous emojis
            ambiguous_emojis = ['😅', '🤭', '😏', '🤔']
            ambiguous_candidates = emoji_messages[
                emoji_messages["text_readable"].str.contains('|'.join(re.escape(e) for e in ambiguous_emojis), na=False)
            ]
            if len(ambiguous_candidates) > 0:
                sarcasm_candidates = ambiguous_candidates.head(20).copy()  # Limit to 20 for review
                sarcasm_candidates["detection_type"] = "ambiguous_emoji"
                print(f"📝 Selected {len(sarcasm_candidates)} messages with potentially ambiguous emojis for manual review")
    else:
        sarcasm_candidates["detection_type"] = "dual_layer"
    
    # Add manual review columns
    sarcasm_candidates["is_real_sarcasm"] = ""
    sarcasm_candidates["confidence_level"] = ""  
    sarcasm_candidates["notes"] = ""
    
    # Select columns for export
    export_columns = [
        "text_readable", "strict_mismatch", "tone_contradiction", 
        "has_emoji", "sent_at", "detection_type",
        "is_real_sarcasm", "confidence_level", "notes"
    ]
    
    # Handle missing columns
    for col in ["strict_mismatch", "tone_contradiction"]:
        if col not in sarcasm_candidates.columns:
            sarcasm_candidates[col] = False
    
    df_export = sarcasm_candidates[export_columns].copy()
    
    # Save results
    output_file = "pi_sarcasm_readable_analysis.csv"
    df_export.to_csv(output_file, index=False)
    
    print(f"\n✅ Analysis complete!")
    print(f"📊 Exported {len(df_export)} candidates to {output_file}")
    print(f"\n🎯 Detection summary:")
    if len(df_export) > 0:
        detection_types = df_export["detection_type"].value_counts()
        for dtype, count in detection_types.items():
            print(f"   - {dtype}: {count} messages")
    
    print(f"\n🔍 Next steps:")
    print(f"   1. Open {output_file} in Excel/Google Sheets")
    print(f"   2. Review the 'text_readable' column for sarcastic patterns")
    print(f"   3. Mark 'is_real_sarcasm' column (True/False)")
    print(f"   4. Rate 'confidence_level' (High/Medium/Low)")
    print(f"   5. Add 'notes' for interesting patterns")
    
    # Show a few examples
    if len(df_export) > 0:
        print(f"\n📝 Sample candidates for review:")
        for i, (_, row) in enumerate(df_export.head(3).iterrows()):
            print(f"{i+1}. [{row['sent_at']}] ({row['detection_type']})")
            print(f"   \"{row['text_readable'][:150]}...\"")
            print()

if __name__ == "__main__":
    main()