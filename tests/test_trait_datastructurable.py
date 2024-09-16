import pytest
from tests.stubs.fake_datastructurable_trait import (
    PayloadData,
    ResponseData,
    Request,
    OneMiddleware,
)
from src.middlewareable import Middlewareable as MiddlewareableBase
from src.traits.data_structurable.data_structurable import DataStructurable
from src.traits.data_structurable.dtos.transport_data import (
    TransportData as TransportDataBase,
)


@pytest.mark.asyncio
async def test_trait_datastructurable_instructions():
    class App(DataStructurable, MiddlewareableBase[Request]):
        middlewares = [OneMiddleware]

    app = App()

    # request
    request = Request(
        request_data=PayloadData(name="John"),
        response_data=ResponseData(),
        transport_data=TransportDataBase(),
    )

    # process request
    result = await app.process_middlewares(request)

    assert result.response_data.value == "John from OneMiddleware"
