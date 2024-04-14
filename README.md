# WordWise-Assist

This application suggests words based on the input keyword. It uses the Jaccard similarity to find similar words and ranks them based on their similarity and frequency in the text.

## Instructions to run locally

1. **Clone the repository:**

    ```zsh
    git clone https://github.com/deepanshu-rawat6/WordWise-Assist.git
    ```

2. **Navigate to the project directory:**

    ```zsh
    cd WordWise-Assist
    ```

3. **Create a virtual environment:**

    ```zsh
    python3 -m venv <virtual_environment>
    ```

4. **Activate the virtual environment:**

    ```zsh
    source <venv>/bin/activate
    ```

5. **Install the required Python packages:**

    ```
    pip install -r requirements.txt
    ```

    This command installs the necessary Python packages as specified in the `requirements.txt` file.

6. **Run the application:**

    ```
    streamlit run app.py
    ```

    This command starts the Streamlit server and opens the application in your default web browser.