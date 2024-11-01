import pytest
from _pytest.capture import CaptureFixture
from python_middlewareable import (
    MiddlewarePipeline,
    MiddlewareStage,
    MiddlewareNextCall,
)


class AddOneStage(MiddlewareStage[int]):
    async def __call__(
        self, payload: int, next_call: MiddlewareNextCall
    ) -> int:
        payload += 1
        return await next_call(payload)


class TimesTwoStage(MiddlewareStage[int]):
    async def __call__(
        self, payload: int, next_call: MiddlewareNextCall
    ) -> int:
        payload *= 2
        return await next_call(payload)


class TimesThreeStage(MiddlewareStage[int]):
    async def __call__(
        self, payload: int, next_call: MiddlewareNextCall
    ) -> int:
        payload *= 3
        return await next_call(payload)


@pytest.mark.asyncio
async def test_lambda_stages():
    pipeline = (
        (MiddlewarePipeline[int]())
        .pipe(lambda x, next_call: next_call(x + 1))
        .pipe(lambda x, next_call: next_call(x * 2))
        .pipe(lambda x, next_call: next_call(x + 3))
    )

    assert await pipeline.process(3) == 11
    assert await pipeline.process(5) == 15


@pytest.mark.asyncio
async def test_classbased_stages():
    pipeline = (
        (MiddlewarePipeline[int]())
        .pipe(TimesTwoStage())
        .pipe(AddOneStage())
        .pipe(TimesThreeStage())
    )

    assert await pipeline.process(5) == 33


@pytest.mark.asyncio
async def test_pipelinebased_stages():
    sub_pipeline1 = (
        (MiddlewarePipeline[int]())
        .pipe(TimesTwoStage())
        .pipe(AddOneStage())
        .pipe(TimesThreeStage())
    )

    sub_pipeline2 = (
        (MiddlewarePipeline[int]())
        .pipe(lambda x, next_call: next_call(x + 1))
        .pipe(lambda x, next_call: next_call(x * 2))
    )

    pipeline = (
        (MiddlewarePipeline[int]())
        .pipe(TimesThreeStage())
        .pipe(sub_pipeline1)
        .pipe(sub_pipeline2)
        .pipe(lambda payload, next_call: next_call(payload * 2))
    )

    assert await pipeline.process(10) == 736


@pytest.mark.asyncio
async def test_execution_order(capsys: CaptureFixture[str]) -> None:
    class OneMiddleware(MiddlewareStage[str]):
        async def __call__(
            self, payload: str, next_call: MiddlewareNextCall
        ) -> str:
            print("OneMiddleware before")
            result = await next_call(payload)
            print("OneMiddleware after")
            return result

    class TwoMiddleware(MiddlewareStage[str]):
        async def __call__(
            self, payload: str, next_call: MiddlewareNextCall
        ) -> str:
            print("TwoMiddleware before")
            result = await next_call(payload)
            print("TwoMiddleware after")
            return result

    pipeline = (
        (MiddlewarePipeline[str]()).pipe(OneMiddleware()).pipe(TwoMiddleware())
    )

    await pipeline.process("")

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
