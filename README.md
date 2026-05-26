# Azure AI Vision 103

A comprehensive Python project for Azure AI Vision image analysis, demonstrating client connection and image tag extraction using the Azure Cognitive Services.

## Overview

This project provides four example scripts for working with Azure's Computer Vision API:

| Script | Purpose |
|--------|---------|
| **01_connect.py** | Establishes basic connection to Azure AI Vision service |
| **02_connect.py** | Analyzes images from URL and extracts visual tags |
| **03_caption.py** | Analyzes images from URL with tag output formatting |
| **04_local.py** | Analyzes local image files and extracts visual tags |

## Prerequisites

- Python 3.7 or higher
- Azure account with Computer Vision resource
- API key and endpoint from Azure Cognitive Services
- Image files (for 04_local.py)

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

## Usage Examples

### 1. Basic Connection Test
```bash
python 01_connect.py
```
**Output:**
```
Client created successfully.
```

### 2. Analyze Image from URL
```bash
python 02_connect.py
```
**Output:**
```
Client created successfully.
Tags found:
  cricket - 0.95
  bat - 0.91
  sport - 0.88
```

### 3. Analyze URL with Formatted Output
```bash
python 03_caption.py
```
**Output:**
```
Client created successfully.
TAGS:
  cricket - 0.95
  bat - 0.91
  sport - 0.88
```

### 4. Analyze Local Image File
```bash
python 04_local.py
```
**Output:**
```
Client created successfully.
TAGS:
  cricket - 0.95
  bat - 0.91
  sport - 0.88
```

**Note:** Update the `image_path` variable in `04_local.py` to point to your image file.

## Project Structure

```
Azure_AI_103/
├── 01_connect.py           # Basic connection test
├── 02_connect.py           # URL image analysis with tags
├── 03_caption.py           # URL image analysis (formatted output)
├── 04_local.py             # Local image file analysis
├── requirements.txt        # Project dependencies
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## Dependencies

- **azure-ai-vision-imageanalysis** - Azure Computer Vision SDK
- **streamlit** - Web app framework (for potential UI extensions)
- **pillow** - Image processing library

## Features

- ✅ Secure credential management via environment variables
- ✅ Image analysis from URLs
- ✅ Local image file processing
- ✅ Visual tag extraction with confidence scores
- ✅ Easy to extend with additional visual features

## Supported Visual Features

The project can be extended to support:
- 🏷️ Tags (currently implemented)
- 📦 Objects
- 📄 Text (OCR)
- 👤 Faces
- 🎨 Color analysis
- 🖼️ Image type detection
- 📝 Captions
- And more...

## Extending the Project

To add more visual features, modify the `visual_features` list:

```python
from azure.ai.vision.imageanalysis.models import VisualFeatures

result = client.analyze_from_url(
    image_url=image_url,
    visual_features=[
        VisualFeatures.TAGS,
        VisualFeatures.OBJECTS,
        VisualFeatures.CAPTION
    ]
)
```

## Error Handling Checklist

- ✓ Verify API key and endpoint are correct
- ✓ Check image URL is accessible
- ✓ Ensure Azure resource is active with available quota
- ✓ Confirm environment variables are set
- ✓ For local files: verify file path and permissions

## Security Best Practices

- ⚠️ **Never** hardcode API keys in source code
- ⚠️ Always use environment variables or secure secret management
- ⚠️ Consider using Azure Key Vault for production applications
- ⚠️ Use `.gitignore` to prevent accidental credential commits
- ⚠️ Rotate API keys regularly

## Resources

- [Azure AI Vision Documentation](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)
- [Python SDK Reference](https://aka.ms/azsdk-python-cognitiveservices-vision-computervision)
- [Azure Cognitive Services Pricing](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/computer-vision/)
- [Visual Features Guide](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/concept-analyzing-images)

## Troubleshooting

### "Client created successfully" but analysis fails
- Check that your Azure resource has available quota
- Verify the image URL is accessible
- Ensure your API credentials are current

### "File not found" error in 04_local.py
- Update the `image_path` variable to match your file location
- Use absolute path if script is in different directory

### Import errors
- Reinstall requirements: `pip install -r requirements.txt --upgrade`
- Verify virtual environment is activated

## License

This project is provided as-is for educational purposes.

## Support

For issues or questions, please refer to:
- [Azure AI Vision documentation](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)
- [Azure Support](https://azure.microsoft.com/en-us/support/)
