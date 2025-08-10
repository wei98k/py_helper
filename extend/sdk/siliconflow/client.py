import requests

class SiliconFlowClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.siliconflow.cn/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

    def api_call(self, endpoint, method="GET", data=None, files=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            if method.upper() == "GET":
                response = requests.get(url, headers=self.headers, params=data)
            elif method.upper() == "POST":
                if files:
                    # For multipart/form-data requests
                    response = requests.post(url, headers=self.headers, data=data, files=files)
                else:
                    # For JSON requests
                    response = requests.post(url, headers={**self.headers, "Content-Type": "application/json"}, json=data)
            else:
                raise ValueError("Unsupported HTTP method")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return None

    def transcribe_audio(self, file_path, model="FunAudioLLM/SenseVoiceSmall"):
        """Transcribe audio file to text

        Args:
            file_path (str): Path to the audio file
            model (str, optional): Model to use for transcription. Defaults to "FunAudioLLM/SenseVoiceSmall".

        Returns:
            dict: Transcription result
        """
        endpoint = "audio/transcriptions"
        data = {
            "model": model
        }
        files = {
            "file": open(file_path, "rb")
        }
        try:
            return self.api_call(endpoint, method="POST", data=data, files=files)
        finally:
            # Ensure the file is closed
            files["file"].close()