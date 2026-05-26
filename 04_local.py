import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

api_key = os.getenv("AZURE_AI_API_KEY")
vision_endpoint = os.getenv("AZURE_AI_ENDPOINT")

credential = AzureKeyCredential(api_key)

client = ImageAnalysisClient(
    endpoint=vision_endpoint,
    credential=credential
)

print("Client created successfully.")

# Update this path to point to your local image file
image_path = "desktop-374078.jpg"

with open(image_path, "rb") as image_file:
    result = client.analyze(
        image_data=image_file,
        visual_features=[VisualFeatures.TAGS]
    )

print("TAGS:")
for tag in result.tags.list:
    print(f"  {tag.name} - {tag.confidence:.2f}")