# -*- coding: utf-8 -*-
import abc

from schematizer import models


class BaseConverter(object):

    source_type = models.SchemaKindEnum.Unknown
    target_type = models.SchemaKindEnum.Unknown

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def convert(self, src_schema):
        """Convert the given source schema to the target schema type."""
        raise NotImplementedError()


class SchemaConversionException(Exception):
    pass


class UnsupportedTypeException(SchemaConversionException):
    pass


class AvroMetaDataKeyEnum(object):
    """Valid metadata keys that can be added in the Avro Field type"""

    FIX_LEN = 'fixlen'        # length of char type
    MAX_LEN = 'maxlen'        # length of varchar type
    PRIMARY_KEY = 'pkey'      # whether it is primary key
    TIMESTAMP = 'timestamp'   # whether it is a timestamp field
    UNSIGNED = 'unsigned'     # whether the int type is unsigned
    PRECISION = 'precision'   # precision of numeric type
    SCALE = 'scale'           # scale of numeric type
    FIXED_POINT = 'fixed_pt'  # fixed-point numeric type
