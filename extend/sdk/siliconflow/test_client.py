import unittest
from unittest.mock import patch, MagicMock
import os
from client import SiliconFlowClient


class TestSiliconFlowClient(unittest.TestCase):
    def setUp(self):
        # 设置测试用例
        self.api_key = "test_api_key"
        self.client = SiliconFlowClient(self.api_key)
        self.test_audio_path = "test_audio.mp3"

        # 创建一个临时音频文件用于测试
        with open(self.test_audio_path, "wb") as f:
            f.write(b"test audio data")

    def tearDown(self):
        # 清理测试数据
        if os.path.exists(self.test_audio_path):
            os.remove(self.test_audio_path)

    def test_initialization(self):
        # 测试初始化
        self.assertEqual(self.client.api_key, self.api_key)
        self.assertEqual(self.client.base_url, "https://api.siliconflow.cn/v1")
        self.assertEqual(self.client.headers, {"Authorization": f"Bearer {self.api_key}"})

    @patch("requests.get")
    def test_api_call_get(self, mock_get):
        # 测试GET请求
        mock_response = MagicMock()
        mock_response.json.return_value = {"success": True}
        mock_get.return_value = mock_response

        result = self.client.api_call("test/endpoint", method="GET", data={"param": "value"})

        mock_get.assert_called_once_with(
            "https://api.siliconflow.cn/v1/test/endpoint",
            headers={"Authorization": f"Bearer {self.api_key}"},
            params={"param": "value"}
        )
        self.assertEqual(result, {"success": True})

    @patch("requests.post")
    def test_api_call_post_json(self, mock_post):
        # 测试POST JSON请求
        mock_response = MagicMock()
        mock_response.json.return_value = {"success": True}
        mock_post.return_value = mock_response

        result = self.client.api_call("test/endpoint", method="POST", data={"key": "value"})

        mock_post.assert_called_once_with(
            "https://api.siliconflow.cn/v1/test/endpoint",
            headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"},
            json={"key": "value"}
        )
        self.assertEqual(result, {"success": True})

    @patch("requests.post")
    def test_api_call_post_multipart(self, mock_post):
        # 测试POST multipart/form-data请求
        mock_response = MagicMock()
        mock_response.json.return_value = {"success": True}
        mock_post.return_value = mock_response

        with open(self.test_audio_path, "rb") as f:
            files = {"file": f}
            result = self.client.api_call("test/endpoint", method="POST", data={"param": "value"}, files=files)

        # 验证请求被正确调用
        mock_post.assert_called()
        self.assertEqual(result, {"success": True})

    @patch("client.SiliconFlowClient.api_call")
    def test_transcribe_audio(self, mock_api_call):
        # 测试音频转录方法
        mock_response = {"text": "测试转录文本"}
        mock_api_call.return_value = mock_response

        result = self.client.transcribe_audio(self.test_audio_path)

        # 验证api_call被正确调用
        mock_api_call.assert_called_once()
        args, kwargs = mock_api_call.call_args
        self.assertEqual(args[0], "audio/transcriptions")
        self.assertEqual(kwargs["method"], "POST")
        self.assertEqual(kwargs["data"], {"model": "FunAudioLLM/SenseVoiceSmall"})
        self.assertIn("files", kwargs)
        self.assertIn("file", kwargs["files"])

        self.assertEqual(result, mock_response)

    @patch("client.SiliconFlowClient.api_call")
    def test_transcribe_audio_custom_model(self, mock_api_call):
        # 测试使用自定义模型的音频转录
        mock_response = {"text": "测试转录文本"}
        mock_api_call.return_value = mock_response
        custom_model = "custom-model"

        result = self.client.transcribe_audio(self.test_audio_path, model=custom_model)

        # 验证模型参数被正确传递
        args, kwargs = mock_api_call.call_args
        self.assertEqual(kwargs["data"], {"model": custom_model})

        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()


# 运行测试命令: python -m unittest sdk/siliconflow/test_client.py