#!/usr/bin/python3

Import unittest
From datetime import datetime

From base_model import BaseModel

Class TestBaseModel(unittest.TestCase):

    Def test_constructor_no_args(self):
        Model = BaseModel()
        Self.assertIsInstance(model, BaseModel)
        Self.assertIsNotNone(model.id)
        Self.assertEqual(model.created_at, model.updated_at)
        Self.assertIsInstance(model.created_at, datetime)
        Self.assertIsInstance(model.updated_at, datetime)

    Def test_constructor_with_kwargs(self):
        Data = {
            ‘id’: ‘123’,
            ‘created_at’: ‘2022-01-01T00:00:00.000’,
            ‘updated_at’: ‘2022-01-02T00:00:00.000’,
            ‘name’: ‘Example’,
            ‘value’: 10
        }
        Model = BaseModel(**data)
        Self.assertIsInstance(model, BaseModel)
        Self.assertEqual(model.id, ‘123’)
        Self.assertEqual(model.created_at, datetime(2022, 1, 1))
        Self.assertEqual(model.updated_at, datetime(2022, 1, 2))
        Self.assertEqual(model.name, ‘Example’)
        Self.assertEqual(model.value, 10)

    Def test_save(self):
        Model = BaseModel()
        Old_updated_at = model.updated_at
        Model.save()
        Self.assertNotEqual(model.updated_at, old_updated_at)
        Self.assertIsInstance(model.updated_at, datetime)

    Def test_to_dict(self):
        Model = BaseModel()
        Data = model.to_dict()
        Self.assertIsInstance(data, dict)
        Self.assertEqual(data[‘__class__’], ‘BaseModel’)
        Self.assertEqual(data[‘id’], model.id)
        Self.assertEqual(data[‘created_at’], model.created_at.isoformat())
        Self.assertEqual(data[‘updated_at’], model.updated_at.isoformat())

If __name__ == ‘__main__’:
    Unittest.main()
```

Explanation:
