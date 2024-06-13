# AI Interactive Blackboard using Gemini API

This project uses Streamlit to create an interactive blackboard and Google's Gemini API to classify and respond based on the content of the drawing.

## Requirements

-   Python 3.8 or higher
-   Python libraries:
    -   streamlit
    -   streamlit-drawable-canvas
    -   google-generativeai
    -   numpy
    -   pillow

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/nguyenn-04/AI-Interactive-Blackboard-using-Gemini-API.git
    cd AI-Interactive-Blackboard-using-Gemini-API
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

    **Alternatively, install the libraries manually:**

    ```bash
    pip install streamlit streamlit-drawable-canvas google-generativeai numpy pillow
    ```

3. Ensure you have a valid API key from Google AI and configure it in the source code.

## Usage

Run the Streamlit application:

```bash
streamlit run project_using_gemini.py
```

Open your browser and go to [http://localhost:8501](http://localhost:8501) to view the application.

Draw or write on the blackboard and click "Send to AI" to send the image to the AI and receive a classified response based on the content.

For more information on the Gemini API, refer to the [Gemini API Documentation](https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=python).

## Demo

[![Demo Video](http://img.youtube.com/vi/sWyMG4DSB-s/0.jpg)](http://www.youtube.com/watch?v=sWyMG4DSB-s "Demo Video")