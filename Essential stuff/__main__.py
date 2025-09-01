import speech_recognition as sr
from transformers import pipeline

r = sr.Recognizer()
m = sr.Microphone()

# Make recognizer more sensitive and responsive
r.energy_threshold = 5      # Lowered for more sensitivity
r.pause_threshold = 0.5     # Reacts quickly after you stop speaking
r.dynamic_energy_threshold = False  # Prevent auto-adjust

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt", device=-1)

try:
    print("Energy threshold fixed at:", r.energy_threshold)
    while True:
        print("\nSay something!")
        with m as source:
            audio = r.listen(source, phrase_time_limit=8)  # Listens for up to 8 seconds per phrase
        print("Got it! Recognizing...")
        try:
            value = r.recognize_google(audio)
            print("\nYou said:\n------------------")
            print(value)
            if len(value.split()) > 5:
                try:
                    summary_result = summarizer(value, max_length=50, min_length=10, do_sample=False)
                    print("\nSummary:\n------------------")
                    print(summary_result[0]['summary_text'])
                except Exception as e:
                    print("\n(Summarization failed: {})".format(e))
            else:
                print("\n(Speech too short to summarize.)")
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass

