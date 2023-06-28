from abc import abstractmethod
from typing import Any, Generator, Protocol, Union

TokenGen = Generator[str, None, None]
RESPONSE_TEXT_TYPE = Union[str, TokenGen]


# TODO: move into a `core` folder
class BaseOutputParser(Protocol):
    """Output parser class."""

    @abstractmethod
    def parse(self, output: str) -> Any:
        """Parse, validate, and correct errors programmatically."""

    @abstractmethod
    def format(self, output: str) -> str:
        """Format a query with structured output formatting instructions."""
