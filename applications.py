"""
FastAPI applications.
"""
from typing import Any, Dict, Optional

from fastapi import FastAPI
from fastapi.routing import APIRouter


class FastAPIInstance:
    """
    A class to manage FastAPI instances.
    """

    def __init__(self, **kwargs: Any) -> None:
        """
        Initialize the FastAPI instance.

        Args:
            **kwargs: Additional keyword arguments to pass to FastAPI.
        """
        self.app = FastAPI(**kwargs)

    def include_router(self, router: APIRouter, **kwargs: Any) -> None:
        """
        Include a router in the FastAPI application.

        Args:
            router: The APIRouter to include.
            **kwargs: Additional keyword arguments to pass to include_router.
        """
        self.app.include_router(router, **kwargs)

    def get_app(self) -> FastAPI:
        """
        Get the FastAPI application instance.

        Returns:
            The FastAPI application instance.
        """
        return self.app


def create_app(**kwargs: Any) -> FastAPI:
    """
    Create a FastAPI application.

    Args:
        **kwargs: Additional keyword arguments to pass to FastAPI.

    Returns:
        A FastAPI application instance.
    """
    return FastAPI(**kwargs)
