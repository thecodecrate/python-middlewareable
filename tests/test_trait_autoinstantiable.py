import pytest
from tests.stubs.fake_datastructurable_trait import (
    PayloadData,
    ResponseData,
    Request,
    OneMiddleware,
)
from src.middlewareable import Middlewareable as MiddlewareableBase
from src.traits.data_structurable.dtos.transport_data import (
    TransportData as TransportDataBase,
)
from src.traits.auto_instantiable.auto_instantiable import (
    AutoInstantiable,
)


@pytest.mark.asyncio
async def test_trait_autoinstantiable_instructions():
    class App(
        AutoInstantiable[Request, ResponseData, TransportDataBase],
        MiddlewareableBase[Request],
    ):
        middlewares = [OneMiddleware]

        # same classes passed to "AutoInstantiable" above
        request_class = Request
        response_data_class = ResponseData
        transport_data_class = TransportDataBase

    app = App()

    # process request
    result = await app.process_middlewares_from_payload(data=PayloadData(name="John"))

    assert result.value == "John from OneMiddleware"
