# Tootle: Revolutionizing Development with GPT 🚀

Welcome to \*\*Tootle\*\* 🌟, a transformative project inspired by the engineering philosophies of Google. The name "Tootle" is a play on words, drawing inspiration from the phonetic sound of "Google" 🌍 and the Chinese term "秃头" (which means bald) 🤖. It captures our ambition to revolutionize software engineering by letting GPT handle significant portions of large-scale coding projects.

## Quick Start 🏁

To get started with our devbots, simply initiate them with your natural language requirement and they will serve you with detailed results:

```python
from tootle import Developer, LLMResponse

response: LLMResponse = Developer().serve(user_message="Write a function to reverse a string")
print(response.code)
print(response.explanation)
```

## Key Features

### Seamless Devbot Communication 🤝

Our GPT devbots can interact seamlessly, creating and understanding interrelated demand files. For instance, `APIDocumentationArchitect` generates an `api-description.json` that can be interpreted and processed by `InterfaceDesigner`.

Example:

```python
import json
import pathlib
from tootle import InterfaceDesigner, CodeWriter

# Load the API designs
design_json = json.load(open("./design.json", "r"))

# Design the APIs using the InterfaceDesigner
interface_designer = InterfaceDesigner()

for api_design in design_json:
    api_file_path = pathlib.Path(api_design['api_file_name'])
    api_name = api_design['api_name']
    api_task_description = api_design['api_task_description']

    print(f"Designing API: {api_name}...")
    result = interface_designer.serve(api_task_description)
    print(f"API {api_name} designed. Explanation: {result.explanation}. Code written to {api_file_path}")

    CodeWriter.write_code(api_file_path, result.code)

```


### The Autom Format 📜

Tootle is built around the innovative [**antom** format](https://github.com/stevieflyer/autom). This novel configuration format enables humans to fine-tune the input, output, objectives, and formatting alignment of GPT bots. By ensuring meticulous architectural design through the antom format, we guarantee impressive GPT chaining performance.

Creating a new bot is as simple as defining a new `.autom/[role].json` file:

```json
{
  "title": "API Documentation Architect",
  "job-description": "Conceptualize, design, and outline a comprehensive series of API descriptions in JSON format, capturing the essence of intended functionalities without delving into code details.",
  "model": "gpt-3.5-turbo-16k-0613",
  "extra-guidance-requirements": [
    "Adhere to a structured JSON format for clarity.",
    "Designs should be scalable and consider future modifications.",
    "Maintain consistency in naming conventions and hierarchy.",
    "Ensure thoroughness and precision in the API design."
  ],
  "extra-format-requirements": [
    "For JSON representations, start with 'MAGIC$$$', and conclude with '$$$'.",
    "For additional explanations, begin with 'MAGIC%%%', and finish with '%%%'."
  ],
  "examples": [
    {
      "query": "Design an API structure for a cloud-based file storage system.",
      "response": "MAGIC$$$\n{\n  \"apis\": [\n    {\n      \"api_name\": \"FileManagementAPI\",\n      \"api_task_description\": \"Handle file uploads, downloads, and metadata operations.\"\n    },\n    {\n      \"api_name\": \"UserManagementAPI\",\n      \"api_task_description\": \"Manage user registrations, permissions, and activity logs.\"\n    },\n    {\n      \"api_name\": \"StorageAnalyticsAPI\",\n      \"api_task_description\": \"Provide insights into storage usage, file access patterns, and potential optimizations.\"\n    },\n    {\n      \"api_name\": \"IntegrationAPI\",\n      \"api_task_description\": \"Facilitate third-party app integrations and handle API key management.\"\n    }\n  ]\n}$$$\nMAGIC%%%\nThe APIs designed for the cloud-based file storage system cover key functionalities, ensuring a comprehensive solution. Note: This example illustrates the structure and is not exhaustive.%%%"
    }
  ]
}
```


For a detailed proposal on the **antom** format, visit our [GitHub discussion](https://github.com/stevieflyer/autom).

### Collaboration with proj-bolt 🔩

Tootle is envisioned to integrate seamlessly with [proj-bolt](https://pypi.org/project/proj-bolt/), enabling intelligent code generation in the future.

## Future Roadmap (TODO) 🗺️


1. **Interactive Code Generation** Elevate from singular responses to an engaging interactive code creation experience.
2. **Expanded Devbot Mesh**: Develop an array of specialized devbots to form an intricate development web.

## Conclusion 🎉

**Tootle** is your gateway to future-oriented, GPT-powered software development. Join us on this journey and experience the transformative potential of GPT in coding.

Contributions, ideas, and feedback are always welcome!
