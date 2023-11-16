import tkinter as tk
import speech_recognition as sr

class MicrophoneTranscriptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Microphone Transcription")

        self.label = tk.Label(root, text="Transcription:")
        self.label.pack(pady=10)

        self.transcription_var = tk.StringVar()
        self.transcription_label = tk.Label(root, textvariable=self.transcription_var, wraplength=400)
        self.transcription_label.pack(pady=10)

        self.transcription_button = tk.Button(root, text="Start Transcription", command=self.transcribe_from_microphone)
        self.transcription_button.pack(pady=10)

    def transcribe_from_microphone(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Say something...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = recognizer.listen(source, timeout=100)  # Listen for up to 10 seconds

        try:
            text = recognizer.recognize_google(audio)
            self.transcription_var.set("Transcription: {}".format(text))
        except sr.UnknownValueError:
            self.transcription_var.set("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            self.transcription_var.set("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = MicrophoneTranscriptionApp(root)
    root.mainloop()
