# Copilot Instructions for Data Repository

## Project Overview
This repository contains miscellaneous data files, primarily focused on conversation history and AI interaction data. The main asset is a comprehensive JSON conversation log between a user and an AI assistant (Pi).

## Key Files and Structure
- `Copy of pi-user-history.json` - Large conversation history file (26K+ lines) containing timestamped messages between human and AI
- `README.md` - Basic project description ("Misc data")

## Data Format Patterns
The JSON conversation log follows this structure:
```json
{
  "user_data": {
    "details": {
      "created_at": "2024-04-16T17:51:56.746",
      "first_name": "Colleenpridemore@gmail.com",
      "identifiers": [{"type": "PHONE_NUMBER", "identifier": "+12248052281"}],
      "entry_channel": "SMS"
    },
    "messages": [
      {
        "text": "message content",
        "sender": "HUMAN|AI", 
        "channel": "SMS",
        "sent_at": "2024-04-16T17:51:56.74"
      }
    ]
  }
}
```

## Content Context
The conversation data covers topics including:
- AI development and SingularityNET ecosystem
- Assistive technology for disabled individuals
- AI agents and ethics training
- AGI/ASI development discussions
- Personal projects and business development

## Primary Use Cases
- **Sarcasm Detection**: Analyze Pi.ai's communication patterns, particularly emoji usage as sarcastic indicators
- **Emoji Analysis**: Identify where Pi uses emojis potentially as sarcasm (🤡, 😒, etc.)

## Working with This Repository
- **Data Analysis**: Use pandas for efficient data manipulation and analysis:
  ```python
  import pandas as pd  
  df = pd.read_json("Copy of pi-user-history.json")  
  df["sent_at_utc"] = pd.to_datetime(df["sent_at"]).dt.tz_convert("UTC")  # Normalize timestamps
  ```
- **Emoji Analysis**: Use the emoji library to detect sarcastic patterns:
  ```python
  import emoji  
  df["sarcastic_emoji"] = df["text"].apply(lambda x: any(e in emoji.UNICODE_EMOJI for e in x))
  ```
- **Emoji Frequency Analysis**: Discover under-the-radar sarcastic emojis by analyzing frequency patterns:
  ```python
  # Count emojis in messages flagged as potentially sarcastic
  df_sarcastic = df[df["sarcastic_emoji"]]  
  from collections import Counter  
  emoji_freq = Counter([e for text in df_sarcastic["text"] for e in extract_emojis(text)])  # Define `extract_emojis()`!
  ```
  Focus on core sarcastic indicators (🤡😒🙄🥴) and discover new patterns
- **Context Clues**: Analyze emoji-word combinations for sarcastic tone patterns:
  ```python
  # Flag positive words with negative emojis (e.g., "love" with eye-roll)
  df["sarcasm_context"] = df["text"].str.contains(r"\b(?:love|fantastic)\b.*[\U0001F480]")  # 💀 Unicode example
  # Manual review recommended for ambiguous emojis (💀, 🐛) to validate sarcastic usage
  ```
- **Dual-Layer Sarcasm Detection**: Combine strict patterns with broader tone analysis:
  ```python
  # Strict Mismatches: Positive word + Negative Emoji  
  strict_pattern = r"\b(?:love|great|amazing|fantastic)\b.*[\U0001F480\U0001F635\U0001F92C]"  # 💀 😒 🥴 example  
  df["strict_mismatch"] = df["text_redacted"].str.contains(strict_pattern)  

  # Broader Tone Contradictions: Neutral word + Sarcastic Emoji (custom logic!)  
  def detect_tone_contradiction(text):  
      neutral_words = r"\b(?:sure|whatever|fine|okay|alright)\b"  # Example seed list—expand yours!  
      sarcastic_emojis = r"[\U0001F612\U0001F614\U0001F635\U0001F92C]"  # 😒 🙄 🥴 etc.—add your core list!  
      return bool(re.search(f"{neutral_words}.*{sarcastic_emojis}", text))  # Adjust spacing/word boundaries as needed  

  df["tone_contradiction"] = df["text_redacted"].apply(detect_tone_contradiction)  
  ```
- **Export Sarcasm Analysis**: Merge detection flags and prepare review dataset:
  ```python
  # Merge flags into one review set  
  df_export = df[(df["strict_mismatch"]) | (df["tone_contradiction"])].copy()  

  # Final redaction pass (enhanced from earlier steps)  
  df_export["text_final"] = df_export["text_redacted"].apply(  
      lambda x: re.sub(r"\b\w{2,}\b", "[REDACTED]", x) if not pd.isna(x) else x  # Mask all standalone words >2 letters  
  )  

  # Optional: Randomize order to avoid biasing reviewers toward recent examples  
  df_export = df_export.sample(frac=1).reset_index(drop=True)  

  # Save!  
  df_export.to_csv("pi_sarcasm_hybrid_review.csv", index=False)  
  ```
- **Review and Validate Results**: Execute analysis and manually review findings:
  ```python
  # The script will flag 200+ rows where either detection method triggers
  # Output CSV contains: redacted text, boolean flags, original timestamps
  
  # Manual review process:
  # 1. Focus on rows where both strict_mismatch AND tone_contradiction are True
  # 2. Sort by flags to prioritize strongest sarcasm candidates  
  # 3. Add "is_real_sarcasm" column for manual validation of ambiguous cases
  # 4. Look for patterns: "I love debugging! 💀" vs "Sure, whatever 😒"
  ```
- **Advanced Sarcasm Detection**: For contextual analysis beyond emojis, consider pre-trained NLP models:
  ```python
  from transformers import pipeline
  classifier = pipeline("text-classification", model="distilbert-base-uncased")
  # Fine-tuning options available for domain-specific sarcasm detection
  ```
- **Search Patterns**: When searching the conversation log, use keywords like "sarcasm", "agent", "AI", "project", "development"
- **File Size**: The main JSON file is large (26K+ lines) - consider streaming or chunked processing for analysis
- **Privacy**: This contains personal conversation data - handle with appropriate privacy considerations

## Privacy Safeguards
- **Anonymize Senders**: Replace "sender": "HUMAN" with pseudonyms (e.g., "USER_001") if sharing data externally
- **Redact Sensitive Text**: Automatically blur personal identifiers using regex or libraries like faker:
  ```python
  import re  
  df["text_redacted"] = df["text"].apply(lambda x: re.sub(r"\b[A-Z][a-z]+\b", "[REDACTED]", x))  # Simple name masking
  ```

## Repository Context
- Simple data storage repository under Violet-Site-Systems organization
- No build system or dependencies required
- Primarily for data archival and potential analysis purposes
- Main branch: `main`