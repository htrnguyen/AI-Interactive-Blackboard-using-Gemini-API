import google.generativeai as genai
import numpy as np
import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas

st.set_page_config(layout="wide")
st.title("AI Interactive Blackboard")

# Cấu hình API key cho Google AI
genai.configure(api_key="YOUR_API_KEY")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
)

# Tạo layout với hai cột
col1, col2 = st.columns([4, 1])

with col1:
    st.header("Board")
    canvas_result = st_canvas(
        fill_color="rgba(0, 0, 0, 0)",
        stroke_width=2,
        stroke_color="#FFFFFF",
        background_color="#000000",
        width=1000,
        height=500,
        drawing_mode="freedraw",
        key="canvas",
    )


with col2:
    st.header("AI Response")

    if st.button("Send to AI"):
        if canvas_result.json_data:
            # Chuyển dữ liệu từ canvas sang ảnh
            img = Image.fromarray(canvas_result.image_data.astype(np.uint8))
            img = img.convert("RGB")

            # Gửi ảnh tới AI để sinh đáp án
            prompt = """
            You are an AI trained to recognize and classify images. Your task is to analyze the content of an image and provide a classification along with an appropriate response based on the category of the image. Here are the categories you should consider:

            1. Nature (e.g., trees, animals, landscapes): "This is a {specific object, e.g., tree, dog, mountain}."
            2. Mathematical expressions (e.g., equations, graphs): "This is a mathematical expression. The solution to the problem is {solution}."
            3. Geometric shapes (e.g., circles, squares, polygons): "This is a geometric shape. It is a {specific shape, e.g., circle, square}."
            4. Physics (e.g., diagrams, experiments): "This is a physics-related image. It shows {specific concept, e.g., a force diagram, an experiment setup}."
            5. Chemistry (e.g., chemical structures, reactions): "This is a chemistry-related image. It represents {specific concept, e.g., a chemical structure, a reaction}."

            Please classify the following image and provide an appropriate response based on its content.
            """
            response = model.generate_content([prompt, img])

            # Hiển thị đáp án
            st.write(response.text)
        else:
            st.write("Please draw something first!")
