# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from julep import Julep, AsyncJulep
from tests.utils import assert_matches_type
from julep.types.tasks import (
    ExecutionListResponse,
    ExecutionCreateResponse,
    ExecutionUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExecutions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Julep) -> None:
        execution = client.tasks.executions.create(
            task_id="task_id",
            input={},
        )
        assert_matches_type(ExecutionCreateResponse, execution, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Julep) -> None:
        execution = client.tasks.executions.create(
            task_id="task_id",
            input={},
            error="error",
            metadata={},
            output={},
        )
        assert_matches_type(ExecutionCreateResponse, execution, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Julep) -> None:
        response = client.tasks.executions.with_raw_response.create(
            task_id="task_id",
            input={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(ExecutionCreateResponse, execution, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Julep) -> None:
        with client.tasks.executions.with_streaming_response.create(
            task_id="task_id",
            input={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(ExecutionCreateResponse, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.tasks.executions.with_raw_response.create(
                task_id="",
                input={},
            )

    @parametrize
    def test_method_update(self, client: Julep) -> None:
        execution = client.tasks.executions.update(
            execution_id="execution_id",
            task_id="task_id",
            status="queued",
        )
        assert_matches_type(ExecutionUpdateResponse, execution, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Julep) -> None:
        response = client.tasks.executions.with_raw_response.update(
            execution_id="execution_id",
            task_id="task_id",
            status="queued",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(ExecutionUpdateResponse, execution, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Julep) -> None:
        with client.tasks.executions.with_streaming_response.update(
            execution_id="execution_id",
            task_id="task_id",
            status="queued",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(ExecutionUpdateResponse, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.tasks.executions.with_raw_response.update(
                execution_id="execution_id",
                task_id="",
                status="queued",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            client.tasks.executions.with_raw_response.update(
                execution_id="",
                task_id="task_id",
                status="queued",
            )

    @parametrize
    def test_method_list(self, client: Julep) -> None:
        execution = client.tasks.executions.list(
            task_id="task_id",
        )
        assert_matches_type(ExecutionListResponse, execution, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Julep) -> None:
        execution = client.tasks.executions.list(
            task_id="task_id",
            direction="asc",
            limit=0,
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(ExecutionListResponse, execution, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Julep) -> None:
        response = client.tasks.executions.with_raw_response.list(
            task_id="task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(ExecutionListResponse, execution, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Julep) -> None:
        with client.tasks.executions.with_streaming_response.list(
            task_id="task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(ExecutionListResponse, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.tasks.executions.with_raw_response.list(
                task_id="",
            )


class TestAsyncExecutions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncJulep) -> None:
        execution = await async_client.tasks.executions.create(
            task_id="task_id",
            input={},
        )
        assert_matches_type(ExecutionCreateResponse, execution, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJulep) -> None:
        execution = await async_client.tasks.executions.create(
            task_id="task_id",
            input={},
            error="error",
            metadata={},
            output={},
        )
        assert_matches_type(ExecutionCreateResponse, execution, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJulep) -> None:
        response = await async_client.tasks.executions.with_raw_response.create(
            task_id="task_id",
            input={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(ExecutionCreateResponse, execution, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJulep) -> None:
        async with async_client.tasks.executions.with_streaming_response.create(
            task_id="task_id",
            input={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(ExecutionCreateResponse, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.tasks.executions.with_raw_response.create(
                task_id="",
                input={},
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncJulep) -> None:
        execution = await async_client.tasks.executions.update(
            execution_id="execution_id",
            task_id="task_id",
            status="queued",
        )
        assert_matches_type(ExecutionUpdateResponse, execution, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncJulep) -> None:
        response = await async_client.tasks.executions.with_raw_response.update(
            execution_id="execution_id",
            task_id="task_id",
            status="queued",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(ExecutionUpdateResponse, execution, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncJulep) -> None:
        async with async_client.tasks.executions.with_streaming_response.update(
            execution_id="execution_id",
            task_id="task_id",
            status="queued",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(ExecutionUpdateResponse, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.tasks.executions.with_raw_response.update(
                execution_id="execution_id",
                task_id="",
                status="queued",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            await async_client.tasks.executions.with_raw_response.update(
                execution_id="",
                task_id="task_id",
                status="queued",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncJulep) -> None:
        execution = await async_client.tasks.executions.list(
            task_id="task_id",
        )
        assert_matches_type(ExecutionListResponse, execution, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJulep) -> None:
        execution = await async_client.tasks.executions.list(
            task_id="task_id",
            direction="asc",
            limit=0,
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(ExecutionListResponse, execution, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJulep) -> None:
        response = await async_client.tasks.executions.with_raw_response.list(
            task_id="task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(ExecutionListResponse, execution, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJulep) -> None:
        async with async_client.tasks.executions.with_streaming_response.list(
            task_id="task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(ExecutionListResponse, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.tasks.executions.with_raw_response.list(
                task_id="",
            )
