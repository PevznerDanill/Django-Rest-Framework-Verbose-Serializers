import pytest
from rest_framework import serializers
import drf_verbose_serializers


# Test object for serialization
class SimpleObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def test_verbose_char_field():
    """Test basic usage of VerboseCharField."""
    class TestSerializer(drf_verbose_serializers.VerboseSerializerMixin, serializers.Serializer):
        name = drf_verbose_serializers.VerboseCharField(verbose_field_name='Name')
    
    obj = SimpleObject(name="John")
    serializer = TestSerializer(obj)
    
    assert 'Name' in serializer.data
    assert serializer.data['Name'] == "John"


def test_field_without_verbose_name():
    """Test that fields without verbose_field_name use the original field name."""
    class TestSerializer(drf_verbose_serializers.VerboseSerializerMixin, serializers.Serializer):
        name = drf_verbose_serializers.VerboseCharField(verbose_field_name='Full Name')
        age = drf_verbose_serializers.VerboseIntegerField()  # No verbose name
    
    obj = SimpleObject(name="John", age=30)
    serializer = TestSerializer(obj)
    
    assert 'Full Name' in serializer.data
    assert 'age' in serializer.data
    assert serializer.data['Full Name'] == "John"
    assert serializer.data['age'] == 30 