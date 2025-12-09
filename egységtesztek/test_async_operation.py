import pytest

from egységtesztek.async_operation import work_data


@pytest.mark.asyncio
async def test_work_data():
    res = await work_data()
    assert res == {"data": "value"}