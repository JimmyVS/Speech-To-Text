import speech_recognition as sr

# Create a recognizer object
recognizer = sr.Recognizer()

while True:

    print("Listening...")

    # Use a microphone as the audio source
    with sr.Microphone() as source:
        # Adjust for ambient noise to improve recognition accuracy
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        # Listen to the audio from the microphone
        recorded_audio = recognizer.listen(source)

    try:
        # Recognize the spoken text using Google's speech recognition service
        text = recognizer.recognize_google(
            recorded_audio, 
            language="en-US"
        )
        text = text.lower()
        
        # Print the recognized command
        print("Recognized Command: {}".format(text))

    except sr.UnknownValueError:
        # Handle cases where no speech could be recognized
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as ex:
        # Handle errors with the recognition service (e.g., network issues)
        print(f"Error accessing the recognition service: {ex}")

    # Wait for user input to continue (optional)
    input("Press Enter to continue...")
    print("")
