from rest_framework import serializers
from django.core.exceptions import ValidationError

from .models import Entity, Property




class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = (
            'key',
            'value',
        )


class EntitySerializer(serializers.ModelSerializer):
    value = serializers.IntegerField()
    # =======================================
    # решение 3 вопроса
    # =======================================
    properties = PropertySerializer(read_only=True, many=True)
    
    # =======================================
    # регение 2 вопроса
    # чтобы сериализатор смог принять поле "data[value]" и сохранить в поле value
    # решил немного изменить метод is_valid
    # =======================================

    def is_valid(self, *, raise_exception=False):
        assert hasattr(self, 'initial_data'), (
            'Cannot call `.is_valid()` as no `data=` keyword argument was '
            'passed when instantiating the serializer instance.'
        )
        if not hasattr(self, '_validated_data'):
            try:
                # вар 1.
                # если находим "data[value]" в initial_data -->> 
                for k, v in self.initial_data.items():
                    if k == 'data[value]':
                        self._validated_data = {'value': v}
                        self._errors = {}
                        return not bool(self._errors)
                # =======================================
                # вар 2.
                # в переменную all_names_fields получим имена все полей
                # all_names_fields = self.get_field_names(declared_fields=self.get_fields(), info='info')
                # try:
                #     # в переменную value попробуем получить "data[value]" из initial_data
                #     value = self.initial_data['data[value]'] # value = list(self.initial_data.values())[-1]
                #     # пройдем по всем полям и если имя поля == value
                #     # то в словарь _validated_data добавим имя этого поля и полученное значение
                #     for name_field in all_names_fields:
                #         if name_field == 'value':
                #             self._validated_data = {name_field: value}
                #             self._errors = {}
                #             return not bool(self._errors)
                # except KeyError:
                # =======================================
                    self._validated_data = self.run_validation(self.initial_data)
            except ValidationError as exc:
                self._validated_data = {}
                self._errors = exc.detail
            else:
                self._errors = {}

        if self._errors and raise_exception:
            raise ValidationError(self.errors)

        return not bool(self._errors)
  
    class Meta:
        model = Entity
        fields = (
            'value',
            'properties',
        )


