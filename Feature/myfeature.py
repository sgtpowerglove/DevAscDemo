"""Basic feature: a small Greeter utility.

This module provides a tiny, well-documented `Greeter` class used
to produce friendly greeting strings and a formatted current time.

Example:
	from Feature.myfeature import Greeter
	g = Greeter("Hi")
	print(g.greet("Alice"))
	print(g.format_time())

This file intentionally keeps the feature minimal so it can be
imported and extended in demos and tests.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Greeter:
	"""A tiny utility for producing greetings and formatted times.

	Attributes:
		greeting: The prefix used when greeting someone (default: "Hello").
	"""

	greeting: str = "Hello"

	def greet(self, name: Optional[str]) -> str:
		"""Return a greeting for `name`.

		If `name` is falsy, returns a generic greeting.
		"""
		if not name:
			return f"{self.greeting}!"
		return f"{self.greeting}, {name}!"

	def format_time(self, when: Optional[datetime] = None) -> str:
		"""Return a compact, human-readable timestamp string.

		Args:
			when: Optional datetime to format. If omitted, use current UTC time.

		Returns:
			A string like "2025-12-09 14:35:22 UTC".
		"""
		when = when or datetime.utcnow()
		return when.strftime("%Y-%m-%d %H:%M:%S UTC")


__all__ = ["Greeter"]

