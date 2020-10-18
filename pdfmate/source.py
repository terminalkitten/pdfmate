# -*- coding: utf-8 -*-
import io
import os
from typing import NoReturn, Union

from .errors import InvalidSourceError


class Source(object):
    def __init__(self, url_or_file, type_) -> None:
        self.source = url_or_file
        self.type = type_

        if self.type == 'file':
            self.checkFiles()

    def isUrl(self) -> bool:
        return 'url' in self.type

    def isFile(self, path=None) -> bool:
        if path:
            return (
                isinstance(path, io.IOBase)
                or path.__class__.__name__ == 'StreamReaderWriter'
            )
        else:
            return 'file' in self.type

    def checkFiles(self):
        if not hasattr(self.source, 'read') and not os.path.exists(self.source):
            raise InvalidSourceError('No such file: %s' % self.source)

    def isString(self) -> bool:
        return 'string' in self.type

    def isFileObj(self) -> bool:
        return hasattr(self.source, 'read')

    def to_s(self) -> str:
        return self.source

    def _append_protocol(self, path, protocol) -> str:
        prefix = protocol if not path.startswith(protocol) else ''
        return prefix + path

    def urlPath(self) -> Union[str, NoReturn]:
        if self.isUrl():
            return self.to_s()
        elif self.isFile() and not self.isFileObj():
            return self._append_protocol(os.path.abspath(self.to_s()), 'file://')
        raise ValueError('Source invalid - cannot be converted to URL paths')
