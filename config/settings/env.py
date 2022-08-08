import os
from typing import Any, Type

from ..utils import str_to_bool

__all__ = ["Config"]


class EnvVar:
    def __init__(self, var: str, type_: Type, default: Any = None):
        """
        Initiates a config value from environment variable

        :param var: the env var name
        :param type_: the type of the variable
        :param default: the default value

        :type type_: Type
        :type var: str
        :type default: Any
        """
        self._var = var
        self._type = type_
        self._default = default
        self._is_set = False

    # #
    # # OVERLOAD
    # #

    def __get__(self, instance, owner):
        """
        If not set, sets the environment variable value.

        :return: the env var value
        """
        if not self._is_set:
            self._set()
        return self._value

    def __set__(self, instance, value):
        """
        This attribute's value can't be altered.

        :raise AttributeError: Always.
        """
        raise AttributeError("can't set attribute")

    # #
    # # Methods
    # #

    def clear(self):
        """
        Marks the variable as unset.
        """
        self._is_set = False

    def _apply_type(self, value):
        """
        Applies the type to the given value.

        :param value: the value to cast into the expected type.
        """
        if self._type == list:
            return value.split(",")
        if self._type == bool:
            return str_to_bool(value)
        return self._type(value)

    def _set(self):
        """
        Sets the env var value and mark the var as set.
        """
        value = os.getenv(self._var)
        self._value = self._default if value is None else self._apply_type(value)
        self._is_set = True


class Config:
    """
    App configuration.
    """

    @classmethod
    def clear(cls):
        """
        Marks all configuration as unset.
        """
        for v in cls.__dict__.values():
            if isinstance(v, EnvVar):
                v.clear()

    ENVIRONMENT = EnvVar("ENVIRONMENT", str, "development")

    SECRET_KEY = EnvVar("SECRET_KEY", str)

    # #
    # LOGGING
    # #

    LOG_LEVEL = EnvVar("LOG_LEVEL", str, "INFO")
    DISABLED_LOGGERS = EnvVar("DISABLED_LOGGERS", str)

    # #
    # POSTGRES CONFIGURATION
    # #

    POSTGRES_HOST = EnvVar("POSTGRES_HOST", str, "localhost")
    POSTGRES_PORT = EnvVar("POSTGRES_PORT", int, 5432)
    POSTGRES_DB = EnvVar("POSTGRES_DB", str, "navi2")
    POSTGRES_USER = EnvVar("POSTGRES_USER", str, "navi2")
    POSTGRES_PASSWORD = EnvVar("POSTGRES_PASSWORD", str)

    # #
    # SENTRY
    # #

    SENTRY_DSN = EnvVar("SENTRY_DSN", str)
