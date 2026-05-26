# Azure AI Vision 103

A Python project for Azure AI Vision image analysis, demonstrating client connection and image tag extraction using the Azure Cognitive Services.

## Overview

This project provides two example scripts for working with Azure's Computer Vision API:
- **01_connect.py** - Establishes a basic connection to the Azure AI Vision service
- **02_connect.py** - Analyzes images and extracts visual tags

## Prerequisites

- Python 3.7 or higher
- Azure account with Computer Vision resource
- API key and endpoint from Azure Cognitive Services

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sds4670/Azure_AI_103.git
cd Azure_AI_103
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Set your Azure credentials as environment variables:

### On Linux/Mac:
```bash
export AZURE_AI_API_KEY="your-api-key"
export AZURE_AI_ENDPOINT="your-endpoint-url"
```

### On Windows (PowerShell):
```powershell
$env:AZURE_AI_API_KEY="your-api-key"
$env:AZURE_AI_ENDPOINT="your-endpoint-url"
```

### On Windows (Command Prompt):
```cmd
set AZURE_AI_API_KEY=your-api-key
set AZURE_AI_ENDPOINT=your-endpoint-url
```

## Usage

### 1. Basic Connection Test
```bash
python 01_connect.py
```
Output:
```
Client created successfully.
```

### 2. Analyze Image and Extract Tags
```bash
python 02_connect.py
```
Output:
```
Client created successfully.
Tags found:
  cricket - 0.95
  bat - 0.91
  sport - 0.88
  ...
```

## Dependencies

- **azure-ai-vision-imageanalysis** - Azure Computer Vision SDK
- **streamlit** - Web app framework (for potential UI extensions)
- **pillow** - Image processing library

## Project Structure

```
Azure_AI_103/
├── 01_connect.py           # Basic connection script
├── 02_connect.py           # Image analysis script
├── requirements.txt        # Project dependencies
└── README.md              # This file
```

## Features

- ✅ Secure credential management via environment variables
- ✅ Image analysis from URLs
- ✅ Visual tag extraction with confidence scores
- ✅ Easy to extend with additional visual features

## Supported Visual Features

The project can be extended to support:
- Tags
- Objects
- Text (OCR)
- Faces
- Color analysis
- Image type detection
- And more...

## Error Handling

Make sure to:
1. Verify your API key and endpoint are correct
2. Check that the image URL is accessible
3. Ensure your Azure resource is active and has available quota

## Security Notes

- **Never** hardcode API keys in your code
- Always use environment variables or secure secret management
- Consider using Azure Key Vault for production applications

## Resources

- [Azure AI Vision Documentation](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)
- [Python SDK Reference](https://aka.ms/azsdk-python-cognitiveservices-vision-computervision)
- [Azure Cognitive Services Pricing](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/computer-vision/)

## License

This project is provided as-is for educational purposes.

## Support

For issues or questions, please refer to the [Azure AI Vision documentation](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/) or contact Azure support.
