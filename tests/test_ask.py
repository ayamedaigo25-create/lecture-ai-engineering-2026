from types import SimpleNamespace

from app import ask as ask_module


def test_ask_prints_token_usage(monkeypatch, capsys):
    response = SimpleNamespace(
        text="answer",
        usage_metadata=SimpleNamespace(prompt_token_count=12, candidates_token_count=7),
    )

    class Models:
        def generate_content(self, **kwargs):
            return response

    class Client:
        def __init__(self, api_key):
            self.models = Models()

    monkeypatch.setattr(ask_module.genai, "Client", Client)
    monkeypatch.setattr(ask_module, "get_api_key", lambda: "test-key")

    assert ask_module.ask("question") == "answer"
    assert capsys.readouterr().out == "[tokens] 入力: 12 / 出力: 7\n"