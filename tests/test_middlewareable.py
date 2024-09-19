import pytest
from _pytest.capture import CaptureFixture
from python_middlewareable import MiddlewareableBase
from tests.stubs.fake_basic_middlewares import (
    Request,
    OneMiddleware,
    TwoMiddleware,
)


@pytest.mark.asyncio
async def test_basic_usage_instructions():
    class App(MiddlewareableBase[Request]):
        middlewares = [OneMiddleware, TwoMiddleware]

    app = App()

    result = await app.process_middlewares(Request(value="John"))

    assert result.value == "Hello, John from OneMiddleware from TwoMiddleware"


@pytest.mark.asyncio
async def test_execution_order(capsys: CaptureFixture[str]) -> None:
    class App(MiddlewareableBase[Request]):
        middlewares = [OneMiddleware, TwoMiddleware]

    # Create the app instance with the middleware
    app = App()

    # Process the request
    request = Request(value="John")
    await app.process_middlewares(request)

    # Capture the output
    captured = capsys.readouterr()

    # Expected output lines in order
    expected_output = [
        "OneMiddleware before",
        "TwoMiddleware before",
        "TwoMiddleware after",
        "OneMiddleware after",
    ]

    # Split the captured output into lines and compare with the expected
    # sequence
    output_lines = captured.out.strip().splitlines()

    assert output_lines == expected_output


@pytest.mark.asyncio
async def test_append_middlewares_dynamically():
    class App(MiddlewareableBase[Request]):
        pass

    app = App()

    app.middleware_instances.append(OneMiddleware())
    app.middleware_instances.append(TwoMiddleware())

    initial_request = Request(value="John")
    processed_request = await app.process_middlewares(initial_request)

    assert (
        processed_request.value
        == "Hello, John from OneMiddleware from TwoMiddleware"
    )
