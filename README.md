# Speech-To-Text

This Python program uses the `speech_recognition` library to perform real-time speech recognition using a microphone as the audio source. The program continuously listens to spoken words, transcribes them into text, and provides a list of available microphones for selection.

## Key Features:

1. **Speech Recognition:** The program employs Google's speech recognition service to convert spoken words into text. It adjusts for ambient noise to enhance recognition accuracy.

2. **Continuous Listening:** The code operates in an infinite loop, continually listening for spoken commands. It captures audio from the microphone and processes it for speech recognition.

3. **Text Output:** Recognized speech is displayed as text on the console. The recognized command is printed in lowercase for consistency.

4. **Error Handling:** The program includes error handling to address various situations. It differentiates between cases where no speech is recognized and errors related to the recognition service itself, such as network issues.

5. **Microphone Selection:** After each recognition attempt, the program provides a list of available microphones along with their respective indices. This information can help users select a specific microphone for input.

6. **User Interaction (Optional):** The program optionally waits for user input (pressing Enter) before continuing to the next recognition cycle. This pause allows users to read the microphone list and select an appropriate microphone if needed.

## Usage:

- To use this program, ensure that you have the `speech_recognition` library installed in your Python environment using the command `pip install SpeechRecognition`.

- Run the program, and it will continuously listen for spoken commands, recognize them, and display the recognized text on the console.

- The program also lists available microphones, which can be helpful if you have multiple microphones connected to your system. Users can select a specific microphone by its index if necessary.

- To exit the program, you can manually terminate it (e.g., by pressing Ctrl+C) or implement a specific exit command within the recognition loop.

## Note: 
Continuous running of this program may consume significant CPU resources, so use it judiciously. Additionally, internet connectivity is required for using Google's speech recognition service.

This program can be customized and extended to perform various voice-activated tasks or voice commands for automation or interaction with applications.
