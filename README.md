# AI Clothing Store Assistant Chatbot

An AI-powered (multi-shot prompting) chatbot that acts as a helpful clothing store assistant, built with Google's Gemini AI model and Gradio for the web interface.

## Features

- **Intelligent Sales Assistant**: The AI assistant helps customers find clothing items while gently encouraging them to explore sale items
- **Multi-shot Prompting**: Uses contextual prompting to maintain consistent behavior as a clothing store assistant
- **Real-time Streaming**: Responses are streamed in real-time for a smooth user experience
- **Product Recommendations**: Actively promotes items on sale with specific discounts


## Requirements

- Python 3.7+
- Google API Key for Gemini AI
- Required packages (install via pip):
  ```bash
  pip install openai python-dotenv gradio
  ```

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ai-clothing-store-assistant
   ```

2. **Create a `.env` file** in the project root:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

3. **Get your Google API Key**:
   - Go to [Google AI Studio](https://aistudio.google.com/)
   - Create a new API key
   - Copy the key to your `.env` file

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Access the chatbot**:
   - Open your browser and go to `http://localhost:7860`
   - Start chatting with the AI clothing store assistant

## How It Works

The chatbot uses Google's Gemini 2.5 Flash model through the OpenAI-compatible API. It's programmed with a detailed system message that:

- Defines its role as a helpful clothing store assistant
- Provides specific product information and pricing
- Encourages customers to try sale items, especially hats (60% off)
- Offers personalized recommendations based on customer inquiries
- Maintains a friendly, sales-oriented conversation style

## Example Interactions

- **Customer**: "I'm looking for a hat"
- **Assistant**: "Wonderful - we have lots of hats - including several that are part of our sales event with 60% off!"

- **Customer**: "Do you have kids clothes?"
- **Assistant**: "Yes! We have a wide variety of kids clothes available and I'd encourage you to try them out..."

## Technology Stack

- **AI Model**: Google Gemini 2.5 Flash Preview
- **Web Framework**: Gradio
- **API Client**: OpenAI Python SDK
- **Environment Management**: python-dotenv

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the clothing store assistant experience.

## License

This project is open source and available under the [MIT License](LICENSE).
