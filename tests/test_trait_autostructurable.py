import pytest
from tests.stubs.fake_datastructurable_trait import (
    RequestData,
    ResponseData,
    Request,
    OneMiddleware,
)
from python_middlewareable import (
    MiddlewareableBase,
    TransportDataBase,
    AutoStructurable,
)


@pytest.mark.asyncio
async def test_trait_autostructurable_instructions():
    class App(
        AutoStructurable[Request, ResponseData, TransportDataBase],
        MiddlewareableBase[Request],
    ):
        middlewares = [OneMiddleware]

        # same classes passed to "AutoStructurable" above
        request_class = Request
        response_data_class = ResponseData
        transport_data_class = TransportDataBase

    app = App()

    # process request
    result = await app.process_middlewares_from_payload(
        data=RequestData(name="John")
    )

    assert result.value == "John from OneMiddleware"
