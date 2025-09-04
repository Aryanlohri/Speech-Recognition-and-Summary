# 🎙️ Speech Recognition and Summarization

This project converts spoken audio into text and then generates a concise summary of the recognized speech.  
It combines **speech recognition**, **natural language processing (NLP)**, and **text-to-speech** to make information more accessible and efficient.

---

## 🚀 Features
- 🎤 Convert speech/audio into text  
- 📝 Summarize long transcriptions into concise key points  
- 🔊 Convert summaries back into speech (Text-to-Speech)  
- 🖥️ Simple and modular Python code  
- ⚡ Works offline/online depending on chosen model  

---

## 🛠️ Technology Stack
- **Python 3.9+**
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) – for converting audio to text  
- [Transformers (HuggingFace)](https://huggingface.co/transformers/) – for text summarization  
- [gTTS](https://pypi.org/project/gTTS/) – for text-to-speech  
- **Other libraries**: `os`, `pyaudio` (optional), etc.  

---

## 📂 Project Structure
```
Speech-Recognition-and-Summary/
│-- speech_recognition/    # Speech recognition logic
│-- summarizer/            # Text summarization logic
│-- main.py                # Main script to run the app
│-- requirements.txt       # Dependencies
│-- README.md              # Documentation
```

---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Aryanlohri/Speech-Recognition-and-Summary.git
   cd Speech-Recognition-and-Summary
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate    # Windows
   source venv/bin/activate # Mac/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

Run the project with:
```bash
python main.py
```

- Speak into your microphone, and the system will transcribe your speech.  
- The recognized text will be summarized.  
- Optionally, the summary will be read aloud using text-to-speech.  

---

## 📌 Example

**Input Speech:**  
*"Artificial Intelligence is transforming industries by automating tasks, improving decision-making, and enhancing productivity."*  

**Recognized Text:**  
Artificial Intelligence is transforming industries by automating tasks, improving decision-making, and enhancing productivity.  

**Summary:**  
AI automates tasks and improves decision-making across industries.  

---

## 🙌 Contributions
Feel free to fork this repo, open issues, or submit pull requests to improve features or fix bugs.  

---

## 📜 License
This project is licensed under the **MIT License** – you are free to use, modify, and distribute it.  
