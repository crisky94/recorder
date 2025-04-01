# 🎙️ Mini Recorder in Python

This is a small Python project that allows you to record audio using the `sounddevice` library.  
The user can select their recording device, and the audio is saved in `.wav` format.  

---

## 📌 Features  
✅ Records audio from the microphone.  
✅ Allows you to choose the recording device.  
✅ Saves audio in `.wav` format.  
✅ Easy to use from the terminal.  

---

## 🛠️ Installation  

Make sure you have **Python 3.x** installed and run the following command to install the dependencies:  

```sh
pip install sounddevice numpy scipy

```
## 🎬 Usage

1. **Run the script:**

   ```sh
   python recorder.py

   ```

2. A list of input/output devices will be displayed.

3. Enter the number of the recording device.

4. The program will record for 5 seconds and save the file as recording.wav.
 

## 🔧 Additional Configuration

- You can change the recording duration by editing the duration variable in the code.

- To change the sampling frequency, modify freq = 44100 (common values: 44100, 48000).

## Enjoy recording! 🎤✨
