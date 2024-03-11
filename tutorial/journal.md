stage 1: basic drf stuff, request methods. Created Models, serializers, model serializers, etc and first version of this api.
stage 2: @api view, Reponse, request.data

stage 3: MIXINS

Mixins in Django REST Framework (DRF) are a way to group common functionality that can be reused across multiple views. They provide additional methods and behavior to views without requiring inheritance from a specific base class.

In the provided code, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, and mixins.DestroyModelMixin are used.

Here's a brief explanation of each:

ListModelMixin: Provides a list method to handle GET requests for listing multiple objects. It expects a queryset attribute to be defined in the view which specifies the list of objects to be returned.

CreateModelMixin: Provides a create method to handle POST requests for creating new objects. It expects a serializer_class attribute to be defined in the view which specifies the serializer used for validating and saving the data.

RetrieveModelMixin: Provides a retrieve method to handle GET requests for retrieving a single object by its primary key (pk). It expects a queryset attribute to be defined in the view which specifies the list of objects to be searched.

UpdateModelMixin: Provides an update method to handle PUT requests for updating an existing object. It expects a queryset attribute to be defined in the view which specifies the list of objects to be searched, and a serializer_class attribute for validating and updating the data.

DestroyModelMixin: Provides a destroy method to handle DELETE requests for deleting an existing object. It expects a queryset attribute to be defined in the view which specifies the list of objects to be searched.

By using mixins, views can be kept concise and focused on their specific responsibilities, promoting code reuse and maintainability.

STAGE 4: GENERICS
DRF provides a set of already mixed-in generic views that we can use to trim down our views.py module even more.